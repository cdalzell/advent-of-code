# Column One (Opponent)
# A: Rock
# B: Paper
# C: Scissors

# Column Two (Player)
# X: Rock
# Y: Paper
# Z: Scissors
from bidict import bidict

win = 6
lose = 0
draw = 3

advantages = bidict({"X": "C", "Y": "A", "Z": "B"})
disadvantages = {"A": "Z", "B": "X", "C": "Y"}
draws = bidict({"X": "A", "Y": "B", "Z": "C"})
points = {"X": 1, "Y": 2, "Z": 3}

total_points_part_one = 0
total_points_part_two = 0

with open("input.txt","r") as input_file:
    for line in input_file:
        round_result = line.strip().split()

        # Part One
        total_points_part_one += points[round_result[1]]

        if draws[round_result[1]] == round_result[0]:
            total_points_part_one += draw
        elif advantages[round_result[1]] == round_result[0]:
            total_points_part_one += win

        # Part Two
        if round_result[1] == "X": # lose
            total_points_part_two += points[disadvantages[round_result[0]]]
        elif round_result[1] == "Y":
            total_points_part_two += draw + points[draws.inverse[round_result[0]]]
        else:
            total_points_part_two += win + points[advantages.inverse[round_result[0]]]


print(f"Total Points (Part One): {total_points_part_one}")
print(f"Total Points (Part Two): {total_points_part_two}")
