# -*- coding: utf 8 -*-
"""
Advent of Code 2018
Day X
"""

def argmax2d(list2d):
    maxi = (0, 0)
    for i, r in enumerate(list2d):
        for j, e in enumerate(r):
            maxi = (i, j) if e > list2d[maxi[0]][maxi[1]] else maxi
    return maxi

def max2d(list2d):
    r, c = argmax2d(list2d)
    return list2d[r][c]

class Grid(list):
    
    def __init__(self, shape, serial_number):
        """shape is (x-size, y-size) and not (rows, columns).
        
        Bah, a Grid should really be empty. Then I could use
        one for the subgrids too. Damn.
        """

        w, h = [int(i) for i in shape]
        super(Grid, self).__init__([w*[0] for _ in range(h)])

        for y, row in enumerate(self):
            for x, c in enumerate(row):
                rackid = x + 1 + 10
                power = rackid * (y + 1)
                power += serial_number
                power *= rackid
                power = power % 1000 // 100
                power -= 5
                self[y][x] = power

    def read(self, x, y):
        return self[y - 1][x - 1]

    @property
    def shape(self):
        return self.x, self.y

    @property
    def x(self):
        return len(self[0])

    @property
    def y(self):
        return len(self)
    
    def traverse(self, n):
        """Traverse subsquares."""
        for y in range(self.y - n + 1):
            for x in range(self.x - n + 1):
                yield x, y, [r[x:x+n] for r in self[y:y+n]]
          
    @staticmethod
    def power(grid):
        return  sum(sum(r) for r in grid)

    def powergrids(self, n):
        """This should really be a Grid.
        """
        w, h = self.x - n + 1, self.y - n + 1
        subgrids = [w*[0] for _ in range(h)]
        for x, y, subgrid in self.traverse(n):
            subgrids[y][x] = self.power(subgrid)
        return subgrids


def part1():
    """Part 1.
    """
    g = Grid(shape=(300, 300), serial_number=5153)
    powergrid = g.powergrids(3)
    max_row, max_col = argmax2d(powergrid)
    return f"Max x, y = {max_col+1}, {max_row+1}"


def part2(n_max):
    """Part 2.
    """
    g = Grid(shape=(300, 300), serial_number=5153)
    maxp = 0
    maxn = 0

    for n in range(n_max):
        powergrid = g.powergrids(n)
        maxp_ = max2d(powergrid)
        print(maxp_)
        if maxp_ > maxp:
            maxp = maxp_
            maxn = n

    powergrid = g.powergrids(maxn)
    max_row, max_col = argmax2d(powergrid)
    return f"Max x, y, n = {max_col+1},{max_row+1},{maxn}"

if __name__ == "__main__":
    import sys
    if sys.argv[1] == '1':
        print(part1())
    else:
        print(sys.argv)
        print(part2(int(sys.argv[2])))
