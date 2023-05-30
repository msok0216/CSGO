import pickle, json, pandas as pd, numpy as np
from GameState import StatePerFrame, Weapon

'''
    The object to create an ETL pipeline for the given data.

    input_file: path to the pickle file that contains all data
    output_file: path to the output file where the user might like to output the transformed data in the future
    coordinates: coordinates of the points that define the light blue region
    data: in case user would like to pass predefined data

    dataByRounds: data sotred by its round
    
'''
class ProcessGameState(object):
    def __init__(self, input_file, output_file, coordinates, data = None) -> None:
        self.input_file = input_file
        self.output_file = output_file
        self.data = data
        self.transformed_data = None
        self.coordinates = coordinates
        self.dataByRounds = None
    
    # extract data from the pickle file 
    def extract(self):
        with open(self.input_file, 'rb') as f:
            data = pickle.load(f)
        return pd.DataFrame(data)
    
    # transform each row to a stateperframe object
    def transform(self, data):
        dict_data = data.to_dict(orient='records')
        transformed_data = [StatePerFrame(i) for i in dict_data]
        return transformed_data
    
    # store the transformed data within the ProcessGameState object.
    def load(self, data, output_file):
        # with open(self.output_file, 'w') as f:
        #     json.dump(data, f, indent=4)
        # self.data = json.dump(data, indent=4)
        self.transformed_data = data

    # extract, transform, and load data.
    def _build(self):
        data = self.extract()
        transformed_data = self.transform(data)
        self.load(transformed_data, self.output_file)

    # can be called after the _build() function. Create dataByRounds attribute and store data by rounds
    def _buildByRounds(self):
        if self.dataByRounds is None:
            self.dataByRounds = []
            round_num = self.transformed_data[-1].round_num
            for i in range(0, round_num): self.dataByRounds.append([])
            for i in self.transformed_data:
                round = i.round_num
                self.dataByRounds[round-1].append(i)
    
    # retrieve data related to the given round
    def getRoundData(self, round):
        return self.dataByRounds[round-1]
    
    # determine if the given coordinate is within the light blue region
    def is_point_within_area(self, x, y):
        # Initialize a counter
        count = 0
        num_points = len(self.coordinates)

        # Iterate over the edges of the polygon
        for i in range(num_points):
            x1, y1 = self.coordinates[i]
            x2, y2 = self.coordinates[(i + 1) % num_points]

            # Check if the point is on the same level as the edge
            if y == y1 == y2:
                if min(x1, x2) <= x <= max(x1, x2):
                    return True

            # Check if the point is above or below the edge
            if min(y1, y2) < y <= max(y1, y2):
                # Calculate the intersection point
                intersection = (x1 + (y - y1) * (x2 - x1) / (y2 - y1))

                # Count the intersections on the right side of the point
                if intersection > x:
                    count += 1

        # If the count is odd, the point is within the polygon
        return count % 2 == 1    

