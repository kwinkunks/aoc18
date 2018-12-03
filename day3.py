# -*- coding: utf 8 -*-
"""
Advent of Code 2018
Day 3
"""
import re
import pickle

def part1():
    """This would be a lot easier with NumPy.
    
    We're looking to create a 2D array, or list of lists, in which we'll
    record each claim as a bunch of ones. We'll add them up as we go.
    """
    # Read the data file.
    data = []
    max_x = max_y = 0
    with open("input/day3.txt", 'r') as f:
        for line in f:
            claim = {}
            claim['i'] = int(re.search(r'^#([0-9]+) ', line)[1])
            claim['x'] = int(re.search(r'@ ([0-9]+),', line)[1])
            claim['y'] = int(re.search(r',([0-9]+):', line)[1])
            claim['w'] = int(re.search(r': ([0-9]+)x', line)[1])
            claim['h'] = int(re.search(r'x([0-9]+)$', line)[1])
            max_x = max(claim['x'], max_x)
            max_y = max(claim['y'], max_y)
            max_w = max(claim['w'], max_y)
            max_h = max(claim['h'], max_y)
            data.append(claim)

    # Save the data for part 2.
    with open('day3_data.pkl', 'wb') as f:
        pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
    
    # Make an empty 'fabric'.
    fabric = [[0 for x in range(max_x+max_w+1)] for y in range(max_y+max_h+1)]

    # Visit each claim and change the fabric to count overlaps.
    for claim in data:
        for y, row in enumerate(fabric[claim['y']:claim['y']+claim['h']]):
            for x, _ in enumerate(row[claim['x']:claim['x']+claim['w']]):
                fabric[claim['y']+y][claim['x']+x] += 1

    # Save the fabric.
    with open('day3_fabric.pkl', 'wb') as f:
        pickle.dump(fabric, f, protocol=pickle.HIGHEST_PROTOCOL)

    # Count the overlaps.
    overlaps = 0
    for row in fabric:
        overlaps += len([x for x in row if x > 1])

    return overlaps


def part2():
    """Which claim overlaps no other?

    This is fairly easy now... just have to traverse once more, this
    time adding up the values of each 'pixel' in each claim. If the
    sum is the same as the area, then it's full of ones.

    Can't believe I'm using for...else again!
    """
    with open('day3_data.pkl', 'rb') as f:
        data = pickle.load(f)

    with open('day3_fabric.pkl', 'rb') as f:
        fabric = pickle.load(f)

    for claim in data:
        summ = 0
        for y, row in enumerate(fabric[claim['y']:claim['y']+claim['h']]):
            for x, _ in enumerate(row[claim['x']:claim['x']+claim['w']]):
                summ += fabric[claim['y']+y][claim['x']+x]
        if summ == claim['h'] * claim['w']:
            result = claim['i']
            break
    else:
        result = None

    return result



if __name__ == "__main__":
    import sys
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
    else:
        print("Which part?")
