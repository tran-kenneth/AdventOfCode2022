import os
import re


class Node:
    def __init__(self, type, name, data=None, parent=None):
        self.type = type
        self.name = name
        self.parent = parent

        self.data = data
        if (self.type == "dir"):
            self.children = []

    def add_child(self, type, name, data=None):
        child = Node(type=type, name=name, data=data, parent=self)
        self.children.append(child)

    def count_child_values(self):
        total = 0
        for child in self.children:
            if (child.type == "dir"):
                total += child.count_child_values()
            elif (child.type == "file"):
                total += child.data
        return total

    def __str__(self):
        if (self.type == "dir"):
            return f'Name: {self.name}\nChildren: {self.children}\nData: {self.data}\nParent: {self.parent}'
        else:
            return f'Name: {self.name}\nData: {self.data}\nParent: {self.parent}'


def main():
    # Read input file.
    current_path = os.path.dirname(__file__)
    file = open(current_path + '/Inputs/7-input.txt')
    lines = [line for line in file.readlines()]
    file.close()

    clean_lines = [line[:-1] for line in lines]

    for cmd_line in clean_lines:
        cd_command = re.match(r"\$ cd (.+)", cmd_line)
        #print(cmd_line, cd_command)
        if (cd_command):
            # print(cd_command.group(1))
            dir_name = cd_command.group(1)

        if cmd_line == "dir dmd":
            break
        ...


if __name__ == "__main__":
    main()
