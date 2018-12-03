# -*- coding: utf 8 -*-
"""
Advent of Code 2018
Day 2
"""


def part1():
    """Do part 1.
    """
    twice = 0
    thrice = 0

    with open('input/day2.txt', 'r') as f:
        for d in f:
            counts = {chr(c):d.count(chr(c)) for c in range(97,123)}
            twice += 1 if 2 in counts.values() else 0
            thrice += 1 if 3 in counts.values() else 0

    return twice * thrice


def part2():
    """Look for pairs of 'words' in which exactly one character
    differs. Check as few pairs as possible.
    """
    done = []
    with open('input/day2.txt', 'r') as f:
        for w1 in f:
            w1 = w1.strip()
            for w2 in done:
                match = [x != y for x, y in zip(w1, w2)]
                if sum(match) == 1:
                    # I don't like this.
                    return "".join(x for x, y in zip(w1, w2) if x == y)
            done.append(w1)
    return None


if __name__ == "__main__":
    import sys
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print("First match:", part2())
    else:
        print("Which part?")
