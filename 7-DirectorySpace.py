import os

# Read input file.
current_path = os.path.dirname(__file__)
file = open(current_path + '/Inputs/7-input.txt')
lines = [line for line in file.readlines()]
file.close()

clean_lines = [line[:-1] for line in lines]
# print(clean_lines)

# Create Dictionary to represent directory file space?
device_files = {}
current_cursor = None


def handle_cd(command):
    directory = command[5:]
    current_cursor = directory

    try:
        print(device_files[directory])
    except:
        device_files[directory] = {}

    current_cursor = device_files[directory]
    return


def handle_ls():
    return


count = 0
for command in clean_lines:
    if command[:4] == '$ cd':
        handle_cd(command)
        print(command)

    if command[:4] == '$ ls':
        handle_ls()
        print(command)
    count += 1
    if (count > 10):
        break

print(device_files)
