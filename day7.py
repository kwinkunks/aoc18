# -*- coding: utf 8 -*-
"""
Advent of Code 2018
Day X
"""
import re


with open('input/day7.txt') as f:
    data = f.read()


def part1():
    """Part 1.

    Just keep asking, "Can I do this yet?"
    """
    todo = [chr(x+65) for x in range(26)]
    pairs = re.findall(r'Step ([A-Z]) .* step ([A-Z])', data)
    pairs.sort()

    done = ''
    while todo:
        for a in todo:
            for x, y in pairs:
                if (a == y) and (x not in done):
                    break
            else:
                todo.remove(a)
                done += a
                break

    return done


def part2():
    """Part 2.

    Same idea as before, but tick a clock and check what each
    worker is doing at each time step. If idle, assign the next
    task.

    Can't just use sequence determined before because some tasks
    can happen in parallel.
    """
    pairs = re.findall(r'Step ([A-Z]) .* step ([A-Z])', data)
    pairs.sort()

    offset = 4
    no_workers = 5
    no_chars = 26

    todo = [chr(x+65) for x in range(no_chars)]
    done = []
    doing = []

    workers = [list() for w in range(no_workers)]

    for t in range(1000000):
        
        if (not todo) and (not doing):
            # Got an Obi Wan error.
            return len(workers[-1]) - 1
        
        # Visit each worker and assign tasks.
        for w in workers:
            working = False
            
            if w:
                p = w[-1]
                if p != '.':
                    if w.count(p) < (ord(p) - offset):
                        working = True
                        w.append(p)
                        continue
                    else:
                        working = False
                        doing.remove(p)
                        done.append(p)
                else:
                    working = False
            else:
                working = False
            
            # Worker is idle so find a task.
            for a in todo:
                
                for x, y in pairs:
                    
                    if (a == y) and (x not in done):
                        #w.append('.')
                        break

                else:
                    # We can do task a...
                    if a not in doing:  # then start it
                        todo.remove(a)
                        doing.append(a)
                        w.append(a)
                        working = True

                    break

            if (not working) and (todo or doing):
                w.append('.')

    return


if __name__ == "__main__":
    import sys
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
    else:
        print("Which part?")
