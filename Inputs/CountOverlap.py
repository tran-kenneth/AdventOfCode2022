# Read input file.
file = open('input4.txt')
assignments_raw = [line for line in file.readlines()]
file.close()

# Remove new lines from input
assignments = [assignment[:-1] for assignment in assignments_raw]
