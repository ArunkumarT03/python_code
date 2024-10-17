import re
'''
S='asdfghnmqwertg!@#$%^.\n'
print(re.findall('.',S))
print(re.findall('^s',S))
print(re.findall('^a',S))
print(re.findall('a$',S))
print(re.findall('n$',S))
print(re.findall('\n$',S))
'''
'''
D='h hi hhii hiii hey heyyy ey y'
print(re.findall('hi*',D))
print(re.findall('hi+',D))
print(re.findall('hi?',D))
print(re.findall('hi{3}',D))
'''
'''
A='agsdfagshERTYUIK'
print(re.findall('a|K',A))
print(re.findall('(as)',A))
print(re.findall('(a)(g)(s)',A))
'''
'''

#print(re.findall('\w',l))
#print(re.findall('\W',l))
#print(re.findall('\d',l))
#print(re.findall('\D',l))
#print(re.findall('\S',l))
#print(re.findall('\s',l))
#print(re.findall('\Aa',l))
#print(re.findall('6\Z',l))'''
l='sdfghjk!@#$%^&*() _>.zxcvbASDF123456a'

print(re.findall(r'\bs',l))
print(re.findall(r'a\B',l))


'''mob='+91-7897653421'
import re
if (re.match('[+]91(-| )[6789][0-9]{9}$',mob)):
    print('yes')'''








