'''num=5
stars=1
for lines in range(1,num+1):
    for st in range(stars):
        print('*',end=' ')
    print()
    stars+=1'''

'''num=5
stars=num+1
for lines in range(num+1,0,-1):
    for st in range (stars):
        print('*',end=' ')
    print()
    stars-=1'''

'''num=5
spaces=num-1
stars=1
for lines in range(1,num+1):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(stars):
        print('*',end=' ')
    print()
    spaces-=1
    stars+=2
for lines  in range(1,num+1):
    for sp in range(1,3):
        print(' ',end=' ')
    for st in range(1,num+1):
        print('*',end=' ')
    print()
    stars-=1
    spaces+=2
spaces=0
stars=num+4
for lines in range(1,num+1):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(stars):
        print('*',end=' ')
    print()
    spaces+=1
    stars-=2


    
num=5
stars=1
for lines in range(1,num+1):
    num1=1
    for st in range(stars):
        if lines==1 or lines==2 or lines==4:
            print('*',end=' ')
        else:
            print(num1,end=' ')
            num1+=1 
    print()
    stars+=1'''

'''num5=5
spaces=num5-1
stars=num5
for lines in range(num5,0,-1):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(stars):
        print('*',end=' ')
    print()
    spaces+=1
    stars-=1'''


''''num=7
spaces=num//2
stars=1
for lines in range(1,num//2+1):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(stars):
        print('*',end=' ')
    print()
    spaces-=1
    stars+=2

for lines in range(num//2+1):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(stars):
        print('*',end=' ')
    print()
    spaces+=1
    stars-=2


num=7
spaces=num//2
stars=1
for lines in range(num):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(stars):
        print('*',end=' ')
    print()
    
    if lines<num//2:
        spaces-=1
        stars+=2
    else:
        spaces+=1
        stars-=2'''

'''stars=1
spaces=0
for lines in range(0,7):
    for st in range(stars):
        print('* ',end=' ')
    print()
    if lines<7//2:
        stars+=1
    else:
        stars-=1
num=9
star=1
spaces=num//2
for lines in range(num):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(stars):
        print('*',end=' ')
    print()
    if lines<num//2:
        stars+=1
        spaces-=1
    else:
        stars-=1
        spaces+=1'''

num=input('enter a string:')
for lines in range(1,len(num)+1):
    for st in range(1,len(num)+1):
        if lines==st or lines+st==len(num)+1:
            print(num[st],end=' ')
        else:
            print(' ',end=' ')
    print()
        

'''num=7
for lines in range(1,num+1):
    for st in range(1,num+1):
        if lines==1 or lines==num:
            if st>=1 or st<=num:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        elif lines>=1 or lines<=num:
            if st==1 or st==num:
                print('*',end=' ')
            else:
                print(' ',end=' ')
    print()'''
  
        

        

    
''''if lines==1 or lines==num:
            if st==1 or st==num:
                print('*',end=' ')
            else:
                print(' ' ,end=' ')
        elif lines%2==0:
            if st%2==0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        elif lines==st//2:
            if st==lines//2:
                print('*',end=' ')
            else:
                print(' ',end=' ')
    print()'''
    
     
