import os
import re

# Read input file.
current_path = os.path.dirname(__file__)
file = open(current_path + '/Inputs/7-input.txt')
lines = [line for line in file.readlines()]
file.close()

clean_lines = [line[:-1] for line in lines]
# print(clean_lines)


class Folder:
    def __init__(self, name="new folder"):
        self.name = name
        self.contents = []

    def add_folder(self, name):
        new_folder = Folder(name)
        self.contents.append(new_folder)

    def add_file(self, name, size):
        new_file = File(name, size)
        self.contents.append(new_file)


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


root_node = Folder("/")
for cmd_line in clean_lines:
    cd_command = re.match(r"\$ cd (.+)", cmd_line)
    print(cmd_line, cd_command)
    if (cd_command):
        print(cd_command.group())

    if cmd_line == "dir dmd":
        break
    ...


command_count = 0
commands = []
for input_line in clean_lines:
    if "$" in input_line:
        command_count += 1

# Enum, group ls lists with
# for k, v in enumerate(clean_lines):
#    print(k, v)
#    if k == 10:
#        break

print(command_count)
