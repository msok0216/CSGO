import pickle, json, pandas as pd, numpy as np
import matplotlib.pyplot as plt
from ProcessGameState import ProcessGameState

obj = ProcessGameState("./data/game_state_frame_data.pickle", "output.json", [[-1735, 250], [-2024, 398], [-2806, 742], [-2472, 1233], [-1565, 580]])
obj._build()
obj._buildByRounds()
# 2.C.check location of Team2 on CT in BombsiteB
x_coordinates, y_coordinates = [], []

# Collect all the data by rounds where Team2 is CT
for round_data in obj.dataByRounds:
    for data in round_data:
        if data.team == 'Team2' and data.side == 'CT' and data.area_name == 'BombsiteB':
            x_coordinates.append(data.x)
            y_coordinates.append(data.y)


# retrieve max and min of x y coordinates 
y_min, y_max, x_min, x_max = float('inf'), float('-inf'), float('inf'), float('-inf')

for i in range(len(x_coordinates)):
    y_min = min(y_min, y_coordinates[i])
    y_max = max(y_max, y_coordinates[i])
    x_min = min(x_min, x_coordinates[i])
    x_max = max(x_max, x_coordinates[i])



# Sample data (replace with your own x, y coordinates)

# Define the grid size and the resolution
grid_size = 50
resolution = 1 / grid_size

# Create a 2D histogram
heatmap, xedges, yedges = np.histogram2d(x_coordinates, y_coordinates, bins=grid_size, range=[[x_min, x_max], [y_min, y_max]])

# Set up the figure and axis
fig, ax = plt.subplots()

# Create the heatmap using imshow
im = ax.imshow(heatmap.T, extent=[0, 1, 0, 1], origin='lower', cmap='hot')

# Add a colorbar
cbar = plt.colorbar(im, ax=ax)

# Set the labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Heatmap')

# Display the plot
plt.show()