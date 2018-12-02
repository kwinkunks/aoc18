# -*- coding: utf 8 -*-
"""
Advent of Code 2018
Day 1

For now, I'll try to use only built-in stuff.
"""


def part1():
    """Compute the cumulative sum of the diffs in the input.
    """
    freq = 0
    with open("input/day1.txt", 'r') as f:
        for d in f:
            freq += float(d)
    return freq


def part2(iter=0, freq=0, freqs=None):
    """Keep computing the cumulative sum of the numbers in the input,
    until we get the same sum twice. Keep count of the file iterations
    too, just for fun.

    Amazing, it's about 500x faster with sets, cf lists.
    """
    freqs = {0} if freqs is None else freqs

    with open("input/day1.txt", 'r') as f:
        data = f.readlines()

    for d in data:
        freq += float(d)

        if freq in freqs:
            break
        else:
            freqs.add(freq)
    
    else:
        freq, iter = part2(iter=iter+1, freq=freq, freqs=freqs)

    return freq, iter


if __name__ == "__main__":
    import sys
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        freq, iter = part2()
        print(f"Got {freq} after {iter} iterations.")
    else:
        print("Which part?")
