'''n=input('enter a name:')
spaces=len(n)-1
for sv in range(len(n)-1,-1,-1):
    for sp in range(spaces):
        print(' ',end=' ')
    for ev in range(len(n)-1,sv-1,-1):
        print(n[ev],end=' ')
    spaces-=1
    print()'''

'''
def armstrong(num):
    res=0
    digits=len(str(num))
    while num!=0:
        rem=num%10
        res+=rem**digits
        num//=10
    return res
n=0
num=0
while n!=15:
      if armstrong(num)==num:
            print(num)
            n+=1
      num+=1
'''
'''n=int(input('enter a number:'))
spaces=n-1
for ch in range(1,n*2,2):
      for sp in range(spaces):
           print(' ',end=' ')
      for st in range(1,ch+1):
          if (ch==1 or ch==n*2-1):
              print('*',end=' ')
          else:
              if (st==1 or st==ch):
                  print('*',end=' ')
              else:
                  print(' ',end=' ')
      
      print()
      spaces-=1'''

'''m1=[[2,3,4],[4,5,6]]
m2=[[1,5,8],[6,8,0]]
if len(m1)==len(m2) and len(m1[0])==len(m2[0]):
      for r in range(len(m1)):
            for c in range(len(m1[0])):
                  m1[r][c]=m1[r][c]+m2[r][c]
      print(m1)
else:
      print('NP')'''
'''name=input('enter a name:').upper()
count=0
for ch in name:
      count+=ord(ch)-64
print(count)'''

'''d1={'a':20 ,'b':60,'c':70}
d2={'d':30 ,'a':40}
d3={}
for ch in d1.items():
    if ch[0] not in d3:
        d3[ch[0]]=[ch[1]]
    else:
        d3[ch[0]]+=[ch[1]]
for ch in d2.items():
    if ch[0] not in d3:
        d3[ch[0]]=[ch[1]]
    else:
        d3[ch[0]]+=[ch[1]]
print(d3)'''






