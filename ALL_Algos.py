#insertion sort
def InsertionSort(A):
    
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while i >= 0 and key < A[i]:
            A[i+1] = key
            i -= 1
        A[i+1] = key
        
    return A

#selection sort
def SelectionSort(A):
    
    for i in range(len(A)):
        min_elem_index = i
        
        for j in range(1,len(A)):
            if A[j] < A[min_elem_index]:
                min_elem = j
        A[i], A[min_elem_index] = A[min_elem_index],A[i]
        
    return A

#MergeSort

def Merge(A,p,q,r):
    
    L = A[q,p]
    R = A[q,r]
    
    i = j = 0
    k = p
    
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1

    while j < len(r):
        A[k] = r[j]
        j += 1
        k += 1
        
def MergeSort(A,p,r):
    
    if p<r:
        q = (r-p)//2
        MergeSort(A,p,q)
        MergeSort(A,q,r)
        Merge(A,p,q,r)
        
#BubbleSort
def BubbleSort(A):
    
    for i in range(len(A)):
        for j in range(len(A)-1, i-1, -1):
            if A[j]< A[j-1]:
                A[j],A[j-1] = A[j-1],A[j]
    return A