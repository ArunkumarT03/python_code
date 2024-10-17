'''def outer(func):
    def inner(n1,n2):
        print('operation')
        func(n1,n2)
    return inner
@outer
def add(n1,n2):
    print('operation')
    print(n1+n2)
add(n1=3,n2=4)'''

'''def outer(func):
    def inner(a,b):
        func(a,b)
    return inner
@outer
def add(a,b):
    print(a+b)
add(int(input('enter num1:')),int(input('enter num2:')))

def mul(a,b):
    print(a*b)
mul(a=2,b=6)

def div(a,b):
    print(a/b)
div(a=4,b=6)

def sub(a,b):
    print(a-b)
sub(a=4,b=7)'''
num1=int(input('enter num1:'))
num2=int(input('enter num2:'))
op=input('enter operation:') 
def calc():
    if op in 'add,mul,sub,div':
        if op=='add':
            print(num1+num2)
        elif op=='mul':
            print(num1*num2)
        elif op=='sub':
            print(num1-num2)
        elif op=='div':
            print(num1%num2)
        else:
            print(num1//num2)       
calc()


