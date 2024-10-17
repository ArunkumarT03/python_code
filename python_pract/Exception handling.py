'''L=[3,5,8,9]
try:
    res=0
    for val in range(len(L)+1):
        res+=L[val]
    print(res)
except IndexError as msg:
    print(f'error:{msg}')
except NameError as msg:
    print(f'error:{msg}')
except TypeError as msg:
    print(f'error:{msg}')'''

'''class arm(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg
num=122
digits=len(str(num))
try:
    dup=num
    res=0
    while num!=0:
        rem=num%10
        res+=rem**digits
        num//=10
    if dup!=res:
       raise arm('not armstrong')
    else:
       print('armstrong')
except arm as msg:
    print(f'error:{msg}')'''


'''class prime(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg
num=11
try:
    for fa in range(2,num//2+1):
        if num%fa==0:
            raise prime('not prime')
except prime as msg:
    print(f'error:{msg}')
else:
    print('prime')'''

class special(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg
num=7
try:
    res=0
    for fact in range(1,num//2+1):
        if num%fact==0:
            res+=fact
    if num!=res:
        raise special('not special')
    else:
        print('special')
except special as msg:
    print(f'error:{msg}')
    


