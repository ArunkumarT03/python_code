'''#recursion
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci_recursive(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence
n = 10  
print(fibonacci_recursive(n))'''

#function
def fibonacci_iterative(n):
    if n <= 0:
        return []
    elif n == 1:
        return 0
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence
n = 6
print(fibonacci_iterative(n))


def distance(L):
    first=[]
    second=[]
    for index,string in enumerate(L):
        if string in first:
            last

















