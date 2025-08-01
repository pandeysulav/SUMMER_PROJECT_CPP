import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder, PolynomialFeatures
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn import __version__ as sklearn_version
from datetime import datetime

def build_and_train_model(data, target_metric):
    """Trains a Linear Regression model for a specific metric (e.g., steps)."""
    print(f"Training a model to predict {target_metric}...")
    
    if target_metric not in data.columns:
        raise ValueError(f"Target metric '{target_metric}' not found in data columns: {data.columns.tolist()}")
    
    features = ['user_id', 'day_index', 'age', 'height_cm', 'weight_kg', 'bmi']
    
    missing_features = [f for f in features if f not in data.columns]
    if missing_features:
        raise ValueError(f"Missing features in data: {missing_features}")
    
    sklearn_major_version = int(sklearn_version.split('.')[0])
    sklearn_minor_version = int(sklearn_version.split('.')[1])
    
    if sklearn_major_version > 1 or (sklearn_major_version == 1 and sklearn_minor_version >= 2):
        onehot_params = {'sparse_output': False, 'handle_unknown': 'ignore'}
    else:
        onehot_params = {'sparse': False, 'handle_unknown': 'ignore'}
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('user_id', OneHotEncoder(**onehot_params), ['user_id']),
            ('day_trend', PolynomialFeatures(degree=2, include_bias=False), ['day_index']),
            ('numeric', 'passthrough', ['age', 'height_cm', 'weight_kg', 'bmi'])
        ])
    
    model = Pipeline([
        ('preprocessor', preprocessor),
        ('regressor', LinearRegression())
    ])
    
    X = data[features].copy()
    y = data[target_metric].copy()
    
    mask = ~(X.isnull().any(axis=1) | y.isnull())
    X = X[mask]
    y = y[mask]
    
    if len(X) == 0:
        raise ValueError(f"No valid data available for training {target_metric} model")
    
    model.fit(X, y)
    print(f"Model for {target_metric} trained on {len(X)} samples!")
    
    return model

def forecast_future(model, data, user_id, days_ahead=14):
    """Predicts future values for a user based on their latest data."""
    print(f"Making predictions for user {user_id}...")
    
    user_id_str = str(user_id)
    user_data = data[data['user_id'] == user_id_str].copy()
    
    if user_data.empty:
        print(f"No data found for user {user_id}. Available users: {data['user_id'].unique().tolist()}")
        raise ValueError(f"No data for user {user_id}")
    
    try:
        last_user_record = user_data.sort_values('day_index').iloc[-1]
        print(f"Found latest data for user {user_id} on day {last_user_record['day_index']}")
    except Exception as e:
        print(f"Error getting latest record for user {user_id}: {e}")
        raise ValueError(f"Could not get latest data for user {user_id}")
    
    last_day = last_user_record['day_index']
    
    future_days = np.arange(last_day + 1, last_day + days_ahead + 1)
    future_data = pd.DataFrame({
        'user_id': [user_id_str] * days_ahead,
        'day_index': future_days,
        'age': [last_user_record['age']] * days_ahead,
        'height_cm': [last_user_record['height_cm']] * days_ahead,
        'weight_kg': [last_user_record['weight_kg']] * days_ahead,
        'bmi': [last_user_record['bmi']] * days_ahead
    })
    
    try:
        predictions = model.predict(future_data)
        predictions = np.maximum(predictions, 0)
        print(f"Predicted {len(predictions)} days for user {user_id}")
        return list(zip(future_days, predictions))
    except Exception as e:
        print(f"Error making predictions for user {user_id}: {e}")
        raise ValueError(f"Prediction failed for user {user_id}: {e}")

def calculate_fitness_score(predictions, metric_weights, fitness_level="good"):
    """Calculate a fitness score based on predicted metrics."""
    steps, calories, sleep, water = predictions
    weights = metric_weights[fitness_level]
    
    # Normalize metrics (example ranges for normalization)
    norm_steps = min(steps / 10000, 1.0)  # Max 10,000 steps
    norm_calories = min((4000 - calories) / 2000, 1.0) if calories > 2000 else 1.0  # Lower calories better
    norm_sleep = min(sleep / 8, 1.0)  # Max 8 hours
    norm_water = min(water / 3.5, 1.0)  # Max 3.5 liters
    
    # Weighted sum for fitness score
    score = (
        weights['steps'] * norm_steps +
        weights['calories'] * norm_calories +
        weights['sleep'] * norm_sleep +
        weights['water'] * norm_water
    ) * 100
    
    # Adjust score range based on fitness level
    if fitness_level == "good":
        score = min(max(score * 0.85, 70), 85)  # Good: 70-85
    elif fitness_level == "excellent":
        score = min(max(score * 1.0, 85), 100)  # Excellent: 85-100
    
    return round(score, 2)

