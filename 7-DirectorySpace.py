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

    clean_lines = [line[:-1] for line in lines[1:]]

    root_node = Node(type="dir", name="/")
    pwd = root_node

    for cmd_line in clean_lines:
        if (is_command(cmd_line)):
            instructions = parse_command(cmd_line)

            if (instructions["command"] == "ls"):
                pass
            elif (instructions["command"] == "cd"):
                dir_name = instructions["dir"]

                if dir_name == "..":
                    pwd = pwd.parent
                else:
                    for child in pwd.children:
                        if child.name == dir_name:
                            #print(f'pwd: {child.name}')
                            pwd = child

        elif (is_dir(cmd_line)):
            dir_name = parse_dir(cmd_line)
            pwd.add_child(type="dir", name=dir_name)

        else:
            file_info = parse_file(cmd_line)
            pwd.add_child(
                type="file", name=file_info["name"], data=file_info["data"])

    # print(root_node.count_child_values())

    small_dirs = []

    def count_small_dirs(node_list):
        for node in node_list:
            if (node.type == "dir"):
                # print(
                #    f"Dir: {node.name}, Children: {node.count_child_values()}")
                dir_size = node.count_child_values()
                if 0 < dir_size <= 100000:
                    small_dirs.append(dir_size)
                count_small_dirs(node.children)

    count_small_dirs(root_node.children)

    starting_total = root_node.count_child_values()

    small_dir_total = 0
    for size in small_dirs:
        small_dir_total += size
    print(small_dir_total)


def is_command(line):
    return line[0] == "$"


def is_dir(line):
    return line[:3] == "dir"


def parse_command(line):
    cmd_regex = re.match(r"\$ (\w+) ?(.+)?", line)
    return {
        "command": cmd_regex.group(1),
        "dir": cmd_regex.group(2)
    }


def parse_dir(line):
    dir_regex = re.match(r"dir (\w+)", line)
    return dir_regex.group(1)


def parse_file(line):
    file_regex = re.match(r"(\d+) (.+)", line)
    return {
        "data": int(file_regex.group(1)),
        "name": file_regex.group(2)
    }


if __name__ == "__main__":
    main()
