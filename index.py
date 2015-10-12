import random

def indexFoo_helper(A):
    '''
    List -> Int
    return True if there exist 0 in A
    '''
    n = len(A)
    if n == 1:
        return A[0] == 0
    middle = A[n/2]
    if middle == 0:
        return True
    elif middle < 0:
        return indexFoo_helper(A[n/2:])
    else:
        return indexFoo_helper(A[:n/2])

def indexFoo(A):
    '''
    List, Int -> Boolean
    return True if there exists i such that A[i] = i,
    where i is index ranging from 0 to len(A)-1
    '''
    A = [A[i] - i for i in range(len(A))]
    return indexFoo_helper(A)



def test():
    A1 = [1, 2, 3, 4, 5, 6]
    A2 = [-100, -50, -10, -5, 0, 1, 2, 3, 4, 9, 100, 200, 300, 301]
    assert not indexFoo(A1)
    assert indexFoo(A2)

test()
