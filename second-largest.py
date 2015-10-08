import random

def firstMax(elements, rivals):
    '''
    List, Dictionary -> Int
    Returns max number in elements
    (and stores rival of winning number in the rivals dictionary.
    This will be useful to find second largest number in the secondMax function.)
    '''
    n = len(elements)
    if n == 1:
        return elements[0]
    x = firstMax(elements[:n/2], rivals)
    y = firstMax(elements[n/2:], rivals)
    x, y = sorted([x, y])
    rivals[y] = rivals.get(y, []) + [x]    
    return y                               

def secondMax(elements):
    '''
    List -> Int
    Returns second maximum number in elements
    '''
    rivals = {}
    x = firstMax(elements, rivals)
    return max(rivals[x])          


elements = [random.randint(0, 10**7) for i in range(10**5)]
a = sorted(elements)[-2]
b = secondMax(elements)
# print b
try:
    assert a == b
    print 'Test passed'
except AssertionError:
    print a, b
    
    