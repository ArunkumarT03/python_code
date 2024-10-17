'''list1=input('enter elements:').split()
list2=input('enter elements:').split()
print(list1+list2)




l=['abc','123','hello','23']
l1=[]
for ch in l:
    if ch.isdigit():
        l1+=ch
print(l1)'''


#alternative
l3=['hello','hello','meloddy','vlogss','kaalai']
res=[]
for c in l3:
    for i in range(len(l3)):
        if l3[i].count(l3[i])>1:
           res.append(c[i])
                   
                         
print(res)
        
#even length
name=['apple','google','gmail','instagram','whatsapp','facebook','snapchat']
res=[]
for ch in name:
    if len(ch)%2==0:
        res.append(ch)
print(res)

l1=['hi','hello','goog morning','bye']
rev=l1[::-1]
l2=[]
for c in range(len(l1)):
    var=rev[c][::-1]
    l2.append(var)
print(l2)


#alternative
'''str1=input('enter:')
ne_1=[]
for ind in range(len(str1)):
    if ind%2==0:
        ne_1+=[str1[ind]]
print(ne_1)'''

'''print(list(filter(lambda num:num%2!=0,range(1,50))))

name=['apple','google','yahoo','apple','google','amazon','google']
ans=[]
for i in name:
    if name.count(i)>1:
        ans.append(i)
print(ans)

numbers=[400,57,567,34]
max_num=0
for num in numbers:
    if max_num<num:
        max_num=num
print(max_num)'''

l6=[3,4,1,7,2,12,8,6,9,11]
ans1=[]
ans2=[]
for n in l6:
    if n%2==0:
        ans1.sort()
        ans1.append(n)
    elif n%2!=0:
        ans2.sort()
        ans2.append(n)
print(ans1,ans2)
print(ans1)


st1='hello123 world567 welcome to 9724python'
res1=0
for ch in st1:
    if ch.isdigit() and int(ch)%2==0:
        res1+=int(ch)
print(res1)
        
