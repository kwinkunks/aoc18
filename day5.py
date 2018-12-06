# -*- coding: utf 8 -*-
"""
Advent of Code 2018
Day 5 oh god
"""
RESULT = []

def scan(data):
    global RESULT
    scanned = ''
    for i, x in enumerate(data[:-1]):
        if data[i+1] == '0':
            RESULT.append(len(data[:-1]))
        if abs(ord(x) - ord(data[i+1])) == 32:
            scanned += data[i+2:]
            return scanned
        else:
            scanned += x
    return scanned

def wrapper(data):
    last_length = 0
    while True:
        scanned = scan(data)
        if len(scanned) == len(data):
            return data
        else:
            data = scanned
    return

def part1():
    """Part 1.
    """
    # Awful.
    global RESULT

    with open('input/day5t.txt', 'r') as f:
        data = f.read()

    RESULT = []
    wrapper(data+'0')
    print(RESULT)
    return

def part2():
    """Part 2.
    """
    global RESULT

    with open('input/day5t.txt', 'r') as f:
        data = f.read()

    RESULT = []
    for i in range(65, 65+26):
        stop = chr(i), chr(i+32)
        data_ = ''.join([c for c in data if c not in stop])
        wrapper(data_+'0')
    print(RESULT)
    return


if __name__ == "__main__":
    import sys
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
    else:
        print("Which part?")
