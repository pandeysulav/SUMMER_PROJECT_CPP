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

# Create DataFrames
df_user1 = pd.DataFrame({
    'Day': days,
    'Steps': user_data['1']['steps'],
    'Calories': user_data['1']['calories'],
    'Sleep Hours': user_data['1']['sleep_hours'],
    'Water Intake (L)': user_data['1']['water_intake_l']
})

df_user4 = pd.DataFrame({
    'Day': days,
    'Steps': user_data['4']['steps'],
    'Calories': user_data['4']['calories'],
    'Sleep Hours': user_data['4']['sleep_hours'],
    'Water Intake (L)': user_data['4']['water_intake_l']
})

# Define output paths
output_path_user1 = r"E:\SUMMER_PROJECT_CPP\ML\outputs\user1_good_fitness_plot.png"
output_path_user4 = r"E:\SUMMER_PROJECT_CPP\ML\outputs\user4_excellent_fitness_plot.png"

# Define target ranges for shading
target_ranges = {
    'Steps': (10000, 15000),  # Recommended step range
    'Calories': (2000, 3000),  # Healthy calorie burn range
    'Sleep Hours': (7, 8),     # Recommended sleep range
    'Water Intake (L)': (2.5, 3.5)  # Recommended water intake
}

# Plot for User 1 (Good)
fig, axes = plt.subplots(2, 2, figsize=(14, 10), sharex=True)
fig.suptitle('Fitness Metrics for User 1 (Good Fitness, Score: 57.25)', fontsize=18, weight='bold', y=1.05)
axes = axes.flatten()
colors = sns.color_palette("Greens", n_colors=4)

for idx, metric in enumerate(['Steps', 'Calories', 'Sleep Hours', 'Water Intake (L)']):
    ax = axes[idx]
    sns.lineplot(x='Day', y=metric, data=df_user1, ax=ax, color=colors[idx], marker='o', linewidth=2.5, markersize=8)
    
    # Add trend line
    z = np.polyfit(df_user1['Day'], df_user1[metric], 1)
    p = np.poly1d(z)
    ax.plot(df_user1['Day'], p(df_user1['Day']), linestyle='--', color='darkgreen', alpha=0.6)
    
    # Shade target range
    ax.fill_between(df_user1['Day'], target_ranges[metric][0], target_ranges[metric][1], 
                    color='lightgreen', alpha=0.2, label='Target Range')
    
    # Annotate max and min values
    max_val = df_user1[metric].max()
    min_val = df_user1[metric].min()
    max_day = df_user1['Day'][df_user1[metric].idxmax()]
    min_day = df_user1['Day'][df_user1[metric].idxmin()]
    ax.annotate(f'Max: {max_val:.1f}', xy=(max_day, max_val), xytext=(0, 10), 
                textcoords='offset points', ha='center', fontsize=10, color='darkgreen')
    ax.annotate(f'Min: {min_val:.1f}', xy=(min_day, min_val), xytext=(0, -15), 
                textcoords='offset points', ha='center', fontsize=10, color='darkgreen')
    
    ax.set_title(metric, fontsize=14, weight='bold')
    ax.set_xlabel('Day', fontsize=12)
    ax.set_ylabel(metric, fontsize=12)
    ax.legend(loc='best', fontsize=10)

plt.tight_layout()
plt.savefig(output_path_user1, dpi=300, bbox_inches='tight')
plt.close()

# Plot for User 4 (Excellent)
fig, axes = plt.subplots(2, 2, figsize=(14, 10), sharex=True)
fig.suptitle('Fitness Metrics for User 4 (Excellent Fitness, Score: 61.41)', fontsize=18, weight='bold', y=1.05)
axes = axes.flatten()
colors = sns.color_palette("Blues", n_colors=4)

for idx, metric in enumerate(['Steps', 'Calories', 'Sleep Hours', 'Water Intake (L)']):
    ax = axes[idx]
    sns.lineplot(x='Day', y=metric, data=df_user4, ax=ax, color=colors[idx], marker='o', linewidth=2.5, markersize=8)
    
    # Add trend line
    z = np.polyfit(df_user4['Day'], df_user4[metric], 1)
    p = np.poly1d(z)
    ax.plot(df_user4['Day'], p(df_user4['Day']), linestyle='--', color='darkblue', alpha=0.6)
    
    # Shade target range
    ax.fill_between(df_user4['Day'], target_ranges[metric][0], target_ranges[metric][1], 
                    color='lightblue', alpha=0.2, label='Target Range')
    
    # Annotate max and min values
    max_val = df_user4[metric].max()
    min_val = df_user4[metric].min()
    max_day = df_user4['Day'][df_user4[metric].idxmax()]
    min_day = df_user4['Day'][df_user4[metric].idxmin()]
    ax.annotate(f'Max: {max_val:.1f}', xy=(max_day, max_val), xytext=(0, 10), 
                textcoords='offset points', ha='center', fontsize=10, color='darkblue')
    ax.annotate(f'Min: {min_val:.1f}', xy=(min_day, min_val), xytext=(0, -15), 
                textcoords='offset points', ha='center', fontsize=10, color='darkblue')
    
    ax.set_title(metric, fontsize=14, weight='bold')
    ax.set_xlabel('Day', fontsize=12)
    ax.set_ylabel(metric, fontsize=12)
    ax.legend(loc='best', fontsize=10)

plt.tight_layout()
plt.savefig(output_path_user4, dpi=300, bbox_inches='tight')
plt.close()

print(f"Graphs generated successfully at: {output_path_user1} and {output_path_user4}")