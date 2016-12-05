INPUT = """LRULLRLDUUUDUDDDRLUDRDLDDLUUDLDDLRDRLDRLLURRULURLDRLDUDURLURRULLDDDUDDRRRDLRRDDLDURDULLRDLLLDRDLLDULDUDLLDLDRUDLLDLDDRRRDRLUDRDDLUDRRDUDUDLLDDUUDLRDUDRRUDUDRULRULUDRUUDLDLULLRLDLDDRULLRLLLULUULDURURLUUULDURLDDDURRUUDURDDDULDLURLRDRURDRUDRLLDLDRUURLLLRDRURUDLRLUDULLDDURLRURDLRDUUURRLULRRLDDULUUURLRRRLLLLLURDDRUULUDRRRUDDLLULRRUULDRDDULRLDDDRRUULUDRLRUDURUUULDLDULUUDURLLLRRDDRDLURDDDLDDDLRDRLDDURLRLLRUDRRLLDDDDDURDURRDDULDULLRULDRUURDRRDUDDUDDDDRRDULDUURDRUDRLDULRULURLLRRDRDRDLUUDRRLRLDULDDLUUUUUURRLRRRULLDDDRLRDRRRRRRRDUUDLLUDURUDDLURRUDL
UDUUURRLRLLDDRRDRRRLDDDLURURLLUDDRLUUDRRRDURRLLRURDLLRRDUUDDDDRDRURRLLLLURDLRRRULLLDLLLUDDLDRRRDLDUUDDRDUDDUURDDLULULDURDURDRUULURURRURDUURUDRRUDRLLLLRRDLLDRDDRLLURDDDUDUDUDRUURDDRUURDLRUUDDRDUURUDDLLUURDLUDRUUDRRDLLUUURDULUULDUUDLLULUUDLUDRUUDUUURLDDDRLRURDDULLRDRULULUDLUUDDDUUDLDUUDRULLDUURDDRUDURULDRDDLRUULRRRDLDLRDULRDDRLLRRLURDLDRUDLRLUDLRLDLDURRUULRLUURDULDRRULLRULRDLLDLDUDRUDDUDLDDURDDDRDLUDRULRUULLRURLDDDRDLRRDRULURULDULRDLDULDURDRDRDRDURDRLUURLRDDLDDRLDDRURLLLURURDULDUDDLLUURDUUUDRUDDRDLDRLRLDURRULDULUUDDLRULDLRRRRDLLDRUUDRLLDLUDUULRDRDLRUUDLRRDDLUULDUULRUDRURLDDDURLRRULURR
LDURLLLRLLLUURLLULDLRLLDLURULRULRDUDLDDUDRLRRDLULLDDULUUULDRLDURURLURLDLRUDULLLULDUURLLRDLUULRULLLULRDRULUDLUUULDDURLUDDUDDRDLDRDRUDLUURDDLULDUULURLUULRDRDLURUDRUDLDRLUUUUULUDUDRRURUDRULDLDRDRLRURUUDRDLULLUDLLRUUDUUDUDLLRRRLDUDDDRDUDLDLLULRDURULLLUDLLRUDDUUDRLDUULLDLUUDUULURURLLULDUULLDLUDUURLURDLUULRRLLRUDRDLLLRRRLDDLUULUURLLDRDLUUULLDUDLLLLURDULLRUDUUULLDLRLDRLLULDUDUDRULLRRLULURUURLRLURRLRRRDDRLUDULURUDRRDLUDDRRDRUDRUDLDDRLRDRRLDDRLLDDDULDLRLDURRRRRULRULLUUULUUUDRRDRDRLLURRRRUULUDDUDDDLDURDRLDLLLLLRDUDLRDRUULU
URURRUUULLLLUURDULULLDLLULRUURRDRRLUULRDDRUDRRDUURDUDRUDDRUULURULDRLDRDDDLDLRLUDDRURULRLRLLLDLRRUDLLLLRLULDLUUDUUDRDLRRULLRDRLRLUUDDRRLLDDRULLLRLLURDLRRRRRLLDDRRDLDULDULLDLULLURURRLULRLRLLLLURDDRDDDUUDRRRDUUDDLRDLDRRLLRURUDUUUDLDUULLLRLURULRULRDRLLLDLDLRDRDLLLRUURDDUDDLULRULDLRULUURLLLRRLLLLLLRUURRLULRUUUDLDUDLLRRDDRUUUURRRDRRDULRDUUDULRRRDUUUUURRDUURRRRLDUDDRURULDDURDDRDLLLRDDURUDLLRURLRRRUDDLULULDUULURLUULRDLRDUDDRUULLLRURLDLRRLUDLULDRLUDDDRURUULLDLRLLLDULUDDRLRULURLRDRRDDLDLURUDDUUURRDDLUDDRDUULRRDLDRLLLULLRULRURULRLULULRDUD
RUDLLUDRRDRRLRURRULRLRDUDLRRLRDDUDRDLRRLLRURRDDLRLLRRURULRUULDUDUULDULDLRLRDLRDLRUURLDRLUDRRDDDRDRRRDDLLLRRLULLRRDDUDULRDRDUURLDLRULULUDLLDRUDUURRUDLLRDRLRRUUUDLDUDRRULLDURRDUDDLRURDLDRLULDDURRLULLRDDDRLURLULDLRUDLURDURRUDULDUUDLLLDDDUUURRRDLLDURRDLULRULULLRDURULLURDRLLRUUDDRRUDRDRRRURUUDLDDRLDRURULDDLLULULURDLDLDULLRLRDLLUUDDUDUDDDDRURLUDUDDDRRUDDLUDULLRDLDLURDDUURDLRLUUDRRULLRDLDDDLDULDUDRDUUULULDULUDLULRLRUULLDURLDULDRDLLDULLLULRLRD"""

