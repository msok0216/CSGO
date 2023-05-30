import pickle, json, pandas as pd, numpy as np
from ProcessGameState import ProcessGameState

obj = ProcessGameState("./data/game_state_frame_data.pickle", "output.json", [[-1735, 250], [-2024, 398], [-2806, 742], [-2472, 1233], [-1565, 580]])
obj._build()
obj._buildByRounds()

# 2.A. check if the given players' location falls within the light blue region
count = 0
for i in range(30):
    data = obj.getRoundData(i)
    for j in data:
        if j.team == 'Team2' and j.side == 'T' and obj.is_point_within_area(j.x, j.y):
            count+=1
            break
print(count)