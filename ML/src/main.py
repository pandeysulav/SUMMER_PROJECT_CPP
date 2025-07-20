import json
import os
import sys
import logging

# Add current directory to Python path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Import project modules
from config import *
from data_loader import load_fitness_data
from predictor import build_and_train_model, forecast_future
from fitness_assessor import assess_fitness

def setup_logging():
    """Configure logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler(sys.stdout)
        ]
    )
    return logging.getLogger()

def create_directories():
    """Create necessary output directories."""
    directories = [DATA_DIR, OUTPUT_DIR, VISUALIZATION_DIR]
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")

def check_dependencies():
    """Check if all required dependencies are installed."""
    try:
        import pandas
        import numpy
        import sklearn
        print("✓ All required packages found")
        return True
    except ImportError as e:
        print(f"✗ Missing dependency: {e}")
        print("Please install with: pip install pandas numpy scikit-learn")
        return False

def check_data_file():
    """Check if the CSV data file exists."""
    if not os.path.exists(CSV_FILE):
        print(f"✗ CSV file not found: {CSV_FILE}")
        print("Please ensure your CSV file is in the data/ directory")
        return False
    print(f"✓ Data file found: {CSV_FILE}")
    return True

def run_fitness_predictor():
    """Main function to orchestrate the entire workflow."""
    logger = setup_logging()
    logger.info("=" * 50)
    logger.info("Starting ML Fitness Predictor")
    logger.info("=" * 50)
    
    # Create necessary directories
    create_directories()
    
    # Check dependencies and data
    if not check_dependencies() or not check_data_file():
        logger.error("Prerequisites not met. Exiting.")
        return False
    
    try:
        # Load and clean data
        logger.info("Loading and cleaning data...")
        data = load_fitness_data(CSV_FILE)
        logger.info(f"Data loaded successfully: {len(data)} rows, {len(data['user_id'].unique())} users")
        
        # Train models for each metric
        logger.info("Training models...")
        models = {}
        for metric in METRICS_TO_PREDICT:
            try:
                models[metric] = build_and_train_model(data, metric)
                logger.info(f"✓ Model trained for {metric}")
            except Exception as e:
                logger.error(f"✗ Failed to train model for {metric}: {e}")
                return False
        
        # Generate predictions for all users
        logger.info("Generating predictions...")
        predictions = {}
        failed_users = []
        
        for user_id in data['user_id'].unique():
            predictions[user_id] = {}
            user_failed = False
            
            for metric in METRICS_TO_PREDICT:
                try:
                    future_forecasts = forecast_future(models[metric], data, user_id, FORECAST_DAYS)
                    predictions[user_id][metric] = [
                        {'day': int(day), 'value': float(round(value, 2))} 
                        for day, value in future_forecasts
                    ]
                except Exception as e:
                    logger.warning(f"Prediction failed for user {user_id}, {metric}: {e}")
                    predictions[user_id][metric] = []
                    user_failed = True
            
            if user_failed:
                failed_users.append(user_id)
            else:
                logger.info(f"✓ Predictions generated for user {user_id}")
        
        if failed_users:
            logger.warning(f"Predictions failed for users: {failed_users}")
        
        # Assess fitness levels
        logger.info("Assessing fitness levels...")
        assessments = assess_fitness(predictions)
        
        # Combine results
        output = {
            'metadata': {
                'total_users': len(data['user_id'].unique()),
                'prediction_days': FORECAST_DAYS,
                'metrics': METRICS_TO_PREDICT,
                'failed_users': failed_users
            },
            'predictions': predictions,
            'assessments': assessments
        }
        
        # Save results
        logger.info(f"Saving results to {PREDICTIONS_FILE}...")
        with open(PREDICTIONS_FILE, 'w') as f:
            json.dump(output, f, indent=2)
        
        # Log summary
        logger.info("=" * 50)
        logger.info("EXECUTION SUMMARY")
        logger.info("=" * 50)
        logger.info(f"✓ Data loaded: {len(data)} rows")
        logger.info(f"✓ Models trained: {len(models)}")
        logger.info(f"✓ Users processed: {len(predictions)}")
        logger.info(f"✓ Results saved to: {PREDICTIONS_FILE}")
        
        if failed_users:
            logger.warning(f"⚠ Failed users: {len(failed_users)}")
        
        # Sample output for first user
        first_user = list(predictions.keys())[0] if predictions else None
        if first_user:
            logger.info(f"\nSample results for User {first_user}:")
            logger.info(f"Fitness Level: {assessments[first_user]['fitness_level']}")
            logger.info(f"Fitness Score: {assessments[first_user]['fitness_score']}")
        
        logger.info("✓ ML Fitness Predictor completed successfully!")
        return True
        
    except Exception as e:
        logger.error(f"Execution failed: {e}")
        logger.exception("Full error traceback:")
        return False

if __name__ == "__main__":
    success = run_fitness_predictor()
    if not success:
        sys.exit(1)