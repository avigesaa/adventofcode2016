import re

INPUT_FILE = '3.in'

def is_invalid_triangle(triangle):
    sorted_lengths = sorted(triangle)
    return sorted_lengths[0] + sorted_lengths[1] > sorted_lengths[2]

def parse_triangle_lengths(line):
    return [int(s) for s in re.split('\W+', line.strip())]

def read_input_grid():
    rows = []
    with open(INPUT_FILE, 'r') as input_file:
        triangles = []
        for line in input_file:
            rows.append(parse_triangle_lengths(line))
    return rows

def get_part1_triangles():
    return read_input_grid()

def get_part2_triangles():
    rows = read_input_grid()
    for i in xrange(0, len(rows), 3):
        yield [rows[i][0], rows[i+1][0], rows[i+2][0]]
        yield [rows[i][1], rows[i+1][1], rows[i+2][1]] 
        yield [rows[i][2], rows[i+1][2], rows[i+2][2]]

valid_part1_triangles = filter(is_invalid_triangle, get_part1_triangles())
valid_part2_triangles = filter(is_invalid_triangle, get_part2_triangles())

print 'Part 1: {}'.format(len(valid_part1_triangles))
print 'Part 2: {}'.format(len(valid_part2_triangles))
