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


def find_index():
    for char_index_start in range(len(input_character_buffer) - 3):
        char_index_end = char_index_start + 4
        four_char = input_character_buffer[char_index_start:char_index_end]
        set_of_four_chars = set(four_char)
        if (len(set_of_four_chars) == 4):
            return char_index_end


test_chars = "qqwe"
set_test_chars = set(test_chars)
print(len(set_test_chars))

print(find_index())
