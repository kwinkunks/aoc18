# -*- coding: utf 8 -*-
"""
Advent of Code 2018
Day 6
"""
def argmax(l):
    maxi = 0
    for i, e in enumerate(l):
        maxi = i if e > l[maxi] else maxi
    return maxi

def argmin(l):
    mini = 0
    for i, e in enumerate(l):
        mini = i if e < l[mini] else mini
    return mini

def choose_min(inlist):
    """See if the location qualifies according to the rules.
    
    >>> choose_min([3,4,6,3,1,4])
    True
    """
    l = inlist.copy()
    minn = min(l)
    if minn == 0:
        return False
    mini = argmin(l)
    l.remove(min(l))
    if minn in l:
        return False
    return True

def part1():
    """Part 1.
    """
    with open('input/day6.txt', 'r') as f:
        data = f.read()

    coords = [list(map(int, d.split(','))) for d in data.split('\n')]
    xy = [[c[0] for c in coords], [c[1] for c in coords]]
    maxx, maxy = max(xy[0]), max(xy[1])

    # Make the space.
    space = [(maxy+2)*[0] for x in range(maxx+2)]

    for i, row in enumerate(space):
        for j, _ in enumerate(row):
            dists = [abs(y-i) + abs(x-j) for _, (x, y) in enumerate(coords)]
            space[i][j] = argmin(dists) if choose_min(dists) else -1
    return

    counts = [1 for c in coords]
    for row in space:
        for e in row:
            counts[e] += 1 if e >= 1 else 0

    edge = space[0] + space[-1] + [r[0] for r in space] + [r[-1] for r in space]
    infinite = set(e for e in edge if e >= 0)

    large = [x if i not in infinite else 0 for i, x in enumerate(counts)]
    largest = max(large)
    largi = argmax(large)

    return largi


def part2():
    """Part 2.
    """
    with open('input/day6.txt', 'r') as f:
        data = f.read()

    coords = [list(map(int, d.split(','))) for d in data.split('\n')]
    xy = [[c[0] for c in coords], [c[1] for c in coords]]
    maxx, maxy = max(xy[0]), max(xy[1])

    # Make the space.
    space = [(maxy+2)*[0] for x in range(maxx+2)]

    for i, row in enumerate(space):
        for j, _ in enumerate(row):
            space[i][j] = sum(abs(y-i) + abs(x-j) for _, (x, y) in enumerate(coords))

    close = 0
    for row in space:
        for e in row:
            close += 1 if e < 10000 else 0

    return close


if __name__ == "__main__":
    import sys
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
    else:
        print("Which part?")
