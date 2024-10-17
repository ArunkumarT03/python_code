
'''def check_ana(str1,str2):
    str1=str1.replace(' ','').lower()
    str2=str2.replace(' ','').lower()
    if len(str1)!=len(str2):
        return False
    else:
        str1=sorted(str1)
        str2=sorted(str2)
        for i in len(str1):
            if str1[i]!=str2[i]:
                return False
        return True
str1='heart'
str2='earth'
if check_ana(str1,str2):
    print('the strings are ana')
else:
    print('not ana')'''
'''def check_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    if len(str1) != len(str2):
        return False
    else:
        str1 = sorted(str1)
        str2 = sorted(str2)
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                return False
        return True
str1 = "heart"
str2 = "earth"
if check_anagram(str1, str2):
    print("The strings are anagrams.")
else:
    print("The strings aren't anagrams.")'''
    
    
def check_anagram(str1,str2):
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()
    if len(str1)!=len(str2):
        return False
    else:
        count1={}
        count2={}
        for i in str1:
            if i in count1:
                count1[i]+=1
            else:
                count1[i]=1
        for i in str2:
            if i in count2:
                count2[i]+=1
            else:
                count2[i]=1
        if count1==count2:
            return True
        else:
            return False
str1='listen'
str2='silenu'
if check_anagram(str1,str2):
    print('the strings are anagram')
else:
    print('the strings not')



'''s='aaaddc'
res=' '
for ch in s:
    if ch not in res:
        res+=ch
print(res)


s='javvvaa'
s1=set(s)
print(s1)'''


s='today is holyday'
res=' '
for ch in s.split():
    res+=ch[::-1]+' '
print(res.strip())
