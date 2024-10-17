num1=int(input('enter num1:'))
num2=int(input('enter num2:'))
op=input('enter operation:') 
def calc():

    #if op in 'add,mul,div,sub':
        if op=='add':
            print(num1+num2)
        elif op=='mul':
            print(num1*num2)
        elif op=='div':
            print(num1/num2)
        elif op=='sub':
            print(num1-num2)
        else:
            print('check once')
calc()
                
