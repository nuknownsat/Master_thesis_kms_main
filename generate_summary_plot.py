import matplotlib.pyplot as plt
import numpy as np
import os

# Data
schemes = ['Set 1', 'Set 2', 'Set 3', 'Set 4', 'Random', 'Set 5', 'Set 6', 'Set 7', 'Set 8', 'Proposed']
metrics = {
    'FLSO': [16.99, 11.55, 8.73, 8.40, 7.96, 7.95, 8.46, 7.75, 10.52, 7.98],
    'UFLSO': [5.09, 2.94, 2.41, 2.18, 2.52, 2.75, 3.26, 2.89, 4.32, 2.51],
    'ToS [s]': [24.53, 31.59, 44.14, 44.26, 39.29, 47.05, 45.74, 49.96, 33.94, 44.35],
    'RSRP [dBm]': [-55.24, -55.86, -59.23, -59.26, -58.18, -58.62, -58.41, -58.91, -59.12, -58.71],
    'Traffic [Gbps]': [1.10, 1.33, 1.19, 1.19, 1.51, 1.80, 1.82, 1.80, 1.91, 1.90],
    'Fairness': [0.77, 0.79, 0.67, 0.68, 0.83, 0.82, 0.81, 0.82, 0.83, 0.82]
}

# Setup figure
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
axes = axes.flatten()

# Colors
colors = ['#1f77b4'] * 9 + ['#d62728'] # Highlight Proposed in red

for i, (metric_name, values) in enumerate(metrics.items()):
    ax = axes[i]
    bars = ax.bar(schemes, values, color=colors)
    
    # Title and labels
    ax.set_title(metric_name, fontsize=12, fontweight='bold')
    ax.tick_params(axis='x', rotation=45, labelsize=8)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        # Handle negative values for RSRP
        if height < 0:
            xy_pos = (bar.get_x() + bar.get_width() / 2, height - 1)
            va = 'top'
        else:
            xy_pos = (bar.get_x() + bar.get_width() / 2, height + 0.1)
            va = 'bottom'
            
        ax.text(xy_pos[0], xy_pos[1], f'{height:.2f}', 
                ha='center', va=va, fontsize=7, rotation=0)

    # Adjust y-limits for better visualization
    if metric_name == 'RSRP [dBm]':
        ax.set_ylim(min(values) - 2, max(values) + 2)
    else:
        ax.set_ylim(0, max(values) * 1.15)

plt.tight_layout()

# Save
output_dir = 'figure'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    
output_path = os.path.join(output_dir, 'summary_performance.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Figure saved to {output_path}")
