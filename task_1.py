import pandas as pd
from geopy.distance import geodesic
from geopy.point import Point
from math import sqrt

df = pd.read_excel(r"C:\Users\Eriona\Downloads\ItalyLegaA.xlsx")
df.head()


# Function to calculate distance between two coordinates
def calculate_distance(coord1, coord2):
    coord1_verona = (45.43838419999999, 10.9916215)
    coord2_naples = (40.8517746, 14.2681244)

    distance = sqrt((coord2_naples[0] - coord1_verona[0]) ** 2 + (coord2_naples[1] - coord1_verona[1]) ** 2)
    return distance


print(calculate_distance((45.43838419999999, 10.9916215), (40.8517746, 14.2681244)))

# Determine value of “base home advantage” and create formula for “distance parameter” Outcome
home_points = 67
away_points = 61
total_points_2 = 128
total_points = 128
total_points_ = 124
home_points_average = ((home_points / total_points) * 100)
away_points_average = ((away_points / total_points_2) * 100)
print(home_points_average)
print(away_points_average)
# Calculate base home advantage

base_home_advantage = home_points_average - away_points_average
print( base_home_advantage)

 # Create formula for distance parameter
def calculate_distance_points(distance, coefficient):


    distance=215
    coefficient=0.75
    result= (distance * coefficient)
    return result
print(calculate_distance_points(215,0.75))
