#list comphrehension
#for loop :l1=[value for loop]
#if condition:l2=[value for loop if condition]
#if condition else:l3=[value if condi else value for loop]
'''
str_='welcome'
l=[]
for ch in str_:
    l.append(ord(ch))
print(l)

print([ord(ch)for ch in str_])

str1_='hello welcome to python'.split()

l1=[ch[0]for ch in str1_]
print(l1)'''

'''str2='welcome to python'
l2=([(word,len(word) for word in str2)])
print(l2)'''


'''l3=[num**2 for num in range(1,20)]
print(l3)

l4=[num for num in range(1,30)if num%2==0]
print(l4)

names=['amazing','lawra','steve','bill','james','alex','ajith']
l5=[name for name in names if name[0] in 'aeiouAEIOU']
print(l5)

languages=['python','php','java','js','ruby','r','c']
l6=[language for language in languages if language[0] in 'p']
print(l6)

names={'apple','google','yahoo','gmail','flipkart','instagram','microsoft'}
l7=[name for name in names if len(name)<6]
print(l7)
l8=[name for name in names if len(name)%2==0]
print(l8)

#third syntax
values={'Royalenfield','selario','ktm','Bmw','java','range'}
l9=[value [::-1] if len(value)%2!=0 else value for value in values]
print(l9)

strings=['hello','kalim','arun']
print([strings[st].upper() if st%2==0 else strings[st].lower() for st in range(len(strings))])

l10=[(num,'even')if num%2==0 else (num,'odd' )for num in range(1,11)]
print(l10)

#kalim
s=input("enter:").split()
print([(word,len(word)) for word in s])

print([val*val for val in range(1,21)])

print([val for val in range(1,21) if val%2==0])

print(['even' if num%2==0 else 'odd' for num in range(20,51)])

print([num*num if num%2==0 else num/num for num in range(1,21)])

print(['small' if num<5 else 'large' for num in range(20,51)])

print([0 if num<0 else num for num in [-5,-3,1,7,-2]])

print({val**3 for val in range(1,5)})

print({val for val in range(20,51) if val%2!=0})

s='hello'
print({ch for ch in s})

s='hello'
print({ch.upper() for ch in s})

sentence='this is a word.this is a only word'
print({ch for ch in sentence.split()})
'''
print({val  for val in range(2,23) if val%3==0 or val%5==0})
