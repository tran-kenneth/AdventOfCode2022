import os

# Read input file.
current_path = os.path.dirname(__file__)
file = open(current_path + '/Inputs/6-input.txt')
lines = [line for line in file.readlines()]
file.close()

# Input datastream with removed new line character
input_character_buffer = lines[0][:-1]
# print(f'{input_character_buffer}, {len(input_character_buffer)}')

#four_char = input_character_buffer[-4:]
# print(four_char)


def find_marker_4():
    # Finds marker with 4 unique characters
    for char_index_start in range(len(input_character_buffer) - 3):
        char_index_end = char_index_start + 4
        four_char = input_character_buffer[char_index_start:char_index_end]
        # set should be length 4 if all unique
        set_of_four_chars = set(four_char)
        if (len(set_of_four_chars) == 4):
            # char_index_end is actually the character number
            return char_index_end


def find_marker_14():
    # Finds marker with 14 unique characters
    for char_index_start in range(len(input_character_buffer) - 13):
        char_index_end = char_index_start + 14
        four_char = input_character_buffer[char_index_start:char_index_end]
        # set should be length 14 if all unique
        set_of_four_chars = set(four_char)
        if (len(set_of_four_chars) == 14):
            # char_index_end is actually the character number
            return char_index_end


print(find_marker_4())
print(find_marker_14())
