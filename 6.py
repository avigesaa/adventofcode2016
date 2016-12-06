from collections import defaultdict
from operator import itemgetter

INPUT_FILE = '6.in'

def read_messages():
    with open(INPUT_FILE, 'r') as input_file:
        for line in input_file:
            yield line.strip()

def get_character_counts_by_position(messages):
    counts_by_position = defaultdict(lambda: defaultdict(int))
    for message in messages:
        for idx, c in enumerate(message):
            counts_by_position[idx][c] += 1
    return counts_by_position

def get_most_frequent_character(character_counts):
    return max(character_counts.iteritems(), key=itemgetter(1))[0]

def get_least_frequent_character(character_counts):
    return min(character_counts.iteritems(), key=itemgetter(1))[0]

def get_error_corrected_message(messages, selector_fn):
    counts_by_position = get_character_counts_by_position(messages)
    message_length = len(counts_by_position)
    corrected_message = ''
    for i in xrange(message_length):
        corrected_message += selector_fn(counts_by_position[i])
    return corrected_message

messages = list(read_messages())

print 'Part 1: {}'.format(get_error_corrected_message(messages, get_most_frequent_character))
print 'Part 2: {}'.format(get_error_corrected_message(messages, get_least_frequent_character))
