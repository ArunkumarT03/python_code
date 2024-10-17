#upper()
var='Today climate is cool'
print(var.upper())

#lower()
print(var.lower())

#swapcase
print(var.swapcase())

#title
print(var.title())

#capitalize
print(var.capitalize())

#startswith
var='Today weather is chill'
check='To'
print(var.startswith(check))

#endswith
var='today'
check='da'
print(var.endswith(check))
check='day'
print(var.endswith(check))

#split
var='happy or sad'
print(var.split(' '))
var='i will come tommorrow class'
print(var.split())
print(var.split('ll'))
print(var.split('o'))
print(var.split('o',1))

#index
var='we are goes our college next week'
print(var.index('e'))
print(var.index('e',2))
print(var.index('e',var.index('e',2,7))+1)
#print(var.index('y'))#error

#rindex
var='i am become a developer'
print(var.rindex('e'))
print(var.rindex('e',2,7))
print(var.rindex('o',0,21))
print(var.rindex('o',0,19))
#print(var.rindex('y'))

#find #rfind
var='today no python class'
print(var.find('e'))#get value -1
print(var.find('py'))
print(var.find('c',5,21))
print(var.find('c',-1,-22))
print(var.find('o',var.find('o',var.find('o')+1)+1))
print(var.find('o'))
print(var.rfind('y'))
print(var.rfind('y',0,5))
print(var.rfind('y',0,4))

#count
var='i should have participate in collage fest'
print(var.count('i'))
print(var.count('A'))
print(var.count('e',5))
print(var.count('e',5,37))
print(var.count('f'))

#isdigit
var='345'
print(var.isdigit())
print(len(var))
var='321e'
print(var.isdigit())

#isalpha
var='Arun'
print(var.isalpha())
var='arun23'
print(var.isalpha())

#isalnum
var='ak123'
print(var.isalnum())
var='ak112@'
print(var.isalnum())

#center
var='abcd'
print('abcd'.center(30))
var='abcde'
print('abcde'.center(30,'w'))
print('abcde'.center(3))
print('abcde'.center(5))
#print('abcde'.center(8,5))#it must be unicode charcter not in int

#format
var='should {} complete {} homework'
print('should {} complete {} homework'.format('i have','my'))
var='i can  my works'
print('i can {} my {} works'.format('do','all'))
var='now i {} studing {} banglore'
print('now i{0} studing {1} banglore'.format('am','in'))
print('now i{a} studing {b} banglore'.format(a='in',b='am'))

#fstring
name='arun'
place='kkdi'
print(f'{name} is from {place}')
a=10
b=15
print(f'{a}+{b}={a+b}')

#strip
s='abcdabcdabcd'
print(s.strip())
print(s.strip('cd'))
print(s.strip('ab'))
s='hello world eh'
print(s.strip('he'))
print(s.strip('h'))
#lstrip
print(s.lstrip('h'))
print(var)
#rstrip
var='hello hii eh'
print(var.rstrip('h'))

#replace
user='scott'
print(user)
print(user.replace('scott','Arun'))

print(s.lstrip('e'))
