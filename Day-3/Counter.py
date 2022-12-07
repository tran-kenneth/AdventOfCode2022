# Read input file.
file = open('input3.txt')
lines = [line for line in file.readlines()]
file.close()

print(lines)
