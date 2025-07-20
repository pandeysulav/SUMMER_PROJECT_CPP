import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder, PolynomialFeatures
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn import __version__ as sklearn_version

def build_and_train_model(data, target_metric):
    """Trains a Linear Regression model for a specific metric (e.g., steps)."""
    print(f"Training a model to predict {target_metric}...")
    
    # Validate that target metric exists
    if target_metric not in data.columns:
        raise ValueError(f"Target metric '{target_metric}' not found in data columns: {data.columns.tolist()}")
    
    features = ['user_id', 'day_index', 'age', 'height_cm', 'weight_kg', 'bmi']
    
    # Check if all features exist
    missing_features = [f for f in features if f not in data.columns]
    if missing_features:
        raise ValueError(f"Missing features in data: {missing_features}")
    
    # Handle scikit-learn version compatibility
    sklearn_major_version = int(sklearn_version.split('.')[0])
    sklearn_minor_version = int(sklearn_version.split('.')[1])
    
    # For scikit-learn >= 1.2, use sparse_output=False, for older versions use sparse=False
    if sklearn_major_version > 1 or (sklearn_major_version == 1 and sklearn_minor_version >= 2):
        onehot_params = {'sparse_output': False, 'handle_unknown': 'ignore'}
    else:
        onehot_params = {'sparse': False, 'handle_unknown': 'ignore'}
    
    # Set up a pipeline to handle different types of data
    preprocessor = ColumnTransformer(
        transformers=[
            ('user_id', OneHotEncoder(**onehot_params), ['user_id']),
            ('day_trend', PolynomialFeatures(degree=2, include_bias=False), ['day_index']),
            ('numeric', 'passthrough', ['age', 'height_cm', 'weight_kg', 'bmi'])
        ])
    
    # Combine preprocessing and model
    model = Pipeline([
        ('preprocessor', preprocessor),
        ('regressor', LinearRegression())
    ])
    
    # Prepare training data
    X = data[features].copy()
    y = data[target_metric].copy()
    
    # Remove any rows with NaN values
    mask = ~(X.isnull().any(axis=1) | y.isnull())
    X = X[mask]
    y = y[mask]
    
    if len(X) == 0:
        raise ValueError(f"No valid data available for training {target_metric} model")
    
    # Train the model
    model.fit(X, y)
    print(f"Model for {target_metric} trained on {len(X)} samples!")
    
    return model

def forecast_future(model, data, user_id, days_ahead=14):
    """Predicts future values for a user based on their latest data."""
    print(f"Making predictions for user {user_id}...")
    
    # Ensure user_id is string for consistency
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
    
    # Create future data points for the next days_ahead days
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
        # Make predictions
        predictions = model.predict(future_data)
        
        # Ensure predictions are non-negative for metrics that shouldn't be negative
        predictions = np.maximum(predictions, 0)
        
        print(f"Predicted {len(predictions)} days for user {user_id}")
        return list(zip(future_days, predictions))
    
    except Exception as e:
        print(f"Error making predictions for user {user_id}: {e}")
        raise ValueError(f"Prediction failed for user {user_id}: {e}")