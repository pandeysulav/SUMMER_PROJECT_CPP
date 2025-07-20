import pandas as pd
import os

def load_fitness_data(file_path):
    """Reads the CSV file and prepares it for analysis."""
    print("Loading fitness data...")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    data = pd.read_csv(file_path)
    
    # Check expected columns
    expected_columns = ['user_id', 'date', 'age', 'gender', 'height_cm', 'weight_kg', 'steps', 'calories', 'sleep_hours', 'water_intake_l', 'bmi']
    missing = [col for col in expected_columns if col not in data.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    
    # Clean user_id
    data['user_id'] = data['user_id'].astype(str).str.replace(r'\.0$', '', regex=True)
    data = data[data['user_id'] != 'nan']
    print(f"Found user IDs: {data['user_id'].unique().tolist()}")
    
    # Convert date and numeric columns
    data['date'] = pd.to_datetime(data['date'], errors='coerce')
    data = data.dropna(subset=['date'])
    numeric_cols = ['age', 'height_cm', 'weight_kg', 'steps', 'calories', 'sleep_hours', 'water_intake_l', 'bmi']
    for col in numeric_cols:
        data[col] = pd.to_numeric(data[col], errors='coerce')
    print(f"Starting with {len(data)} rows, after cleaning: {len(data.dropna())} rows")
    data = data.dropna()
    
    # Add day_index
    data['day_index'] = (data['date'] - data['date'].min()).dt.days
    print("Data sample:")
    print(data[['user_id', 'date', 'day_index', 'steps']].head())
    
    return data