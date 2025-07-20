def assess_fitness(predictions):
    """Evaluates fitness level and provides recommendations based on predictions."""
    print("Assessing fitness levels...")
    assessments = {}
    
    for user_id, metrics in predictions.items():
        # Calculate average predicted values
        steps_avg = sum(p['value'] for p in metrics.get('steps', [])) / len(metrics.get('steps', [])) if metrics.get('steps') else 0
        calories_avg = sum(p['value'] for p in metrics.get('calories', [])) / len(metrics.get('calories', [])) if metrics.get('calories') else 0
        sleep_avg = sum(p['value'] for p in metrics.get('sleep_hours', [])) / len(metrics.get('sleep_hours', [])) if metrics.get('sleep_hours') else 0
        water_avg = sum(p['value'] for p in metrics.get('water_intake_l', [])) / len(metrics.get('water_intake_l', [])) if metrics.get('water_intake_l') else 0
        
        # Normalize metrics to 0-100 scale
        steps_score = min(max((steps_avg - 3000) / (12000 - 3000) * 100, 0), 100)
        calories_score = min(max((calories_avg - 1900) / (2900 - 1900) * 100, 0), 100)
        sleep_score = min(max((sleep_avg - 6) / (8.5 - 6) * 100, 0), 100)
        water_score = min(max((water_avg - 2) / (3.5 - 2) * 100, 0), 100)
        
        # Calculate overall fitness score
        fitness_score = (steps_score + calories_score + sleep_score + water_score) / 4
        
        # Determine fitness level
        if fitness_score < 50:
            fitness_level = "Needs Improvement"
        elif fitness_score < 75:
            fitness_level = "Moderate"
        else:
            fitness_level = "Fit"
        
        # Generate recommendations
        recommendations = []
        if steps_avg < 7000:
            recommendations.append("Increase daily steps by walking or light exercise.")
        if calories_avg < 2000:
            recommendations.append("Ensure adequate calorie intake for energy needs.")
        elif calories_avg > 2900:
            recommendations.append("Monitor calorie intake to avoid excess.")
        if sleep_avg < 6.5:
            recommendations.append("Aim for 7-8 hours of sleep per night.")
        elif sleep_avg > 8.5:
            recommendations.append("Avoid oversleeping; maintain a consistent schedule.")
        if water_avg < 2.5:
            recommendations.append("Drink more water, aiming for 2.5-3.5 liters daily.")
        
        assessments[user_id] = {
            'fitness_score': round(fitness_score, 2),
            'fitness_level': fitness_level,
            'recommendations': recommendations or ["Maintain your current fitness routine!"]
        }
        print(f"Assessed fitness for user {user_id}: {fitness_level}")
    
    return assessments