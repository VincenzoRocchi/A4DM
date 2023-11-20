import random

def new_array():
    A = [random.randint(1, 100) for _ in range(10)]
    return A

def swap_ind(A,a,b):
    A[a], A[b] = A[b], A[a]
    
def parent(A,i):
    if i == 0:
        print(f"key {A[i]} has no parent node")
    else:
        parent = (i-1)//2
        return parent
