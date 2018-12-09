# -*- coding: utf 8 -*-
"""
Advent of Code 2018
Day 8
"""

with open('input/day8.txt') as f:
    data = f.read()


def part1():
    """Part 1.
    """
    seq = [int(d) for d in data.split()]

    meta = []
    job_stack = []

    while seq:
        
        # Get a job off the stack.
        job = job_stack.pop()
        
        # Process the job if not empty.
        if job:
            for _ in range(job):
                meta.append(seq.pop(0))

        # Otherwise add jobs for self and children.
        else:
            c, m = seq.pop(0), seq.pop(0)
            
            # Add own job.
            job_stack.append(m)

            # Add empty child jobs.
            for _ in range(c):
                job_stack.append(0)

    return sum(meta)


def part2():
    """Part 2.
    """

    return


if __name__ == "__main__":
    import sys
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
    else:
        print("Which part?")
