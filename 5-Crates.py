import os

# Read input file.
current_path = os.path.dirname(__file__)
file = open(current_path + '/Inputs/5-input.txt')
lines = [line for line in file.readlines()]
file.close()

# Create stacks of boxes
stacks, move_list = [], []


def print_starting_stacks():
    for index in range(8):
        print(lines[index])


def parse_stacks():
    # Assign starting input to stacks

    # Initialize array for each stack
    for i in range(9):
        stacks.append([])

    # Loop through the 9 stacks
    for stack_index in range(9):
        char_start_index = 1 + (stack_index * 4)
        char_end_index = char_start_index + 1

        # Loop through height of stacks from bottom to top
        for height in range(8):
            char_to_add = lines[7 - height][char_start_index:char_end_index]
            if (char_to_add != ' '):
                stacks[stack_index].append(char_to_add)


def parse_moves():
    import re

    for line_index in range(10, len(lines)):
        move_set = re.findall("\d+", lines[line_index])
        move_list.append(move_set)


def print_stacks():
    for box_stack in stacks:
        print(box_stack)


def print_move_list():
    for moves in move_list:
        print(moves)


parse_stacks()
parse_moves()


def perform_moves():
    for moves in move_list:
        num_to_move = int(moves[0])
        index_of_origin_stack = int(moves[1]) - 1
        index_of_end_stack = int(moves[2]) - 1

        for box in range(num_to_move):
            box_moved = stacks[index_of_origin_stack].pop()
            stacks[index_of_end_stack].append(box_moved)


def perform_moves_multibox():
    #count = 0
    for moves in move_list:
        num_to_move = int(moves[0])
        index_of_origin_stack = int(moves[1]) - 1
        index_of_end_stack = int(moves[2]) - 1

        originating_stack = stacks[index_of_origin_stack]
        ending_stack = stacks[index_of_end_stack]

        boxes_to_move = originating_stack[len(
            originating_stack) - num_to_move:]
        #print("before", originating_stack, boxes_to_move)
        #print("move", ending_stack, boxes_to_move)
        del originating_stack[len(originating_stack) - num_to_move:]
        stacks[index_of_end_stack] = ending_stack + boxes_to_move
        #print("after", originating_stack, ending_stack)
        #print("move line: ", count + 11, "\n")
        #count += 1


perform_moves_multibox()
print_stacks()
