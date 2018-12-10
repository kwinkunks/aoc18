# -*- coding: utf 8 -*-
"""
Advent of Code 2018
Day 10
"""

import re

with open("input/day10.txt", 'r') as f:
    data = f.read()

def parse_data(data):
    pos = [(int(x), int(y)) for x, y in re.findall(r'position=< ?([-0-9]+), +?([-0-9]+)>', data)]
    vel = [(int(x), int(y)) for x, y in re.findall(r'velocity=< ?([-0-9]+), +?([-0-9]+)>', data)]
    return pos, vel

def mima(pos):
    minx, maxx = min(x for x, y in pos), max(x for x, y in pos)
    miny, maxy = min(y for x, y in pos), max(y for x, y in pos)
    return minx, maxx, miny, maxy

def get_size(pos):
    minx, maxx, miny, maxy = mima(pos)
    return (maxx-minx) * (maxy-miny)

def advance(pos, vel):
    return [(x+u, y+v) for (x, y), (u, v) in zip(pos, vel)]

def visualize(pos, chars='.#'):
    off, on = chars
    minx, maxx, miny, maxy = mima(pos)
    space = [(maxx-minx+1)*[off] for _ in range(maxy-miny+1)]
    for xi, yi in pos:
        space[yi-miny][xi-minx] = on

    result = ''
    for row in space:
        result += ''.join(row) + '\n'
    return result

def find_compact(pos, vel):
    time = 0
    while time < 100000:
        posnew = advance(pos, vel)
        if get_size(posnew) > get_size(pos):
            return pos, time
        pos = posnew
        
        time += 1

def part1():
    """Part 1.

    The key observation was that the 'image' with the
    words in it would be the smallest in area, so we
    only have to measure the size and find the one
    with a larger next image.
    """
    pos, vel = parse_data(data)
    best_position, time_ = find_compact(pos, vel)
    result = visualize(best_position, ' #')
    print(result)
    return


def part2():
    """Part 2.
    """
    pos, vel = parse_data(data)
    best_position, time = find_compact(pos, vel)
    return time


if __name__ == "__main__":
    import sys
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
    else:
        print("Which part?")
