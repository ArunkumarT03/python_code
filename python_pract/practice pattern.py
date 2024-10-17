
'''spaces=1
stars=0
for line in range(1,num+1):
    for sp in range(spaces):
        print(' ' ,end=' ')
    for st in range(stars):
        print('*',end=' ')
    print()
    spaces-=1
    stars+=1'''
'''num=6
spaces=2
for line in range(1,num+1):
    if line<=2 or line>4:
        for st in range(num):
            print('*',end=' ')
    else:
        for sp in range(spaces):
            print(' ',end=' ')
        for st in range(2):
            print('*',end=' ')
    print()

    

num=6
for line in range(1,num+1):
    if line<=4:
        for st in range(2):
            print('*',end=' ')
    else:
        for st in range(num):
            print('*',end=' ')
    print()'''



'''num=5
stars=num
for line in range(1,num+1):
    for st in range(stars):
        print('*',end=' ')
    print()
    stars-=1


n=input('enter a string:')
for line in range(len(n)):
    for st in range(len(n)):
        if  line==st or line==n-1-st:
            print(n[st],end=' ')
        else:
            print(' ',end=' ')
    print()'''

n=5
spaces=n-1
for ch in range(1,n*2,2):
      for sp in range(spaces):
           print(' ',end=' ')
      for st in range(1,ch+1):
          if ch==1 or ch==n*2-1:
              print('*',end=' ')
          else:
              if st==1 or st==ch:
                  print('*',end=' ')
              else:
                  print(' ',end=' ')
      
      print()
      spaces-=1

class arm(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return  self.msg
num=122
digits=len(str(num))
try:
    dup=num
    res=0
    while num!=0:
        rem=num%10
        res+=rem**digits
        num//=10
except arm as msg:
    print(f'error:{msg}')
if dup!=res:
    raise arm('not armstrong')
else:
    print('armstrong')
   
