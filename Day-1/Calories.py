
file = open('input1.txt')
lines = [line for line in file.readlines()]
file.close()

print(len(lines))
