import random

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def setLocX(self, i):
        '''
        Stores the location of point in Px
        '''
        self.locx = i
    def setLocY(self, j):
        '''
        Stores the location of point in Py
        '''
        self.locy = j
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

def QuickSortPreprocess(P):
    '''
    P:  list of points; points are represented as (x, y)
    Px: list of points, sorted by x
    Py: list of points, sorted by y
    Returns Px and Py from P
    ###
    The function does the following preprocessing:
    1. It converts all points to point objects
    2. Px and Py contains all points sorted in x and y
    3. Every point remember its position in Px and Py
    '''
    # Convert all points to point objects
    P = [Point(p[0], p[1]) for p in P]
    Px = sorted(P, key = lambda p: p.x)
    Py = sorted(P, key = lambda p: p.y)
    # Iterate over all points in Px and Py and make them remember their position
    for i in range(len(P)):
        # Make point in Px remember its position in x
        Px[i].setLocX(i)
        Py[i].setLocY(i)
    return Px, Py

def test():
    # A demo to obtain Qx, Qy, Rx and Ry from Px and Py in linear time
    P = [(random.randint(0, 10), random.randint(0, 10)) for i in range(10)]
    print P

    # Obtain Qx and Rx in linear time
    Px, Py = QuickSortPreprocess(P)
    Qx = Px[:5]
    Rx = Px[5:]

    # This is the expected result
    expQy = sorted(Qx, key = lambda p: p.y)
    expRy = sorted(Rx, key = lambda p: p.y)

    # Obtain Qy and Ry in linear time
    Qy = []
    Ry = []
    for p in Py:
        if p.x <= Qx[4].x:
            Qy.append(p)
        else:
            Ry.append(p)

    assert Qy == expQy
    assert Ry == expRy

test()
