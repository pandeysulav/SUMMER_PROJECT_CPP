import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set Seaborn style for clear, presentation-ready visuals
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

# Extract data for Users 1 and 2
users = ['1', '2']
metrics = ['steps', 'calories', 'sleep_hours', 'water_intake_l']
days = list(range(15, 29))  # Days 15 to 28
user_data = {user: {metric: [] for metric in metrics} for user in users}

for user in users:
    for metric in metrics:
        user_data[user][metric] = [entry['value'] for entry in data['predictions'][user][metric]]

# Normalization scales
max_values = {'steps': 20000, 'calories': 4000, 'sleep_hours': 8, 'water_intake_l': 3.5}

# Ideal values (midpoint of target ranges for comparison)
ideal_values = {
    'steps': (10000 + 15000) / 2 / max_values['steps'] * 100,  # 12,500 steps
    'calories': (2000 + 3000) / 2 / max_values['calories'] * 100,  # 2,500 calories
    'sleep_hours': (7 + 8) / 2 / max_values['sleep_hours'] * 100,  # 7.5 hours
    'water_intake_l': (2.5 + 3.5) / 2 / max_values['water_intake_l'] * 100  # 3L
}

# Create DataFrames with normalized values
df_user1 = pd.DataFrame({
    'Day': days,
    'Steps': [val / max_values['steps'] * 100 for val in user_data['1']['steps']],
    'Calories': [val / max_values['calories'] * 100 for val in user_data['1']['calories']],
    'Sleep Hours': [val / max_values['sleep_hours'] * 100 for val in user_data['1']['sleep_hours']],
    'Water Intake (L)': [val / max_values['water_intake_l'] * 100 for val in user_data['1']['water_intake_l']]
})

df_user2 = pd.DataFrame({
    'Day': days,
    'Steps': [val / max_values['steps'] * 100 for val in user_data['2']['steps']],
    'Calories': [val / max_values['calories'] * 100 for val in user_data['2']['calories']],
    'Sleep Hours': [val / max_values['sleep_hours'] * 100 for val in user_data['2']['sleep_hours']],
    'Water Intake (L)': [val / max_values['water_intake_l'] * 100 for val in user_data['2']['water_intake_l']]
})

# Define output paths
output_path_user1 = r"E:\SUMMER_PROJECT_CPP\ML\outputs\user1_fitness_comparison.png"
output_path_user2 = r"E:\SUMMER_PROJECT_CPP\ML\outputs\user2_fitness_comparison.png"

# Target ranges (normalized to 0–100 scale)
target_ranges = {
    'Steps': (10000 / max_values['steps'] * 100, 15000 / max_values['steps'] * 100),  # 10,000–15,000 steps
    'Calories': (2000 / max_values['calories'] * 100, 3000 / max_values['calories'] * 100),  # 2,000–3,000 calories
    'Sleep Hours': (7 / max_values['sleep_hours'] * 100, 8 / max_values['sleep_hours'] * 100),  # 7–8 hours
    'Water Intake (L)': (2.5 / max_values['water_intake_l'] * 100, 3.5 / max_values['water_intake_l'] * 100)  # 2.5–3.5L
}

# Plot for User 1
fig, axes = plt.subplots(2, 2, figsize=(14, 10), sharex=True)
fig.suptitle('User 1 Fitness Metrics vs Ideal', fontsize=18, weight='bold')
colors = sns.color_palette("Set2", n_colors=4)
metrics_list = ['Steps', 'Calories', 'Sleep Hours', 'Water Intake (L)']

for idx, (metric, ax) in enumerate(zip(metrics_list, axes.flatten())):
    # Plot user data
    ax.plot(df_user1['Day'], df_user1[metric], marker='o', color=colors[idx], label='User 1', linewidth=2)
    # Plot ideal value as a horizontal line
    ax.axhline(y=ideal_values[metric.lower().replace(' (l)', '_l').replace(' ', '_')], 
               color='red', linestyle='--', label='Ideal Value', linewidth=2)
    # Shade target range
    ax.axhspan(target_ranges[metric][0], target_ranges[metric][1], facecolor=colors[idx], alpha=0.2, label='Target Range')
    ax.set_title(metric, fontsize=14)
    ax.set_ylabel('Normalized (%)', fontsize=12)
    ax.legend(fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.7)

# Annotations for fitness score and average steps
fig.text(0.05, 0.95, f'Fitness Score: {data["assessments"]["1"]["fitness_score"]:.2f}',
         fontsize=12, weight='bold', color='darkblue', transform=fig.transFigure)
fig.text(0.05, 0.90, f'Avg Steps: {data["assessments"]["1"]["average_metrics"]["steps"]:.0f}',
         fontsize=10, color='darkblue', transform=fig.transFigure)

plt.xlabel('Day', fontsize=14)
plt.xticks(days, rotation=45)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig(output_path_user1, dpi=300, bbox_inches='tight')
plt.close()

# Plot for User 2
fig, axes = plt.subplots(2, 2, figsize=(14, 10), sharex=True)
fig.suptitle('User 2 Fitness Metrics vs Ideal', fontsize=18, weight='bold')
for idx, (metric, ax) in enumerate(zip(metrics_list, axes.flatten())):
    # Plot user data
    ax.plot(df_user2['Day'], df_user2[metric], marker='o', color=colors[idx], label='User 2', linewidth=2)
    # Plot ideal value as a horizontal line
    ax.axhline(y=ideal_values[metric.lower().replace(' (l)', '_l').replace(' ', '_')], 
               color='red', linestyle='--', label='Ideal Value', linewidth=2)
    # Shade target range
    ax.axhspan(target_ranges[metric][0], target_ranges[metric][1], facecolor=colors[idx], alpha=0.2, label='Target Range')
    ax.set_title(metric, fontsize=14)
    ax.set_ylabel('Normalized (%)', fontsize=12)
    ax.legend(fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.7)

# Annotations for fitness score and average steps
fig.text(0.05, 0.95, f'Fitness Score: {data["assessments"]["2"]["fitness_score"]:.2f}',
         fontsize=12, weight='bold', color='darkblue', transform=fig.transFigure)
fig.text(0.05, 0.90, f'Avg Steps: {data["assessments"]["2"]["average_metrics"]["steps"]:.0f}',
         fontsize=10, color='darkblue', transform=fig.transFigure)

plt.xlabel('Day', fontsize=14)
plt.xticks(days, rotation=45)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig(output_path_user2, dpi=300, bbox_inches='tight')
plt.close()

print(f"Graphs regenerated successfully at: {output_path_user1} and {output_path_user2}")