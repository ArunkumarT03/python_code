str1='abcbbacdabgbabababa'
max_len=' '
for i in range(len(str1)):
    for j in range(i+1,len(str1)):
        if str1[i]==str1[j]:
            rev=''
            for ch in range(i,j+1):
                rev=str1[ch]+rev
            if rev==str1[i:j+1]:
                if len(max_len)<len(str1[i:j+1]):
                    max_len=str1[i:j+1]
print(max_len)
