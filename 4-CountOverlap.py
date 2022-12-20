import os

# Read input file.
current_path = os.path.dirname(__file__)
file = open(current_path + '/Inputs/4-input.txt')
assignments_raw = [line for line in file.readlines()]
file.close()

# Remove new lines from input
assignments = [assignment[:-1] for assignment in assignments_raw]


# Part 1 Number of total overlaps
def parse_pairs(assignment_pair):
    comma = assignment_pair.index(',')
    assignment_1 = assignment_pair[:comma]
    assignment_2 = assignment_pair[comma+1:]
    return assignment_1, assignment_2


def contained_within_start(num1, num2):
    # num1 in num2
    return num1 >= num2


def contained_within_end(num1, num2):
    # num1 in num2
    return num1 <= num2


def compare(assignment_pair_tuple):

    dash_in_pair1 = assignment_pair_tuple[0].index('-')
    pair1_start = int(assignment_pair_tuple[0][:dash_in_pair1])
    pair1_end = int(assignment_pair_tuple[0][dash_in_pair1+1:])

    dash_in_pair2 = assignment_pair_tuple[1].index('-')
    pair2_start = int(assignment_pair_tuple[1][:dash_in_pair2])
    pair2_end = int(assignment_pair_tuple[1][dash_in_pair2+1:])

    return ((contained_within_start(pair1_start, pair2_start)
            and contained_within_end(pair1_end, pair2_end)) or (contained_within_start(pair2_start, pair1_start)
                                                                and contained_within_end(pair2_end, pair1_end)))


def count_num_overlaps(assignments):
    total_overlaps = 0
    for pairs in assignments:
        found_overlap = compare(parse_pairs(pairs))
        if found_overlap:
            total_overlaps += 1
    return total_overlaps


print(count_num_overlaps(assignments))

# Part 2 Number of partial overlaps


def find_partial_overlap(num1, range_start, range_end):
    return range_start <= num1 <= range_end


def compare_partial(assignment_pair_tuple):

    dash_in_pair1 = assignment_pair_tuple[0].index('-')
    pair1_start = int(assignment_pair_tuple[0][:dash_in_pair1])
    pair1_end = int(assignment_pair_tuple[0][dash_in_pair1+1:])

    dash_in_pair2 = assignment_pair_tuple[1].index('-')
    pair2_start = int(assignment_pair_tuple[1][:dash_in_pair2])
    pair2_end = int(assignment_pair_tuple[1][dash_in_pair2+1:])

    return (find_partial_overlap(pair1_end, pair2_start, pair2_end) or
            find_partial_overlap(pair2_end, pair1_start, pair1_end))


def count_partial_num_overlaps(assignments):
    total_overlaps = 0
    for pairs in assignments:
        found_overlap = compare_partial(parse_pairs(pairs))
        if found_overlap:
            total_overlaps += 1
    return total_overlaps


print(count_partial_num_overlaps(assignments))
