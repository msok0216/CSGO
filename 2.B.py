import pickle, json, pandas as pd, numpy as np
from ProcessGameState import ProcessGameState

obj = ProcessGameState("./data/game_state_frame_data.pickle", "output.json", [[-1735, 250], [-2024, 398], [-2806, 742], [-2472, 1233], [-1565, 580]])
obj._build()
obj._buildByRounds()

# 2.B. Calculate the average time it takes for Team2 on T side to enter bombsiteb with at least 2 rifles or SMGS
times = []

# Iterate through all the rounds
# Keep track of players in each round to accurately calculate the total number of rifles and SMGS used by the team
# if the team made it into the bombsiteb with at least 2 rifles/smgs, add it to the times list
for round_num in range(30):
    players = set()
    count_rifles_and_smgs = 0
    data = obj.getRoundData(round_num)
    bombsiteb_time = None
    for data in obj.getRoundData(round_num):
        if  data.team == 'Team2' and data.side == 'T':
            if bombsiteb_time is None and data.area_name == 'BombsiteB':
                bombsiteb_time = data.tick
            if data.player not in players:
                players.add(data.player)
                for weapon_class, weapons in data.inventory.items():
                    if weapon_class == 'SMG' or weapon_class == 'Rifle':
                        count_rifles_and_smgs += len(weapons)
    if count_rifles_and_smgs >= 2:
        if bombsiteb_time is not None: 
#             times.append([round,-1])
            times.append(bombsiteb_time)
    
            
# calculate the average of the times collected in the previous steps
sum = 0
for i in times: sum += i
print(sum / len(times))