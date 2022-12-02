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
