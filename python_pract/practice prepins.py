'''strat=-4
end=10
for num in range(strat,end+1):
    if num<0:
        print(num)'''



def anagram(str1,str2):
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()
    if len(str1)!=len(str2):
        return False
    else:
        str1=sorted(str1)
        str2=sorted(str2)
        for i in range(len(str1)):
            if str1[i]!=str2[i]:
                return False
        return True
str1='heart'
str2='earth'
if anagram(str1,str2):
    print('is anagram')
else:
    print('is not')
            
