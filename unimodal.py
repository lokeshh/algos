import random

def maxUni(elts):
    '''
    List -> elts
    produces maximum element in 'elts' array of unimodal elements
    '''
    n = len(elts)
    if n == 1:
        return elts[0]
    middle1 = elts[n/2-1]
    middle2 = elts[n/2]
    if middle1 < middle2:
        return maxUni(elts[n/2:])
    else:
        return maxUni(elts[:n/2])

def test():
    elts1 = [random.randint(0, 10**7) for i in range(10**5)]
    elts2 = [random.randint(0, 10**7) for i in range(10**5)]
    elts = sorted(elts1) + sorted(elts2, reverse = True)
    assert max(elts) == maxUni(elts)

test()
