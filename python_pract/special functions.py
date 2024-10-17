#lambda -lambda arguments:operations
#map()- map(function name,sequence)
#filter - filter(function name,sequence)
#reduce-from function import reduce
        #reduce(function name,sequence)

'''fun=lambda val1,val2,val3:val1*2+val2*3
print(fun(3,4,5))

print(list(map(lambda val:val*val,range(1,11))))

def sq(val):
    return val*val
print(list(map(sq,[2,4,6,8])))

#prime or not
def prime(num,f_count=0):
    for fa in range(1,num+1):
        if num%fa==0:
             f_count+=1     
    return f_count==2
        
      
print(list(map(prime,range(1,31))))

#add all digits
def add(num,res=0):
    while num!=0:
        rem=num%10
        res+=rem
        num//=10
    return res
print(list(map(add,[123,101,245,0,7])))

#patterns
print('\n'.join(list(map(lambda st:'* '*st,range(1,6)))))

print('\n'.join(list(map(lambda st:'* '*st,range(5,0,-1)))))

num=5
print('\n'.join(list(map(lambda sp,st:' '*sp + '*'*st,range(num-1,-1,-1),range(1,num+1)))))'''

'''num=6
print('\n'.join(list(map(lambda sp,st:' '*sp + '* ' *st,range(0,num),range(num,0,-1)))))'''

'''num=5
print('\n'.join(list(map(lambda sp,st:' '*sp + '*' *st,range(num-1,-1,-1),range(1,num*2,2)))))

num=5
print('\n'.join(list(map(lambda sp,st:' '*sp + '*' *st,range(0,num),range(num*2-1,0,-2)))))

num=9
print('\n'.join(list(map(lambda n:(str(n)+' ')*n,range(1,num+1)))))

num=10
print('\n'.join(list(map(lambda n:(str(num+1-n)+' ')*n,range(1,num+1)))))'''

#filter

'''def even(num):
    if num%2==0:
        return num
print(list(filter(even,range(1,10))))

def  arm(num,res=0):
    dup,power=num,len(str(num))
    while num!=0:  
       rem=num%10
       res+=rem**power
       num//=10
    return dup==res
print(list(filter(arm,range(1,31))))

def prime(num,f_count=0):
    for fa in range(1,num+1):
        if num%fa==0:
            f_count+=1
    return f_count==2 
print(list(filter(prime,range(1,30))))'''


#reduce
from functools import reduce
print(reduce(lambda e1,e2:e1+e2,[100,200,300,400]))



