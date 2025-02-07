
"""
Author: Fatma Akkoca
Assignment: #1
"""
# creating variables
gym_member = "Alex Alliton"  # String
preferred_weight_kg = 20.5   # Float
highest_reps = 25            # Integer
membership_active = True     # Boolean


# Dictionary where keys are strings " Alex, Jamie, Taylor) values are tuples three integers

workout_stats = {
    "Alex": (10, 15, 20),
    "Jamie": (15, 20, 25),
    "Taylor": (20, 25, 75)}
print(workout_stats)


# Using a loop, calculate the total workout minutes for each friend
total_workout_times = {}

# Loop through workout_stats and calculate total workout minutes for each friend
for name, stats in workout_stats.items():
    total_minutes = sum(stats)  # Calculate total minutes
    total_workout_times[f"{name}_Total"] = total_minutes  # separate dictionary
    print(f"{name} did {total_minutes} minutes of workout.")

# Merge the new dictionary into workout_stats
workout_stats.update(total_workout_times)
print(workout_stats)

## Nested list where each row represents friend and each column represents (yoga, running, weightlifting)
workout_list = [list(stats) for name, stats in workout_stats.items() if "_Total" not in name]
print(workout_list)

# Get yoga & running minutes for all friends
yoga_running_minutes = []
for row in workout_list:
    yoga_running_minutes.append(row[:2])  # Get first two values (Yoga & Running)

print("Yoga & Running Minutes for All Friends:", yoga_running_minutes)

# Get weightlifting minutes for the last two friends
weightlifting_minutes = []
for row in workout_list[-2:]:  # Get only the last two friends
    weightlifting_minutes.append(row[2])  # Get the third value

print("Weightlifting Minutes for Last Two Friends:", weightlifting_minutes)


# Check if any friend's total workout minutes 120=>
for name in workout_stats:
    if "_Total" in name:  # Only check total
        if workout_stats[name] >= 120:
            friend_name = name.replace("_Total", "")  # Remove '_Total' from the name
            print("Great job staying active,", friend_name + "!")

# Ask user for a friend's name
friend_name = input("Enter a friend's name to check their workout stats: ")


# Check if the name exists in  dictionary
if friend_name in workout_stats:


    print(f"{friend_name}'s workout minutes:")
    print(f"Yoga: {workout_stats[friend_name][0]} min")
    print(f"Running: {workout_stats[friend_name][1]} min")
    print(f"Weightlifting: {workout_stats[friend_name][2]} min")

    # Check and print total workout time if available
    total_key = f"{friend_name}_Total"
    if total_key in workout_stats:
        print(f"Total workout time: {workout_stats[total_key]} min")

else:

    print(f"Friend {friend_name} not found in the records.")


# Extract only the total workout values from the dictionary
total_minutes_dict = {name: minutes for name, minutes in workout_stats.items() if "_Total" in name}

# Check if there are any total workout times
if total_minutes_dict:

    # Find the friend with the highest and lowest total workout minutes
    max_friend = max(total_minutes_dict, key=total_minutes_dict.get)
    min_friend = min(total_minutes_dict, key=total_minutes_dict.get)

    # Clean the names by removing "_Total"
    max_friend_name = max_friend.replace("_Total", "")
    min_friend_name = min_friend.replace("_Total", "")

    print(f"{max_friend_name} has the highest total workout time: {total_minutes_dict[max_friend]} min")
    print(f"{min_friend_name} has the lowest total workout time: {total_minutes_dict[min_friend]} min")

else:
    print("No workout data available to compare.")



