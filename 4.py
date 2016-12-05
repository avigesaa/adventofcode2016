import re
from operator import itemgetter

INPUT_FILE = '4.in'
ROOM_SPEC_PATTERN = re.compile('(?P<encrypted_name>.*)-(?P<sector_id>.*)\[(?P<checksum>.*)\]')

def parse_room_spec(line):
    match = ROOM_SPEC_PATTERN.match(line)
    return match.groupdict() if match is not None else None

def get_room_specs():
    with open(INPUT_FILE, 'r') as input_file:
        for line in input_file:
            yield parse_room_spec(line)

def get_character_counts(s):
    counts = {}
    for character in s:
        if not character.isalpha():
            continue
        if character in counts:
            counts[character] += 1
        else:
            counts[character] = 1
    return counts

def calculate_checksum(room_spec):
    name = room_spec['encrypted_name']
    counts = get_character_counts(name).items()
    counts = sorted(counts, key=itemgetter(0))
    counts = sorted(counts, key=itemgetter(1), reverse=True)
    return ''.join(map(itemgetter(0), counts)[:5])

def is_real_room(room_spec):
    return calculate_checksum(room_spec) == room_spec['checksum']

def get_sector_id(room_spec):
    return int(room_spec['sector_id'])

def get_unencrypted_room_name(room_spec):
    name = ''
    sector_id = get_sector_id(room_spec)
    is_odd_sector_id = (sector_id % 2) == 1
    for c in room_spec['encrypted_name']:
        if c.isalpha():
            name += chr(((ord(c) - ord('a') + sector_id) % 26) + ord('a'))
        elif c == '-':
            name += ' ' if is_odd_sector_id else '-'
        elif c == ' ':
            name += '-' if is_odd_sector_id else ' '
    return name

def is_northpole_object_storage(room_spec):
    return get_unencrypted_room_name(room_spec) == 'northpole object storage'

real_rooms = filter(is_real_room, get_room_specs())
north_pole_storage_rooms = filter(is_northpole_object_storage, real_rooms)

print 'Part 1: {}'.format(sum(get_sector_id(room_spec) for room_spec in real_rooms))
print 'Part 2: {}'.format(get_sector_id(north_pole_storage_rooms[0]))
