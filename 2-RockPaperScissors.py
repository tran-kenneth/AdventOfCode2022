import os

# Read input file.
current_path = os.path.dirname(__file__)
file = open(current_path + '/Inputs/2-input.txt')
lines = [line for line in file.readlines()]
file.close()

clean_lines = [line[:3] for line in lines]
print(clean_lines)

score_key = {
    'A X': 1+3,
    'A Y': 2+6,
    'A Z': 3+0,
    'B X': 1+0,
    'B Y': 2+3,
    'B Z': 3+6,
    'C X': 1+6,
    'C Y': 2+0,
    'C Z': 3+3
}

score_total = 0

for line in clean_lines:
    score_total += score_key[line]
print(score_total)


# Part 2
# X means lose
# Y means draw
# Z means win

score_key_part_2 = {
    'A X': 3+0,
    'A Y': 1+3,
    'A Z': 2+6,
    'B X': 1+0,
    'B Y': 2+3,
    'B Z': 3+6,
    'C X': 2+0,
    'C Y': 3+3,
    'C Z': 1+6
}

score_total_part_2 = 0

for line in clean_lines:
    score_total_part_2 += score_key_part_2[line]
print(score_total_part_2)
