import os

# Read input file.
current_path = os.path.dirname(__file__)
file = open(current_path + '/Inputs/1-input.txt')
lines = [line for line in file.readlines()]
file.close()

calorie_total_by_elf = []

temp_elf_total = 0

# Sum total of calories carried by each elf.
for line in lines:
    if line == '\n':
        calorie_total_by_elf.append(temp_elf_total)
        temp_elf_total = 0
    else:
        calorie_num = int(line[:len(line)-1])
        temp_elf_total += calorie_num

# Find elf with the most calories
most_calories = max(calorie_total_by_elf)

# Index of the elf with the most calories
index_most_calories = [index for index, value in enumerate(
    calorie_total_by_elf) if value == most_calories]

# Output of the elf with the most calories
print(index_most_calories, most_calories)

# Part 2: Find total number of calories held by
#         the top 3 elves holding the most calories.

total_calories_top_three = 0
for i in range(3):
    most_calories = max(calorie_total_by_elf)
    total_calories_top_three += most_calories
    calorie_total_by_elf.remove(most_calories)

print(total_calories_top_three)
