import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder, PolynomialFeatures
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def build_and_train_model(data, target_metric):
    """Trains a Linear Regression model for a specific metric (e.g., steps)."""
    print(f"Training a model to predict {target_metric}...")
    features = ['user_id', 'day_index', 'age', 'height_cm', 'weight_kg', 'bmi']
    
    # Set up a pipeline to handle different types of data
    preprocessor = ColumnTransformer(
        transformers=[
            ('user_id', OneHotEncoder(sparse_output=False, handle_unknown='ignore'), ['user_id']),
            ('day_trend', PolynomialFeatures(degree=2, include_bias=False), ['day_index']),
            ('numeric', 'passthrough', ['age', 'height_cm', 'weight_kg', 'bmi'])
        ])
    
    # Combine preprocessing and model
    model = Pipeline([
        ('preprocessor', preprocessor),
        ('regressor', LinearRegression())
    ])
    
    # Train the model
    X = data[features]
    y = data[target_metric]
    model.fit(X, y)
    print(f"Model for {target_metric} is ready!")
    
    return model

def forecast_future(model, data, user_id, days_ahead=14):
    """Predicts future values for a user based on their latest data."""
    print(f"Making predictions for user {user_id}...")
    try:
        last_user_record = data[data['user_id'] == str(user_id)].sort_values('day_index').iloc[-1]
        print(f"Found latest data for user {user_id} on day {last_user_record['day_index']}")
    except IndexError:
        print(f"No data found for user {user_id}. Check if this user exists in the dataset.")
        raise ValueError(f"No data for user {user_id}")
    
    last_day = last_user_record['day_index']
    
    # Create future data points for the next 14 days
    future_days = np.arange(last_day + 1, last_day + days_ahead + 1)
    future_data = pd.DataFrame({
        'user_id': [str(user_id)] * days_ahead,
        'day_index': future_days,
        'age': [last_user_record['age']] * days_ahead,
        'height_cm': [last_user_record['height_cm']] * days_ahead,
        'weight_kg': [last_user_record['weight_kg']] * days_ahead,
        'bmi': [last_user_record['bmi']] * days_ahead
    })
    
    # Make predictions
    predictions = model.predict(future_data)
    print(f"Predicted {len(predictions)} days for user {user_id}")
    return list(zip(future_days, predictions))