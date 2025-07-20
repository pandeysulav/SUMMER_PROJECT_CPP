import pandas as pd
import numpy as np
import os

def load_fitness_data(file_path):
    """Loads and cleans the fitness data from a CSV file."""
    print(f"Loading fitness data from {file_path}...")
    
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Load CSV with explicit UTF-8 encoding
    try:
        data = pd.read_csv(file_path, encoding='utf-8')
        print(f"✓ CSV loaded successfully with {len(data)} rows")
    except Exception as e:
        print(f"✗ Error reading CSV: {e}")
        raise ValueError(f"Failed to read CSV: {e}")
    
    # Validate required columns
    required_columns = ['user_id', 'date', 'age', 'gender', 'height_cm', 'weight_kg', 
                       'steps', 'calories', 'sleep_hours', 'water_intake_l', 'bmi']
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        print(f"✗ Missing columns: {missing_columns}")
        print(f"Available columns: {data.columns.tolist()}")
        raise ValueError(f"CSV missing required columns: {missing_columns}")
    
    print("✓ All required columns found")
    
    # Clean data
    initial_rows = len(data)
    
    # Clean user_id
    data['user_id'] = data['user_id'].astype(str)
    data = data[data['user_id'] != 'nan']
    data = data[data['user_id'] != '']
    
    # Clean dates
    data['date'] = pd.to_datetime(data['date'], errors='coerce')
    data = data.dropna(subset=['date'])
    
    # Convert numeric columns
    numeric_columns = ['age', 'height_cm', 'weight_kg', 'steps', 'calories', 
                       'sleep_hours', 'water_intake_l', 'bmi']
    
    for col in numeric_columns:
        data[col] = pd.to_numeric(data[col], errors='coerce')
    
    # Remove rows with any NaN values in numeric columns
    data = data.dropna(subset=numeric_columns)
    
    # Remove obviously invalid data
    data = data[data['age'] > 0]
    data = data[data['height_cm'] > 0]
    data = data[data['weight_kg'] > 0]
    data = data[data['steps'] >= 0]
    data = data[data['calories'] >= 0]
    data = data[data['sleep_hours'] >= 0]
    data = data[data['water_intake_l'] >= 0]
    
    # Add day_index for time-based predictions
    data = data.sort_values(['user_id', 'date'])
    data['day_index'] = (data['date'] - data['date'].min()).dt.days
    
    final_rows = len(data)
    print(f"✓ Data cleaned: {initial_rows} → {final_rows} rows ({initial_rows - final_rows} removed)")
    
    # Validate we have data
    if final_rows == 0:
        raise ValueError("No valid data remaining after cleaning")
    
    unique_users = data['user_id'].unique()
    print(f"✓ Found {len(unique_users)} unique users: {unique_users.tolist()}")
    print(f"✓ Date range: {data['date'].min()} to {data['date'].max()}")
    print(f"✓ Day index range: {data['day_index'].min()} to {data['day_index'].max()}")
    
    # Show sample data
    print("\nSample data:")
    print(data.head(3))
    
    return data