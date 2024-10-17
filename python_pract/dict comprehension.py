
d1_={num:num**2 for num in range(1,5)}
print(d1_)

details={'name':'mani','age':21,'city':'karaikudi'}
print({word.upper():val for word,val in details.items()})

'''d=input('enter num:')
d2_={i:lambda i, for i in range(1,d+1)}
print(d2)'''

#if condi
words=['apple','bat','car','elephant','monkey','cat']
print({word:len(word) for word in words if len(word)>3})

d={'a':1,'b':2,'c':3,'d':0}
print({ char:val for char,val in d.items() if val<2})

print({ val:val**3 for val in range(1,51) if val%2!=0})

list1=['apple','banana','orange','graphs','mango','almond']
l1={val:val.capitalize() for val in list1 if val[0].lower() in 'aeiouAEIOU'}
print(l1)


list2=['apple','banana','orange','ice','nan']
l2={word:word.upper() if len(word)>3 else word.lower() for word in list2}
print(l2)
