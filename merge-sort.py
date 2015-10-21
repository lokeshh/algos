def mergeSort(A):
    '''
    List -> List
    returns the sorted A
    '''
    n = len(A)
    
    # Base case
    if n == 0 or n == 1:
        return A
        
    # Split subroutine
    left = A[:n/2]
    right = A[n/2:]
    # Sort the left and right arrays
    left = mergeSort(left)
    right = mergeSort(right)
    
    # Merge subroutine
    i, j = 0, 0
    res = []
    for k in range(n):
        if j >= len(right) or (i < len(left) and  left[i] <= right[j]):
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    return res
            
    