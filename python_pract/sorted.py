'''str1='i am late'
print(sorted(str1))
print(' '.join(sorted(str1,reverse=True)))

names=['bob','mill','steve','pavan','ak']
print(sorted(names,key=(len)))
print(sorted(names))

def last_char(names):
    for name in names:
        print(name[-1])
last_char([names])'''

def last_char(names):
    return names[-1]
print(sorted(['bob','mill','arun','steve','ola'],key=last_char,reverse=True))

first_char=lambda names:names[0]
print(sorted(['bob','mill','arun','cat','not','mani','make'],key=first_char))

prices={'acme':45.5,'aatl':612.78,'ibm':205.55,'hp':37.20,'fb':10.75}
print(sorted(prices,key=lambda prices:max(prices),min(prices))))
