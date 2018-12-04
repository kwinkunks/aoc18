# -*- coding: utf 8 -*-
"""
Advent of Code 2018
Day 4
"""
import re
from collections import defaultdict

def argmax(l):
    """OK, so maybe not using NumPy is really stupid.
    """
    maxi = 0
    for i, e in enumerate(l):
        maxi = i if e > l[maxi] else maxi
    return maxi


def part1(part=1):
    """Part 1.

    Look, it's not pretty. I'm not proud. But it works.
    """
    # Read and sort the input data.
    with open('input/day4.txt', 'r') as f:
        data = f.readlines()
    data.sort()

    # Iterate over the data and build a dict of the guards
    # and their (asleep, awake) events.
    guards = defaultdict(list)
    g = e = t = timer = 0
    for event in data:
        guard = re.search(r'#(\d+?) ', event)
        if guard is None:
            e = 'asleep' if re.search(r'\] falls asleep', event) else 'awake'
            t = int(re.search(r'\:(\d\d)\]', event)[1])
            if e == 'asleep':
                timer = t
                state = 'asleep'
            elif (e == 'awake') and (state == 'asleep'):
                guards[g].append((timer, t))
                state = 'awake'
            else:
                state = 'awake'
        else:                
            g = int(guard[1])

    # Iterate over the guard events dict and build a list of
    # minute-logs for each guard.
    guard_mins = {}
    for guard, times in guards.items():
        mins = 60*[0]
        coll = []
        for start, stop in times:
            mins = [1 if start <= i < stop else 0 for i, m in enumerate(mins)]
            coll.append(mins)
        guard_mins[guard] = [sum(x) for x in zip(*coll)]

    # Get the laziest guard (and the minutes they're asleep).
    max_guard = max_mins = 0
    for guard, mins in guard_mins.items():
        if sum(mins) > max_mins:
            max_mins = sum(mins)
            max_guard = guard

    # Get the argmax of the minutes for the laziest guard.
    maxi = argmax(guard_mins[max_guard])

    if part == 1:
        return max_guard * maxi

    # Part 2.
    # Get the highest number of a minute for any guard.
    guard_max = {}
    for guard, mins in guard_mins.items():
        maxi = argmax(mins)
        maxx = max(mins)
        guard_max[guard] = (maxx, maxi, guard)
    maxx, maxi, maxx_guard = sorted(guard_max.values(), reverse=True)[0]

    if part == 2:
        return maxx_guard * maxi


def part2():
    """Part 2.
    """
    return part1(part=2)


if __name__ == "__main__":
    import sys
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
    else:
        print("Which part?")