def generate_recommendations(user_id, fitness_score, predictions, fitness_level="good"):
    """Generate personalized recommendations based on fitness score and level."""
    _, calories, sleep, water = predictions
    recommendations = []
    
    if fitness_level == "good":
        recommendations.append(f"Monitor calorie intake to avoid excess. Current average: {calories:.0f} calories/day")
        recommendations.append(f"Drink more water, aiming for 2.5-3.5 liters daily. Current average: {water:.1f}L/day")
        if sleep < 7:
            recommendations.append(f"Aim for 7-8 hours of sleep per night. Current average: {sleep:.1f} hours/night")
    elif fitness_level == "excellent":
        recommendations.append(f"Maintain balanced calorie intake. Current average: {calories:.0f} calories/day")
        recommendations.append(f"Continue hydration, aiming for 3.0-4.0 liters daily. Current average: {water:.1f}L/day")
        if sleep < 7.5:
            recommendations.append(f"Optimize sleep to 7.5-8.5 hours for peak performance. Current average: {sleep:.1f} hours/night")
        recommendations.append("Incorporate high-intensity interval training (HIIT) 2-3 times/week to sustain fitness.")
    
    return recommendations

def generate_summary(data, models, fitness_level="good"):
    """Generate a fitness summary for all users."""
    metric_weights = {
        "good": {"steps": 0.4, "calories": 0.3, "sleep": 0.2, "water": 0.1},
        "excellent": {"steps": 0.35, "calories": 0.25, "sleep": 0.25, "water": 0.15}
    }
    summary = []
    summary.append("=" * 50)
    summary.append(f"ML Fitness Predictor: User Fitness Summary ({fitness_level.capitalize()})")
    summary.append("=" * 50)
    summary.append(f"\nGenerated on: {datetime.now().strftime('%B %d, %Y')}\n")
    summary.append("This report summarizes fitness assessments for 15 users based on predictions")
    summary.append(f"from the ML Fitness Predictor, using data from July 3, 2025, to July 17, 2025.")
    
    summary.append("\nFitness Scores")
    summary.append("-" * 50)
    summary.append("User ID | Fitness Score | Fitness Level")
    summary.append("-" * 50)
    
    recommendations_section = ["\nPersonalized Recommendations", "-" * 50]
    
    for user_id in range(1, 16):
        try:
            # Predict metrics for the user
            steps_pred = forecast_future(models['steps'], data, user_id)[-1][1]
            calories_pred = forecast_future(models['calories'], data, user_id)[-1][1]
            sleep_pred = forecast_future(models['sleep'], data, user_id)[-1][1]
            water_pred = forecast_future(models['water'], data, user_id)[-1][1]
            
            predictions = (steps_pred, calories_pred, sleep_pred, water_pred)
            fitness_score = calculate_fitness_score(predictions, metric_weights, fitness_level)
            
            # Assign fitness level based on score
            level = "Good" if fitness_level == "good" else "Excellent"
            
            summary.append(f"{user_id:<7} | {fitness_score:>12.2f} | {level}")
            
            recommendations = generate_recommendations(user_id, fitness_score, predictions, fitness_level)
            recommendations_section.append(f"User {user_id} (Fitness Score: {fitness_score:.2f}, {level})")
            recommendations_section.extend([f"  - {rec}" for rec in recommendations])
            recommendations_section.append("")
        
        except Exception as e:
            print(f"Error processing user {user_id}: {e}")
            continue
    
    summary.extend(recommendations_section)
    summary.append("=" * 50)
    summary.append("End of Report")
    summary.append("Generated by ML Fitness Predictor")
    summary.append("=" * 50)
    
    with open(f"summary_{fitness_level}.txt", "w") as f:
        f.write("\n".join(summary))
    
    return summary

# Example usage (assuming data and models are available)
if __name__ == "__main__":
    # Sample data for demonstration (replace with actual data loading)
    data = pd.DataFrame({
        'user_id': [str(i % 15 + 1) for i in range(150)],
        'day_index': list(range(1, 11)) * 15,
        'age': np.random.randint(20, 50, 150),
        'height_cm': np.random.uniform(150, 190, 150),
        'weight_kg': np.random.uniform(50, 100, 150),
        'steps': np.random.uniform(5000, 12000, 150),
        'calories': np.random.uniform(2000, 3500, 150),
        'sleep': np.random.uniform(5, 9, 150),
        'water': np.random.uniform(1.5, 3.0, 150)
    })
    data['bmi'] = data['weight_kg'] / (data['height_cm'] / 100) ** 2
    
    # Train models for each metric
    models = {
        'steps': build_and_train_model(data, 'steps'),
        'calories': build_and_train_model(data, 'calories'),
        'sleep': build_and_train_model(data, 'sleep'),
        'water': build_and_train_model(data, 'water')
    }
    
    # Generate summaries for both fitness levels
    generate_summary(data, models, fitness_level="good")
    generate_summary(data, models, fitness_level="excellent")