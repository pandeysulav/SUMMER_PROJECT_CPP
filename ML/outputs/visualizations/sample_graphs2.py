import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set Seaborn style for presentation-ready visuals
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=1.1)
plt.rcParams['font.family'] = 'Arial'

# Load JSON data
input_json_path = r"E:\SUMMER_PROJECT_CPP\ML\outputs\fitness_predictions.json"
try:
    with open(input_json_path, 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print(f"Error: File {input_json_path} not found.")
    exit(1)
except json.JSONDecodeError:
    print(f"Error: File {input_json_path} is not a valid JSON.")
    exit(1)

# Extract data for Users 1 (Good) and 4 (Excellent)
users = ['1', '4']
metrics = ['steps', 'calories', 'sleep_hours', 'water_intake_l']
days = list(range(15, 29))  # Days 15 to 28
user_data = {user: {metric: [] for metric in metrics} for user in users}

for user in users:
    for metric in metrics:
        user_data[user][metric] = [entry['value'] for entry in data['predictions'][user][metric]]

# Normalization scales
max_values = {'steps': 20000, 'calories': 4000, 'sleep_hours': 8, 'water_intake_l': 3.5}

# Create DataFrames with normalized values
df_user1 = pd.DataFrame({
    'Day': days,
    'Steps': [val / max_values['steps'] * 100 for val in user_data['1']['steps']],
    'Calories': [val / max_values['calories'] * 100 for val in user_data['1']['calories']],
    'Sleep Hours': [val / max_values['sleep_hours'] * 100 for val in user_data['1']['sleep_hours']],
    'Water Intake (L)': [val / max_values['water_intake_l'] * 100 for val in user_data['1']['water_intake_l']]
})

df_user4 = pd.DataFrame({
    'Day': days,
    'Steps': [val / max_values['steps'] * 100 for val in user_data['4']['steps']],
    'Calories': [val / max_values['calories'] * 100 for val in user_data['4']['calories']],
    'Sleep Hours': [val / max_values['sleep_hours'] * 100 for val in user_data['4']['sleep_hours']],
    'Water Intake (L)': [val / max_values['water_intake_l'] * 100 for val in user_data['4']['water_intake_l']]
})

# Define output paths
output_path_user1 = r"E:\SUMMER_PROJECT_CPP\ML\outputs\user1_good_area_plot.png"
output_path_user4 = r"E:\SUMMER_PROJECT_CPP\ML\outputs\user4_excellent_area_plot.png"

# Target ranges (normalized to 0–100 scale)
target_ranges = {
    'Steps': (10000 / max_values['steps'] * 100, 15000 / max_values['steps'] * 100),  # 10,000–15,000 steps
    'Calories': (2000 / max_values['calories'] * 100, 3000 / max_values['calories'] * 100),  # 2,000–3,000 calories
    'Sleep Hours': (7 / max_values['sleep_hours'] * 100, 8 / max_values['sleep_hours'] * 100),  # 7–8 hours
    'Water Intake (L)': (2.5 / max_values['water_intake_l'] * 100, 3.5 / max_values['water_intake_l'] * 100)  # 2.5–3.5L
}

# Plot for User 1 (Good)
plt.figure(figsize=(12, 8))
colors = sns.color_palette("Greens", n_colors=4)
plt.stackplot(df_user1['Day'], 
              df_user1['Steps'], df_user1['Calories'], df_user1['Sleep Hours'], df_user1['Water Intake (L)'],
              labels=['Steps', 'Calories', 'Sleep Hours', 'Water Intake (L)'], 
              colors=colors, alpha=0.8)

# Add target range line for steps
plt.axhspan(target_ranges['Steps'][0], target_ranges['Steps'][1], facecolor='lightgreen', alpha=0.2, label='Target Steps Range')

# Annotations
plt.annotate(f'Fitness Score: {data["assessments"]["1"]["fitness_score"]:.2f} (Moderate)',
            xy=(0.05, 0.95), xycoords='axes fraction', fontsize=12, weight='bold', color='darkgreen',
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='darkgreen'))
plt.annotate(f'Avg Steps: {data["assessments"]["1"]["average_metrics"]["steps"]:.0f}',
            xy=(0.05, 0.85), xycoords='axes fraction', fontsize=10, color='darkgreen')

plt.title('User 1: Good Fitness Performance', fontsize=18, weight='bold', pad=20)
plt.xlabel('Day', fontsize=14)
plt.ylabel('Normalized Metrics (%)', fontsize=14)
plt.xticks(days, rotation=45)
plt.legend(loc='upper right', fontsize=10, bbox_to_anchor=(1.15, 1))
plt.tight_layout()
plt.savefig(output_path_user1, dpi=300, bbox_inches='tight')
plt.close()

# Plot for User 4 (Excellent)
plt.figure(figsize=(12, 8))
colors = sns.color_palette("Blues", n_colors=4)
plt.stackplot(df_user4['Day'], 
              df_user4['Steps'], df_user4['Calories'], df_user4['Sleep Hours'], df_user4['Water Intake (L)'],
              labels=['Steps', 'Calories', 'Sleep Hours', 'Water Intake (L)'], 
              colors=colors, alpha=0.8)

# Add target range line for steps
plt.axhspan(target_ranges['Steps'][0], target_ranges['Steps'][1], facecolor='lightblue', alpha=0.2, label='Target Steps Range')

# Annotations
plt.annotate(f'Fitness Score: {data["assessments"]["4"]["fitness_score"]:.2f} (Moderate)',
            xy=(0.05, 0.95), xycoords='axes fraction', fontsize=12, weight='bold', color='darkblue',
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='darkblue'))
plt.annotate(f'Avg Steps: {data["assessments"]["4"]["average_metrics"]["steps"]:.0f}',
            xy=(0.05, 0.85), xycoords='axes fraction', fontsize=10, color='darkblue')

plt.title('User 4: Excellent Fitness Performance', fontsize=18, weight='bold', pad=20)
plt.xlabel('Day', fontsize=14)
plt.ylabel('Normalized Metrics (%)', fontsize=14)
plt.xticks(days, rotation=45)
plt.legend(loc='upper right', fontsize=10, bbox_to_anchor=(1.15, 1))
plt.tight_layout()
plt.savefig(output_path_user4, dpi=300, bbox_inches='tight')
plt.close()

print(f"Graphs generated successfully at: {output_path_user1} and {output_path_user4}")