PART_1_KEYPAD_GRAPH = {
    '1': { 'L': '1', 'R': '2', 'U': '1', 'D': '4' },
    '2': { 'L': '1', 'R': '3', 'U': '2', 'D': '5' },
    '3': { 'L': '2', 'R': '3', 'U': '3', 'D': '6' },
    '4': { 'L': '4', 'R': '5', 'U': '1', 'D': '7' },
    '5': { 'L': '4', 'R': '6', 'U': '2', 'D': '8' },
    '6': { 'L': '5', 'R': '6', 'U': '3', 'D': '9' },
    '7': { 'L': '7', 'R': '8', 'U': '4', 'D': '7' },
    '8': { 'L': '7', 'R': '9', 'U': '5', 'D': '8' },
    '9': { 'L': '8', 'R': '9', 'U': '6', 'D': '9' }
}

PART_2_KEYPAD_GRAPH = {
    '1': { 'L': '1', 'R': '1', 'U': '1', 'D': '3' },
    '2': { 'L': '2', 'R': '3', 'U': '2', 'D': '6' },
    '3': { 'L': '2', 'R': '4', 'U': '1', 'D': '7' },
    '4': { 'L': '3', 'R': '4', 'U': '4', 'D': '8' },
    '5': { 'L': '5', 'R': '6', 'U': '5', 'D': '5' },
    '6': { 'L': '5', 'R': '7', 'U': '2', 'D': 'A' },
    '7': { 'L': '6', 'R': '8', 'U': '3', 'D': 'B' },
    '8': { 'L': '7', 'R': '9', 'U': '4', 'D': 'C' },
    '9': { 'L': '8', 'R': '9', 'U': '9', 'D': '9' },
    'A': { 'L': 'A', 'R': 'B', 'U': '6', 'D': 'A' },
    'B': { 'L': 'A', 'R': 'C', 'U': '7', 'D': 'D' },
    'C': { 'L': 'B', 'R': 'C', 'U': '8', 'D': 'C' },
    'D': { 'L': 'D', 'R': 'D', 'U': 'B', 'D': 'D' },
}

def get_keycode(input, start_key, keypad_graph):
    current_key = start_key
    for line in input.split('\n'):
        for direction in line.strip():
            current_key = keypad_graph[current_key][direction]
        yield current_key

print 'Part 1: {}'.format(''.join(get_keycode(INPUT, '5', PART_1_KEYPAD_GRAPH)))
print 'Part 2: {}'.format(''.join(get_keycode(INPUT, '5', PART_2_KEYPAD_GRAPH)))
