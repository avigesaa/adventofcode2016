import md5

INPUT =  'wtnhxymk'

def get_hashes():
    i = 0
    while True:
        yield md5.new(INPUT + str(i)).hexdigest()
        i += 1

def get_hashes_with_prefix(prefix):
    for hash_str in get_hashes():
        if hash_str[0:5] == '00000':
            yield hash_str

def get_part1_password(length):
    password = ''
    for hash_str in get_hashes_with_prefix('00000'):
        password += hash_str[5]
        if len(password) >= length:
            break
    return password

def get_position_from_hash(hash_str, length):
    position = hash_str[5]
    if position.isalpha() or int(position) >= length:
        return None
    return int(position)

def get_part2_password(length):
    password = [None] * length
    chars_found = 0
    for hash_str in get_hashes_with_prefix('00000'):
        position = get_position_from_hash(hash_str, length)
        # Skip if invalid position
        if position is None:
            continue
        # If this isn't the first match for this position:
        if password[position] is not None:
            continue
        # Record password character:
        password[position] = hash_str[6]
        chars_found += 1
        if chars_found >= length:
            break
    return ''.join(password)

print 'Part 1: {}'.format(get_part1_password(length=8))
print 'Part 2: {}'.format(get_part2_password(length=8))
