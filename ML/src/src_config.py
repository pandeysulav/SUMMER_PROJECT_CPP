# Configuration settings for the Fitness Predictor project

# File paths
CSV_FILE_PATH = "E:\\SUMMER_PROJECT_CPP\\ML\\fitness_logs_15users_15days.csv"
OUTPUT_JSON_PATH = "E:\\SUMMER_PROJECT_CPP\\ML\\fitness_predictions.json"
LOG_FILE_PATH = "E:\\SUMMER_PROJECT_CPP\\ML\\fitness_predictor.log"

# Metrics to predict
METRICS = ['steps', 'calories', 'sleep_hours', 'water_intake_l']

# Number of days to predict
DAYS_AHEAD = 14