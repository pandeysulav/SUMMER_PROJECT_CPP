"""
Configuration settings for the ML Fitness Predictor
"""

import os

# -------------------------------
# Base directories
# -------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Root project folder
DATA_DIR = os.path.join(BASE_DIR, 'data')
OUTPUT_DIR = os.path.join(BASE_DIR, 'outputs')
VISUALIZATION_DIR = os.path.join(OUTPUT_DIR, 'visualizations')

# -------------------------------
# File paths
# -------------------------------
CSV_FILE = os.path.join(DATA_DIR, 'fitness_logs_15users_15days.csv')
PREDICTIONS_FILE = os.path.join(OUTPUT_DIR, 'fitness_predictions.json')
LOG_FILE = os.path.join(BASE_DIR, 'fitness_predictor.log')

# -------------------------------
# Model settings
# -------------------------------
METRICS_TO_PREDICT = ['steps', 'calories', 'sleep_hours', 'water_intake_l']
FORECAST_DAYS = 14

# -------------------------------
# Dataset schema
# -------------------------------
REQUIRED_COLUMNS = [
    'user_id', 'date', 'age', 'gender', 'height_cm', 'weight_kg', 
    'steps', 'calories', 'sleep_hours', 'water_intake_l', 'bmi'
]

NUMERIC_COLUMNS = [
    'age', 'height_cm', 'weight_kg', 'steps', 'calories', 
    'sleep_hours', 'water_intake_l', 'bmi'
]

FEATURE_COLUMNS = ['user_id', 'day_index', 'age', 'height_cm', 'weight_kg', 'bmi']

# -------------------------------
# Fitness thresholds & levels
# -------------------------------
FITNESS_THRESHOLDS = {
    'steps': {'min': 3000, 'max': 12000, 'target': 7000},
    'calories': {'min': 1900, 'max': 2900, 'target_min': 2000, 'target_max': 2900},
    'sleep_hours': {'min': 6, 'max': 8.5, 'target_min': 6.5, 'target_max': 8.5},
    'water_intake_l': {'min': 2, 'max': 3.5, 'target': 2.5}
}

FITNESS_LEVELS = {
    'needs_improvement': (0, 50),
    'moderate': (50, 75),
    'fit': (75, 100)
}
