"""
    File name: spanning_tree.py
    Author: Matthew Carter
    Date created: 25/07/2020
    Date last modified: 27/07/2020
    Python Version: 3.8
"""

# Example.
# Key is current location. Values are dictionaries of potential destinations and their distances away from the location.
tree = {
        "entrance": {"ticket_booth": 2, "fan_zone": 6, "burger_van": 7},
        "ticket_booth": {"fan_zone": 3},
        "fan_zone": {"burger_van": 6, "garage": 7},
        "burger_van": {"garage": 2},
        "garage": {}
        }

# Challenge.
# Key is current location. Values are dictionaries of potential destinations and their distances away from the location.
# tree = {
#         "entrance": {"ticket": 2, "press_pen": 6},
#         "press_pen": {"vip_restaurant": 2, "fan_zone": 1},
#         "vip_restaurant": {"grandstand": 2, "garage": 5},
#         "ticket": {"fan_zone": 2},
#         "fan_zone": {"press_pen": 1, "grandstand": 4},
#         "grandstand": {"vip_restaurant": 2, "garage": 1},
#         "garage": {}
#         }


# def destination_in_dict(dictionary, destination):
#     for dest_key, dest_val in dictionary.items():
#         if dest_key == destination:
#             # A match.
#             return True
#     # No matches.
#     return False
#
#
# start_location = "entrance"
# final_destination = "garage"
#
# # Get all locations that lead to the "garage".
# penultimate_locations = []
# for location, destinations in tree.items():
#     if destination_in_dict(destinations, final_destination):
#         penultimate_locations.append(location)
#
# # Work way back from penultimate location to "entrance".
# for penultimate_location in penultimate_locations:
#     print(f"{final_destination} ->")
#     print(f"{penultimate_location} ->")
#     current_location = penultimate_location
#     while current_location != start_location:
#         for location, destinations in tree.items():
#             if destination_in_dict(destinations, current_location):
#                 current_location = location
#                 print(f"{current_location} ->")
#                 break
#             print(f"{current_location} ->")
#     print()

# TODO: Going to revise approach and work from start point, keeping tab on timings of routes.

start_location = "entrance"
final_destination = "garage"

# Create potential paths from starting point.
# Path dictionary format eg: paths = {"path_1": (["locationA", "locationB"], 3)}
paths = {}
path_number = 1
for location, time in tree[start_location].items():
    paths[f"path_{path_number}"] = ([location], time)
    path_number += 1
print(paths)

# Select path with lowest travel time.
current_path = "none"
current_path_route = []
current_path_time = 0
for path_no, path_info in paths.items():
    if current_path_time == 0 or path_info[1] < current_path_time:
        current_path = path_no
        current_path_route = path_info[0]
        current_path_time = path_info[1]
print(current_path, current_path_route, current_path_time)

# Get next potential destinations on current path.
