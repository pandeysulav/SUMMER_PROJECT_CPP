import os
import json
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder, PolynomialFeatures
from sklearn.compose import ColumnTransformer
from sklearn.utils.validation import check_is_fitted
from config import CSV_PATH, PREDICTIONS_FILE, OUTPUT_DIR, REPORT_PATH, METRICS_TO_PREDICT, FEATURE_COLUMNS, REQUIRED_COLUMNS, FITNESS_THRESHOLDS, FITNESS_LEVELS, FORECAST_DAYS


def load_data():
    print(f"Loading data from {CSV_PATH}")
    df = pd.read_csv(CSV_PATH)
    missing = set(REQUIRED_COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns in dataset: {missing}")

    df["date"] = pd.to_datetime(df["date"])
    df["day_index"] = (df["date"] - df["date"].min()).dt.days
    return df


def build_and_train_model(df, target_column):
    if not set(FEATURE_COLUMNS).issubset(df.columns):
        missing_features = set(FEATURE_COLUMNS) - set(df.columns)
        raise ValueError(f"Missing features: {missing_features}")

    X = df[FEATURE_COLUMNS]
    y = df[target_column]

    numeric_features = ["age", "height_cm", "weight_kg", "bmi", "day_index"]
    categorical_features = ["user_id"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", "passthrough", numeric_features),
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ]
    )

    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("poly", PolynomialFeatures(degree=2, include_bias=False)),
            ("regressor", LinearRegression()),
        ]
    )

    print(f"Training model for {target_column}...")
    model.fit(X, y)
    print(f"Model trained for {target_column} on {len(df)} samples.")
    return model


def predict_for_user(models, user_df, user_id, start_index):
    future_data = []
    for i in range(FORECAST_DAYS):
        day_data = user_df.iloc[-1].copy()
        day_data["day_index"] = start_index + i + 1
        future_data.append(day_data)

    future_df = pd.DataFrame(future_data)

    predictions = {}
    for metric in METRICS_TO_PREDICT:
        if metric in models:
            X_pred = future_df[FEATURE_COLUMNS]
            predictions[metric] = list(models[metric].predict(X_pred))
            print(f"Predicted {FORECAST_DAYS} days for user {user_id}")
    return predictions


def calculate_fitness_score(avg_metrics):
    score = 0

    steps = avg_metrics["steps"]
    score += 30 if steps >= FITNESS_THRESHOLDS["steps"]["target"] else (steps / FITNESS_THRESHOLDS["steps"]["target"]) * 30

    calories = avg_metrics["calories"]
    if FITNESS_THRESHOLDS["calories"]["target_min"] <= calories <= FITNESS_THRESHOLDS["calories"]["target_max"]:
        score += 30
    else:
        score += max(0, 30 - abs(calories - 2500) / 50)

    sleep = avg_metrics["sleep_hours"]
    if FITNESS_THRESHOLDS["sleep_hours"]["target_min"] <= sleep <= FITNESS_THRESHOLDS["sleep_hours"]["target_max"]:
        score += 20
    else:
        score += max(0, 20 - abs(sleep - 7) * 5)

    water = avg_metrics["water_intake_l"]
    score += 20 if water >= FITNESS_THRESHOLDS["water_intake_l"]["target"] else (water / 2.5) * 20

    return round(min(score, 100), 2)


def fitness_level(score):
    if score < 50:
        return "Poor"
    elif score < 75:
        return "Average"
    elif score < 90:
        return "Good"
    else:
        return "Excellent"


def generate_report(all_scores, all_averages):
    report_lines = []
    report_lines.append("=" * 50)
    report_lines.append("ML Fitness Predictor: User Fitness Summary")
    report_lines.append("=" * 50 + "\n")
    report_lines.append(f"Generated on: {datetime.now().strftime('%B %d, %Y')}\n")
    report_lines.append("This report summarizes fitness assessments for users based on predictions")
    report_lines.append("from the ML Fitness Predictor, using data from {} to {}.".format(
        (datetime.now().date() + timedelta(days=1)).strftime("%Y-%m-%d"),
        (datetime.now().date() + timedelta(days=FORECAST_DAYS)).strftime("%Y-%m-%d"),
    ))
    report_lines.append("The following sections provide fitness scores and personalized recommendations.\n")

    report_lines.append("Fitness Scores")
    report_lines.append("-" * 50)
    report_lines.append("User ID | Fitness Score | Fitness Level")
    report_lines.append("-" * 50)
    for user_id, score in all_scores.items():
        level = fitness_level(score)
        report_lines.append(f"{user_id:<8} | {score:>13} | {level}")

    report_lines.append("\nPersonalized Recommendations")
    report_lines.append("-" * 50)
    for user_id, avg in all_averages.items():
        score = all_scores[user_id]
        level = fitness_level(score)
        report_lines.append(f"User {user_id} (Fitness Score: {score:.2f}, {level})")
        report_lines.append(f"  - Monitor calorie intake to avoid excess. Current average: {round(avg['calories'])} calories/day")
        report_lines.append(f"  - Aim for 7-8 hours of sleep per night. Current average: {round(avg['sleep_hours'], 1)} hours/night")
        report_lines.append(f"  - Drink more water, aiming for 2.5-3.5 liters daily. Current average: {round(avg['water_intake_l'], 1)}L/day\n")

    report_lines.append("=" * 50)
    report_lines.append("End of Report\nGenerated by ML Fitness Predictor")
    report_lines.append("=" * 50)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(REPORT_PATH, 'w') as f:
        f.write('\n'.join(report_lines))
    print(f"Report saved to {REPORT_PATH}")


def main():
    df = load_data()

    models = {}
    for metric in METRICS_TO_PREDICT:
        models[metric] = build_and_train_model(df, metric)

    all_predictions = {}
    all_scores = {}
    all_averages = {}

    for user_id in df["user_id"].unique():
        user_df = df[df["user_id"] == user_id].sort_values("date")
        start_index = user_df["day_index"].max()
        predictions = predict_for_user(models, user_df, user_id, start_index)

        # Store predictions
        all_predictions[int(user_id)] = predictions

        # Calculate averages
        avg_metrics = {metric: np.mean(values) for metric, values in predictions.items()}
        all_averages[int(user_id)] = avg_metrics

        # Score
        score = calculate_fitness_score(avg_metrics)
        all_scores[int(user_id)] = score

    # Save predictions as JSON
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    serializable_predictions = {str(int(k)): v for k, v in all_predictions.items()}
    with open(PREDICTIONS_FILE, 'w') as f:
        json.dump(serializable_predictions, f, indent=4)

    # Save summary report
    generate_report(all_scores, all_averages)


if __name__ == "__main__":
    main()
