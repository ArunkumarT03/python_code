#if
#if condition is only taken true values
num=20
var=25
if num%2==0:
    print('it is even')
    if var%2!=0:
        print('it is odd')

#elif
#whenever we can take elif condition first must should have if condition
num1=10
num2=20
num3=35
num4=58
if num1%2!=0:
    print('it is odd')
elif num2%2!=0:
    print('it is odd')
elif num3%2==0:
    print('it is odd')
elif num4%2==0:
    print('it is even')

#else

num1=123
if num1%2==0:
    print('its even')
else:
    print('its odd')

#if elif else
var1=12
var2=14
var3=16
if var1>var2:
    if var1>var2:
        print('var1 is great')
    else:
        print('var2 is grate')
else:
    if var2>var3:
        print('var2 is great')
    else:
        print('var3 is great')
       
var1=120
var2=320
var3=765
var4=458
if var1>var2:
    if var1>var2:
        print('var1')
    if var1>var3:
        print('var1')
    if var1>var4:
        print('var1')
elif var2>var3:
    if var2>var3:
        print('var2')
    if var2>var4:
        print('var2')
elif var4>var3:
    if var4>var3:
        print('var4')
else:
    print('var3')

var11=550
var12=420
var13=658
var14=789
if var11%2!=0:
    print('its even')
elif var12%2==0:
    print('even')
elif var13%2==0:
    print('even')
elif var14%2!=0:
    print('even')
else:
    print('its odd')

var21=120
var22=150
var23=567
var24=221
if var21>var22 and var21>var23 and var21>var24:
    print('var21 is great')
elif var22>var23 and var22>24:
    print('var22 is great')
elif var23>24:
    print('var23 is great')
else:
    print('var24 is great')
