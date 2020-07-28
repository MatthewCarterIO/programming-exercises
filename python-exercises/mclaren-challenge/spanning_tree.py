"""
    File name: spanning_tree.py
    Author: Matthew Carter
    Date created: 25/07/2020
    Date last modified: 28/07/2020
    Python Version: 3.8
"""

# Example.
# Key is current location. Values are dictionaries of potential destinations and their distances away from the location.
# tree = {
#         "entrance": {"ticket_booth": 2, "fan_zone": 6, "burger_van": 7},
#         "ticket_booth": {"fan_zone": 3},
#         "fan_zone": {"burger_van": 6, "garage": 7},
#         "burger_van": {"garage": 2},
#         "garage": {}
#         }

# Challenge.
# Key is current location. Values are dictionaries of potential destinations and their distances away from the location.
tree = {
        "entrance": {"ticket": 2, "press_pen": 6},
        "press_pen": {"vip_restaurant": 2, "fan_zone": 1},
        "vip_restaurant": {"grandstand": 2, "garage": 5},
        "ticket": {"fan_zone": 2},
        "fan_zone": {"press_pen": 1, "grandstand": 4},
        "grandstand": {"vip_restaurant": 2, "garage": 1},
        "garage": {}
        }

start_location = "entrance"
final_destination = "garage"

# Create potential paths from starting point.
# Path dictionary format {path number: ([path route locations], path total travel time), path completely traversed bool}
# eg: paths = {"path_1": (["locationA", "locationB"], 3), False}
paths = {}
path_number_counter = 1
for location, time in tree[start_location].items():
    paths[f"path_{path_number_counter}"] = (["entrance", location], time, False)
    path_number_counter += 1
print(paths)

# While paths still need traversing...
all_paths_traversed = False
while all_paths_traversed == False:
    current_path_number = "none"
    current_path_route = []
    current_path_time = 0
    # Select the path with the lowest total travel time to be the current path.
    for path_no, path_info in paths.items():
        # Only check paths that haven't been fully traversed.
        if path_info[2] == False:
            if current_path_time == 0 or path_info[1] < current_path_time:
                current_path_number = path_no
                current_path_route = path_info[0]
                current_path_time = path_info[1]
    print("CURRENT PATH: ", current_path_number, current_path_route, current_path_time)

    # Get potential next destinations from the last location on the current path (given by current_path_route[-1]).
    # From these get the closest one.
    potential_destinations = []
    shortest_travel_time = 0
    shortest_travel_destination = "none"
    for next_destination, next_destination_time in tree[current_path_route[-1]].items():
        # Ensure the potential next destination has not already been visited on the current path.
        if next_destination not in current_path_route:
            # Add potential destination to list.
            potential_destinations.append((next_destination, next_destination_time))
            if shortest_travel_time == 0 or next_destination_time < shortest_travel_time:
                # Destination is closest.
                shortest_travel_time = next_destination_time
                shortest_travel_destination = next_destination
    # Remove shortest travel destination from potential destinations list so it is not duplicated later when creating
    # new paths.
    potential_destinations.remove((shortest_travel_destination, shortest_travel_time))

    # Check if the next (closest) destination to be added to the path matches the last destination already present on
    # any other existing paths and if it does compare their travel times to see how to proceed.
    shorter_path_exists = False
    for path_no, path_info in paths.items():
        # Only check paths that haven't been fully traversed.
        if path_info[2] == False:
            if path_info[0][-1] == shortest_travel_destination:
                # Last destination in an existing path matches the potential next destination of current path.
                if path_info[1] >= (current_path_time + shortest_travel_time):
                    # Time to reach next destination on current path would be shorter or equal to the time taken on an
                    # existing path. Therefore mark the existing path as completely traversed in path dictionary.
                    paths[path_no] = (path_info[0], path_info[1], True)
                else:
                    # Time to reach next destination on current path would be longer than the time taken on an
                    # existing path. Mark current path as completely traversed in path dictionary.
                    paths[current_path_number] = (current_path_route, current_path_time, True)
                    shorter_path_exists = True

    # If no shorter path already exists, add the next destination to the current path.
    if shorter_path_exists is False:
        # Before updating the current path, create new paths for the other potential destinations if there are any.
        if len(potential_destinations):
            for potential_destination in potential_destinations:
                potential_path_route = current_path_route.copy()
                potential_path_route.append(potential_destination[0])
                potential_path_time = current_path_time + potential_destination[1]
                # Only create new path if an existing one with shorter travel time to potential destination doesn't
                # exist.
                for path_no, path_info in paths.items():
                    # Only check paths that haven't been fully traversed.
                    if path_info[2] == False:
                        if path_info[0][-1] == potential_path_route[-1]:
                            if path_info[1] >= potential_path_time:
                                # Final destination of potential path exists, but time to reach it on existing path is
                                # longer or equal than it would be on new potential path. Therefore mark the existing
                                # path as completely traversed in path dictionary and create new path.
                                paths[path_no] = (path_info[0], path_info[1], True)
                                paths[f"path_{path_number_counter}"] = (potential_path_route, potential_path_time, False)  ##
                                path_number_counter += 1  ##

        # Append next location to the current path
        current_path_route.append(shortest_travel_destination)
        current_path_time += shortest_travel_time
        # Update path in dictionary
        paths[current_path_number] = (current_path_route, current_path_time, False)
        print("CURRENT PATH UPDATED: ", current_path_number, current_path_route, current_path_time)

    # If the final destination has been reached on the current path, mark it as traversed.
    if current_path_route[-1] == final_destination:
        paths[current_path_number] = (current_path_route, current_path_time, True)

    # Check if all paths have been completely traversed. If not, break and continue from top of while loop.
    all_paths_traversed = True
    for path_no, path_info in paths.items():
        if path_info[2] == False:
            # Still a path that needs traversing.
            all_paths_traversed = False
            break

    print()
    print(paths)
    print("-------------")

