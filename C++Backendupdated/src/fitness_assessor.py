def assess_fitness(predictions):
    """Evaluates fitness level and provides recommendations based on predictions."""
    print("Assessing fitness levels...")
    assessments = {}
    
    if not predictions:
        print("✗ No predictions provided for assessment")
        return assessments
    
    for user_id, metrics in predictions.items():
        print(f"Assessing user {user_id}...")
        
        # Calculate average predicted values with safe division
        steps_list = metrics.get('steps', [])
        calories_list = metrics.get('calories', [])
        sleep_list = metrics.get('sleep_hours', [])
        water_list = metrics.get('water_intake_l', [])
        
        # Calculate averages safely
        steps_avg = sum(p['value'] for p in steps_list) / len(steps_list) if steps_list else 0
        calories_avg = sum(p['value'] for p in calories_list) / len(calories_list) if calories_list else 0
        sleep_avg = sum(p['value'] for p in sleep_list) / len(sleep_list) if sleep_list else 0
        water_avg = sum(p['value'] for p in water_list) / len(water_list) if water_list else 0
        
        # Normalize metrics to 0-100 scale with safe division
        def safe_normalize(value, min_val, max_val):
            if max_val == min_val:
                return 50  # Default score if range is 0
            return min(max((value - min_val) / (max_val - min_val) * 100, 0), 100)
        
        steps_score = safe_normalize(steps_avg, 3000, 12000) if steps_avg > 0 else 0
        calories_score = safe_normalize(calories_avg, 1900, 2900) if calories_avg > 0 else 0
        sleep_score = safe_normalize(sleep_avg, 6, 8.5) if sleep_avg > 0 else 0
        water_score = safe_normalize(water_avg, 2, 3.5) if water_avg > 0 else 0
        
        # Calculate overall fitness score
        scores = [s for s in [steps_score, calories_score, sleep_score, water_score] if s > 0]
        fitness_score = sum(scores) / len(scores) if scores else 0
        
        # Determine fitness level
        if fitness_score < 50:
            fitness_level = "Needs Improvement"
        elif fitness_score < 75:
            fitness_level = "Moderate"
        else:
            fitness_level = "Fit"
        
        # Generate specific recommendations
        recommendations = []
        
        if steps_avg < 7000:
            recommendations.append(f"Increase daily steps by walking or light exercise. Current average: {steps_avg:.0f} steps/day, target: 7000+")
        
        if calories_avg < 2000:
            recommendations.append(f"Ensure adequate calorie intake for energy needs. Current average: {calories_avg:.0f} calories/day")
        elif calories_avg > 2900:
            recommendations.append(f"Monitor calorie intake to avoid excess. Current average: {calories_avg:.0f} calories/day")
        
        if sleep_avg < 6.5:
            recommendations.append(f"Aim for 7-8 hours of sleep per night. Current average: {sleep_avg:.1f} hours/night")
        elif sleep_avg > 8.5:
            recommendations.append(f"Avoid oversleeping; maintain a consistent schedule. Current average: {sleep_avg:.1f} hours/night")
        
        if water_avg < 2.5:
            recommendations.append(f"Drink more water, aiming for 2.5-3.5 liters daily. Current average: {water_avg:.1f}L/day")
        
        if not recommendations:
            recommendations.append("Great job! Maintain your current fitness routine!")
        
        assessments[user_id] = {
            'fitness_score': round(fitness_score, 2),
            'fitness_level': fitness_level,
            'average_metrics': {
                'steps': round(steps_avg, 2),
                'calories': round(calories_avg, 2),
                'sleep_hours': round(sleep_avg, 2),
                'water_intake_l': round(water_avg, 2)
            },
            'component_scores': {
                'steps_score': round(steps_score, 2),
                'calories_score': round(calories_score, 2),
                'sleep_score': round(sleep_score, 2),
                'water_score': round(water_score, 2)
            },
            'recommendations': recommendations
        }
        
        print(f"✓ User {user_id}: {fitness_level} (Score: {fitness_score:.1f})")
    
    print(f"✓ Fitness assessment completed for {len(assessments)} users")
    return assessments