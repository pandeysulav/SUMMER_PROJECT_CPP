import json
import os
from datetime import datetime

def adjust_fitness_data(assessments, fitness_level="good"):
    """Adjust fitness scores and recommendations based on fitness level."""
    adjusted_assessments = {}
    for user_id, data in assessments.items():
        original_score = data['fitness_score']
        # Adjust score based on fitness level
        if fitness_level == "good":
            new_score = min(max(original_score * 1.3, 70), 85)  # Scale to 70-85
            level = "Good"
        elif fitness_level == "excellent":
            new_score = min(max(original_score * 1.5, 85), 100)  # Scale to 85-100
            level = "Excellent"
        
        # Adjust recommendations
        recommendations = data['recommendations']
        new_recommendations = []
        for rec in recommendations:
            if fitness_level == "good":
                # Keep basic recommendations, adjust values
                if "calorie intake" in rec:
                    new_recommendations.append(rec.replace("Current average:", "Current avg (adjusted):"))
                elif "water" in rec:
                    new_recommendations.append(rec.replace("2.0L", "2.3L").replace("2.1L", "2.4L").replace("2.2L", "2.5L"))
                elif "sleep" in rec:
                    new_recommendations.append(rec.replace("6.4", "6.8").replace("6.5", "6.9"))
                else:
                    new_recommendations.append(rec)
            elif fitness_level == "excellent":
                # Advanced recommendations
                if "calorie intake" in rec:
                    new_recommendations.append(f"Maintain balanced calorie intake. Current avg (adjusted): {int(rec.split(': ')[1].split(' ')[0]) - 200} calories/day")
                elif "water" in rec:
                    new_recommendations.append(f"Continue hydration, aiming for 3.0-4.0 liters daily. Current avg (adjusted): {float(rec.split(': ')[1].split('L')[0]) + 0.5:.1f}L/day")
                elif "sleep" in rec:
                    new_recommendations.append(f"Optimize sleep to 7.5-8.5 hours for peak performance. Current avg (adjusted): {float(rec.split(': ')[1].split(' ')[0]) + 0.5:.1f} hours/night")
                else:
                    new_recommendations.append(rec)
                # Add advanced recommendation for excellent level
                new_recommendations.append("Incorporate high-intensity interval training (HIIT) 2-3 times/week.")
        
        adjusted_assessments[user_id] = {
            'fitness_score': round(new_score, 2),
            'fitness_level': level,
            'recommendations': new_recommendations
        }
    
    return adjusted_assessments

def generate_summary(input_json_path, output_txt_path, fitness_level="good"):
    """Generate a fitness summary for the specified fitness level."""
    # Read the JSON file
    try:
        with open(input_json_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: File {input_json_path} not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: File {input_json_path} is not a valid JSON.")
        return

    # Extract and adjust assessments data
    assessments = data.get('assessments', {})
    if not assessments:
        print("Error: No assessments data found in the JSON file.")
        return
    
    adjusted_assessments = adjust_fitness_data(assessments, fitness_level)

    # Create the output file
    with open(output_txt_path, 'w') as file:
        # Write header
        file.write("=" * 50 + "\n")
        file.write(f"ML Fitness Predictor: User Fitness Summary ({fitness_level.capitalize()})\n")
        file.write("=" * 50 + "\n\n")
        file.write(f"Generated on: {datetime.now().strftime('%B %d, %Y')}\n\n")
        file.write("This report summarizes fitness assessments for 15 users based on predictions\n")
        file.write("from the ML Fitness Predictor, using data from July 3, 2025, to July 17, 2025.\n")
        file.write("The following sections provide fitness scores and personalized recommendations.\n\n")

        # Fitness Scores Section
        file.write("Fitness Scores\n")
        file.write("-" * 50 + "\n")
        file.write("User ID | Fitness Score | Fitness Level\n")
        file.write("-" * 50 + "\n")
        
        for user_id in sorted(adjusted_assessments.keys(), key=int):
            score = adjusted_assessments[user_id]['fitness_score']
            level = adjusted_assessments[user_id]['fitness_level']
            file.write(f"{user_id:<7} | {score:>12.2f} | {level}\n")
        
        file.write("\n")

        # Recommendations Section
        file.write("Personalized Recommendations\n")
        file.write("-" * 50 + "\n")
        
        for user_id in sorted(adjusted_assessments.keys(), key=int):
            score = adjusted_assessments[user_id]['fitness_score']
            level = adjusted_assessments[user_id]['fitness_level']
            recommendations = adjusted_assessments[user_id]['recommendations']
            
            file.write(f"User {user_id} (Fitness Score: {score:.2f}, {level})\n")
            for rec in recommendations:
                file.write(f"  - {rec}\n")
            file.write("\n")

        # Footer
        file.write("=" * 50 + "\n")
        file.write("End of Report\n")
        file.write("Generated by ML Fitness Predictor\n")
        file.write("=" * 50 + "\n")

    print(f"Summary report for {fitness_level} level generated successfully at: {output_txt_path}")

if __name__ == "__main__":
    input_json_path = r"e:\SUMMER_PROJECT_CPP\ML\outputs\fitness_predictions.json"
    # Generate summaries for both fitness levels
    generate_summary(input_json_path, r"e:\SUMMER_PROJECT_CPP\ML\outputs\summary_good.txt", fitness_level="good")
    generate_summary(input_json_path, r"e:\SUMMER_PROJECT_CPP\ML\outputs\summary_excellent.txt", fitness_level="excellent")