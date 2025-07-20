import json
import os
import sys
import logging
from data_loader import load_fitness_data
from predictor import build_and_train_model, forecast_future
from fitness_assessor import assess_fitness

# Configure logging for better debugging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('fitness_predictor.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger()

def check_setup(file_path):
    """Verify that all required files and dependencies are present."""
    logger.info("Checking project setup...")
    
    # Check for CSV file
    if not os.path.exists(file_path):
        logger.error(f"CSV file not found: {file_path}")
        raise FileNotFoundError(f"CSV file not found: {file_path}")
    
    # Check for required scripts
    required_scripts = ['data_loader.py', 'predictor.py', 'fitness_assessor.py']
    for script in required_scripts:
        if not os.path.exists(script):
            logger.error(f"Required script not found: {script}")
            raise FileNotFoundError(f"Required script not found: {script}")
    
    # Check for dependencies
    try:
        import pandas
        import numpy
        import sklearn
    except ImportError as e:
        logger.error(f"Missing dependency: {e}")
        raise ImportError(f"Missing dependency: {e}. Install with 'pip install pandas numpy scikit-learn'")
    
    logger.info("Setup check passed!")

def run_fitness_predictor(file_path, output_file='fitness_predictions.json'):
    """Main function to load data, predict metrics, assess fitness, and save results."""
    logger.info("Starting Fitness Predictor...")
    
    # Verify setup
    try:
        check_setup(file_path)
    except (FileNotFoundError, ImportError) as e:
        logger.error(f"Setup failed: {e}")
        return {}
    
    # Load data
    logger.info("Loading and cleaning data...")
    try:
        data = load_fitness_data(file_path)
    except (FileNotFoundError, ValueError) as e:
        logger.error(f"Data loading failed: {e}")
        return {}
    
    # Metrics to predict
    metrics = ['steps', 'calories', 'sleep_hours', 'water_intake_l']
    
    # Train models
    logger.info("Training models...")
    models = {}
    for metric in metrics:
        try:
            models[metric] = build_and_train_model(data, metric)
        except Exception as e:
            logger.error(f"Failed to train model for {metric}: {e}")
            return {}
    
    # Generate predictions
    logger.info("Generating predictions...")
    predictions = {}
    for user_id in data['user_id'].unique():
        predictions[user_id] = {}
        for metric in metrics:
            try:
                future_forecasts = forecast_future(models[metric], data, user_id)
                predictions[user_id][metric] = [
                    {'day': int(day), 'value': float(round(value, 2))} for day, value in future_forecasts
                ]
                logger.info(f"Saved predictions for user {user_id}, {metric}")
            except ValueError as e:
                logger.error(f"Prediction error for user {user_id}, {metric}: {e}")
                predictions[user_id][metric] = []
    
    # Assess fitness
    logger.info("Assessing fitness levels...")
    try:
        assessments = assess_fitness(predictions)
    except Exception as e:
        logger.error(f"Fitness assessment failed: {e}")
        return {}
    
    # Combine predictions and assessments
    output = {
        'predictions': predictions,
        'assessments': assessments
    }
    
    # Save to JSON
    logger.info(f"Saving results to {output_file}...")
    try:
        with open(output_file, 'w') as f:
            json.dump(output, f, indent=2)
        logger.info(f"Results saved to {output_file}")
    except Exception as e:
        logger.error(f"Failed to save results: {e}")
        return {}
    
    # Preview for User 1
    logger.info("Sample results for User 1:")
    logger.info(json.dumps(output['predictions'].get('1', {}), indent=2))
    logger.info("Fitness Assessment for User 1:")
    logger.info(json.dumps(output['assessments'].get('1', {}), indent=2))
    
    return output

if __name__ == "__main__":
    csv_file_path = "E:\\SUMMER_PROJECT_CPP\\ML\\fitness_logs_15users_15days.csv"
    try:
        run_fitness_predictor(csv_file_path)
        logger.info("Fitness predictions and assessments complete!")
    except Exception as e:
        logger.error(f"Process failed: {e}")