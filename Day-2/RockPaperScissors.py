# Read input file.
file = open('input2.txt')
lines = [line for line in file.readlines()]
file.close()

"""
A - Rock
B - Paper
C - Scissors

X - Rock
Y - Paper
Z - Scissors

Scores:
1 - Choose rock
2 - Choose paper
3 - Choose scissors

0 - Lose
3 - Draw
6 - Win
"""
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
