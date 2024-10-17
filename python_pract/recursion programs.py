'''def rec(num):
    if  num==0:
        return  
    print(num)
    rec(num+1)
num=-10
rec(num)'''


def arm(num,res=0):
    if num==0:
        return 0
    return (num%10)**digits+arm(num//10,digits)
num=153
digits=len(str(num))
print('armstrong' if arm(num,digits)==num else 'not arm')

'''def fact(num):
    if num==0:
        return 1
    return num*fact(num-1)
def strong(num):
    if num==0:
        return 0
    return fact(num)+strong(num//10)
num=145
print('strong' if strong(num)==num else 'not strong')'''

def special(num,fa=1):
    if fa==num//2+1:
        return 0
    if num%fa==0:
        return fa+special(num,fa+1)
    else:
        return special(num,fa+1)
num=12
print('special' if special(num)==num else 'not special')

def sq(num):
    if num==0:
        return 0
    return (num%10)**2+sq(num//10)
def happy(num):
    if num==0:
        return 0
    return 
        

