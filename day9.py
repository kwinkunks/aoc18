# -*- coding: utf 8 -*-
"""
Advent of Code 2018
Day X
"""

def argmax(l):
    """OK, so maybe not using NumPy is really stupid.
    """
    maxi = 0
    for i, e in enumerate(l):
        maxi = i if e > l[maxi] else maxi
    return maxi

def play_game(num_players, last_marble, logging=0, fast=True):
    marble = 1
    
    if fast:
        try:
            from blist import blist
        except ModuleNotFoundError as e:
            print("You need blist to use this feature.", e)
        marbles = blist([0])
    else:
        marbles = [0]

    current = 0
    players = [0 for _ in range(num_players)]
    player = 0
    turn = 0

    if logging > 1:
        print('-', marbles)

    while marble <= last_marble:

        if marble % 23:
            # Take turn normally
            insert = (current + 2) % len(marbles)
            marbles.insert(insert, marble)
            current = insert
        else:
            # Take 23 turn
            remove = current - 7
            score = marble + marbles.pop(remove)
            players[player] += score
            current = remove if remove > 0 else (remove + 1)
            if logging:
                print(players)

        # Show status
        if logging > 1:
            print(player+1, marbles, marbles[current])

        # Increment
        marble += 1
        player = (player + 1) % len(players) 
        turn += 1
        
    return max(players), argmax(players)+1

def part1():
    """Part 1.
    """
    return play_game(439, 71307)[0]


def part2():
    """Part 2.
    """
    return play_game(439, 7130700, fast=True)[0]


if __name__ == "__main__":
    import sys
    
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
