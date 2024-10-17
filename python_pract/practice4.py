'''s='racecar'
sind=0
eind=-1
while sind!=len(s)//2:
    if s[sind]!=s[eind]:
        print('not palindrome')
        break
    sind+=1
    eind-=1
else:
    print('palindrome')


s1='ababdbc'
for ind in range(len(s1)):
    if s1[ind]!=s1[ind+1]:'''
'''a=3
b=7
lcm=0
if a>b:
    lcm=a
else:
    lcm=b
while True:
    if lcm%a==0 and lcm%b==0:
        print(lcm)
        break
    else:
        lcm+=1
s='aabbbcdddd'
count=1
res=' '
s=s+' '
for ind in range(len(s)-1):
    if s[ind]==s[ind+1]:
        count+=1
    else:
        res=res+str(count)+s[ind]
        count=1
print(res)'''



'''s='4a3b1c'
res=' '
for ind in range(0,len(s),2):
    res+=int(s[ind])*s[ind+1]
print(res)'''
    
        
'''def leap(year):
    if year==0:
        return 0
    return (year%4==0 and year%400==0)or year%100!=0+leap(year//10)
year=2001
print('leap year' if leap(year) else 'not leap')

year=int(input('enter a year:'))
total_year=int(input('enter a total year:'))
def leap(year):
    if (year%4==0 and year%400==0)or year%100!=0:
        return True
    else:
        return False
for ch in range(0,total_year):
    if leap(year+ch):
        print('leap')
    else:
        print('not leap')'''

numbers=[1,2,3,4,512,12]
maxnum=0
for num  in numbers:
    if maxnum<num:
        maxnum=num
print(maxnum)

s='abbsha'
res=[]
for ch in s:
    if s[ch]>1:
        res+=s[ch]
    else:
        
print(res)
    



        
        
    
  
    
    

