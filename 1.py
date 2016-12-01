INPUT = 'R5, R4, R2, L3, R1, R1, L4, L5, R3, L1, L1, R4, L2, R1, R4, R4, L2, L2, R4, L4, R1, R3, L3, L1, L2, R1, R5, L5, L1, L1, R3, R5, L1, R4, L5, R5, R1, L185, R4, L1, R51, R3, L2, R78, R1, L4, R188, R1, L5, R5, R2, R3, L5, R3, R4, L1, R2, R2, L4, L4, L5, R5, R4, L4, R2, L5, R2, L1, L4, R4, L4, R2, L3, L4, R2, L3, R3, R2, L2, L3, R4, R3, R1, L4, L2, L5, R4, R4, L1, R1, L5, L1, R3, R1, L2, R1, R1, R3, L4, L1, L3, R2, R4, R2, L2, R1, L5, R3, L3, R3, L1, R4, L3, L3, R4, L2, L1, L3, R2, R3, L2, L1, R4, L3, L5, L2, L4, R1, L4, L4, R3, R5, L4, L1, L1, R4, L2, R5, R1, R1, R2, R1, R5, L1, L3, L5, R2'

NORTH = 0
EAST  = 1
SOUTH = 2
WEST  = 3

def xsteps():
    for step_str in INPUT.split(','):
        direction = step_str.strip()[0]
        num_blocks = int(step_str.strip()[1:])
        yield { 'direction': direction, 'num_blocks': num_blocks }

def get_locations():
    blocks_by_direction = [0, 0, 0, 0]
    current_direction = NORTH

    yield(0, 0)

    for step in xsteps():
        if step['direction'] == 'R':
            current_direction = (current_direction + 1) % 4
        else:
            current_direction = (current_direction + 3) % 4

        for i in xrange(step['num_blocks']):
            blocks_by_direction[current_direction] += 1
            yield (blocks_by_direction[NORTH] - blocks_by_direction[SOUTH],
                   blocks_by_direction[EAST]  - blocks_by_direction[WEST])

def calc_distance(location):
    return abs(location[0]) + abs(location[1])

def find_first_repeat_location(locations):
    visited = set()
    for location in locations:
        if location in visited:
            return location
        visited.add(location)
    return None

all_locations = [location for location in get_locations()]
last_location = all_locations[-1]
repeat_location = find_first_repeat_location(all_locations)

print 'Part 1: {}'.format(calc_distance(last_location))
print 'Part 2: {}'.format(calc_distance(repeat_location))
