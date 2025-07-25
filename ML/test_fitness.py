# import pandas as pd
# import numpy as np
# from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import OneHotEncoder, PolynomialFeatures
# from sklearn.compose import ColumnTransformer
# from sklearn.pipeline import Pipeline
# import json

# # Let's load and clean up our fitness data to make it ready for modeling
# def load_fitness_data(file_path):
#     """Reads the CSV file and prepares it for analysis."""
#     print("Loading your fitness data... Let's see what we've got!")
#     try:
#         data = pd.read_csv(file_path)
#     except FileNotFoundError:
#         print(f"Oops! Couldn't find the file at {file_path}. Double-check the path and try again.")
#         raise
    
#     # Check if all expected columns are present
#     expected_columns = ['user_id', 'date', 'age', 'height_cm', 'weight_kg', 'steps', 'calories', 'sleep_hours', 'water_intake_l', 'bmi']
#     missing = [col for col in expected_columns if col not in data.columns]
#     if missing:
#         print(f"Hmm, the CSV is missing some columns: {missing}. Please check the file format.")
#         raise ValueError(f"Missing columns: {missing}")
    
#     # Clean up user_id: convert to string and remove '.0' suffix
#     data['user_id'] = data['user_id'].astype(str).str.replace(r'\.0$', '', regex=True)
#     # Remove any rows with invalid user_id (like 'nan')
#     data = data[data['user_id'] != 'nan']
#     print(f"Found these user IDs: {data['user_id'].unique().tolist()}")
    
#     # Convert date to datetime and handle numeric columns
#     data['date'] = pd.to_datetime(data['date'], errors='coerce')
#     data = data.dropna(subset=['date'])
#     numeric_cols = ['age', 'height_cm', 'weight_kg', 'steps', 'calories', 'sleep_hours', 'water_intake_l', 'bmi']
#     for col in numeric_cols:
#         data[col] = pd.to_numeric(data[col], errors='coerce')
#     print(f"Starting with {len(data)} rows...")
#     data = data.dropna()
#     print(f"After cleaning, we have {len(data)} rows left.")
    
#     # Add a day index for time-based predictions
#     data['day_index'] = (data['date'] - data['date'].min()).dt.days
#     print("Here's a peek at the cleaned data:")
#     print(data[['user_id', 'date', 'day_index', 'steps']].head())
    
#     return data

# # Build and train a model to predict fitness metrics
# def build_and_train_model(data, target_metric):
#     """Trains a Linear Regression model for a specific metric (e.g., steps)."""
#     print(f"Training a model to predict {target_metric}...")
#     features = ['user_id', 'day_index', 'age', 'height_cm', 'weight_kg', 'bmi']
    
#     # Set up a pipeline to handle different types of data
#     preprocessor = ColumnTransformer(
#         transformers=[
#             ('user_id', OneHotEncoder(sparse_output=False, handle_unknown='ignore'), ['user_id']),
#             ('day_trend', PolynomialFeatures(degree=2, include_bias=False), ['day_index']),
#             ('numeric', 'passthrough', ['age', 'height_cm', 'weight_kg', 'bmi'])
#         ])
    
#     # Combine preprocessing and model
#     model = Pipeline([
#         ('preprocessor', preprocessor),
#         ('regressor', LinearRegression())
#     ])
    
#     # Train the model
#     X = data[features]
#     y = data[target_metric]
#     model.fit(X, y)
#     print(f"Model for {target_metric} is ready!")
    
#     return model

# # Predict future fitness metrics for a user
# def forecast_future(model, data, user_id, days_ahead=7):
#     """Predicts future values for a user based on their latest data."""
#     print(f"Making predictions for user {user_id}...")
#     try:
#         last_user_record = data[data['user_id'] == str(user_id)].sort_values('day_index').iloc[-1]
#         print(f"Found latest data for user {user_id} on day {last_user_record['day_index']}")
#     except IndexError:
#         print(f"No data found for user {user_id}. Check if this user exists in the dataset.")
#         raise ValueError(f"No data for user {user_id}")
    
#     last_day = last_user_record['day_index']
    
#     # Create future data points for the next 7 days
#     future_days = np.arange(last_day + 1, last_day + days_ahead + 1)
#     future_data = pd.DataFrame({
#         'user_id': [str(user_id)] * days_ahead,
#         'day_index': future_days,
#         'age': [last_user_record['age']] * days_ahead,
#         'height_cm': [last_user_record['height_cm']] * days_ahead,
#         'weight_kg': [last_user_record['weight_kg']] * days_ahead,
#         'bmi': [last_user_record['bmi']] * days_ahead
#     })
    
#     # Make predictions
#     predictions = model.predict(future_data)
#     print(f"Predicted {len(predictions)} days for user {user_id}")
#     return list(zip(future_days, predictions))

# # Main function to tie everything together
# def run_fitness_predictor(file_path, output_file='predictions.json'):
#     """Loads data, trains models, and predicts future fitness metrics."""
#     print("Starting the fitness predictor... Let's make some forecasts!")
    
#     # Load and clean the data
#     data = load_fitness_data(file_path)
    
#     # Metrics we want to predict
#     metrics = ['steps', 'calories', 'sleep_hours', 'water_intake_l']
    
#     # Train a model for each metric
#     models = {metric: build_and_train_model(data, metric) for metric in metrics}
    
#     # Store predictions for all users
#     predictions = {}
#     for user_id in data['user_id'].unique():
#         predictions[user_id] = {}
#         for metric in metrics:
#             try:
#                 future_forecasts = forecast_future(models[metric], data, user_id)
#                 predictions[user_id][metric] = [
#                     {'day': int(day), 'value': float(round(value, 2))} for day, value in future_forecasts
#                 ]
#                 print(f"Saved predictions for user {user_id}, {metric}")
#             except ValueError as e:
#                 print(f"Uh-oh! Issue with user {user_id}, {metric}: {e}")
#                 predictions[user_id][metric] = []
    
#     # Save predictions to a JSON file
#     with open(output_file, 'w') as f:
#         json.dump(predictions, f, indent=2)
#     print(f"All predictions saved to {output_file}")
    
#     # Show a sneak peek for User 1
#     print("\nHere's what we predict for User 1:")
#     print(json.dumps(predictions.get('1', {}), indent=2))
    
#     return predictions

# # Let's get started!
# csv_file_path = "D:\\fitness_logs_6users_15days.csv"

# if __name__ == "__main__":
#     print("Welcome to the Fitness Predictor!")
#     try:
#         predictions = run_fitness_predictor(csv_file_path)
#         print("All done! Your predictions are ready.")
#     except FileNotFoundError as e:
#         print(e)
#     except ValueError as e:
#         print(e)
#     except Exception as e:
#         print(f"Something went wrong: {e}. Let's figure it out!")



import tensorflow as tf
print("TensorFlow GPUs:", tf.config.list_physical_devices('GPU'))