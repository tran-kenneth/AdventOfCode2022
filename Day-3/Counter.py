# Read input file.
file = open('input3.txt')
rucksacks = [line for line in file.readlines()]
file.close()

# Rucksack letter key values
rucksack_key_values = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4,
    'e': 5, 'f': 6, 'g': 7, 'h': 8,
    'i': 9, 'j': 10, 'k': 11, 'l': 12,
    'm': 13, 'n': 14, 'o': 15, 'p': 16,
    'q': 17, 'r': 18, 's': 19, 't': 20,
    'u': 21, 'v': 22, 'w': 23, 'x': 24,
    'y': 25, 'z': 26,
    'A': 1+26, 'B': 2+26, 'C': 3+26, 'D': 4+26,
    'E': 5+26, 'F': 6+26, 'G': 7+26, 'H': 8+26,
    'I': 9+26, 'J': 10+26, 'K': 11+26, 'L': 12+26,
    'M': 13+26, 'N': 14+26, 'O': 15+26, 'P': 16+26,
    'Q': 17+26, 'R': 18+26, 'S': 19+26, 'T': 20+26,
    'U': 21+26, 'V': 22+26, 'W': 23+26, 'X': 24+26,
    'Y': 25+26, 'Z': 26+26,
}

# Remove new lines from input
clean_rucksacks = [rucksack[:-1] for rucksack in rucksacks]


def find_common_letter(list1, list2):
  # Find the common letter in two lists
    print(list1, list2)
    for letter1 in list1:
        for letter2 in list2:
            if (letter1 == letter2):
                return letter1


def sum_value_common_letters():
    # Find value of common letter of each list and add to total
    total_value = 0
    for rucksack in clean_rucksacks:
        half_index = int(len(rucksack)/2)
        first_compartment = rucksack[:half_index]
        second_compartment = rucksack[half_index:]
        common_letter = find_common_letter(
            first_compartment, second_compartment)
        total_value += rucksack_key_values[common_letter]
    print(total_value)


sum_value_common_letters()
