'''s=eval(input('enter a list:'))
count=0
L=[11]
for i in s:
    if i in L:
        count+=1
print(count)'''

'''L=[[1,2],[2,5],[3,4],[4,1]]
L1=sorted(L,key=lambda L:L[1])
print(L1)'''

'''def flat(L):
    for ele in L:
        if type(ele)==int:
            res.append(ele)
        else:
            flat(ele)
    return res
L=[1,2,[3,4],5,[6,7],8]
res=[]
print(flat(L))


def i2b(num,pos=1,res=0):
    while num!=0:
        rem=num%2
        res+=rem*pos
        pos*=10
        num//=2
    return res
num=25
print(i2b(num))

def b2i(num,power=1,res=0):
    while num!=0:
        rem=num%10
        res+=rem*power
        power*=2
        num//=10
    return res
num=11001
print(b2i(num))
        

def fact(num,val):
    if val==num:
        return num
    return val*fact(num,val+1)
num=5
val=1
print(fact(num,val))'''

def divide(a, b):
    print(f"Dividing {a} by {b}")
    return a / b

result = divide(10, 2)
print(f"Result: {result}")


#rev string iterativly and recursivly
def rev(s):
    res=' '
    for ch in s:
        res=ch+res
    return res
s='hello'
print(rev(s))

def rec(str1):
    if len(str1)==0:
        return ""
    return rec(str1[1:])+str1[0]
str1='hello'
print(rec(str1))


#breadth-first search
from collections import deque

def bfs(graph, start_node):
    visited = set()             
    queue = deque([start_node])  
    
    while queue:
        node = queue.popleft()  
        if node not in visited:
            print(node)          
            visited.add(node)    
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', ],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')


#dictionary sorted
data = {'banana': 3, 'apple': 4, 'orange': 2, 'mango': 5}
s1 = dict(sorted(data.items()))
print(s1)























    


























