'''m1=[[2,3,4],[5,6,7]]
m2=[[5,6,8],[6,8,3]]

if len(m1)==len(m2) and len(m1[0])==len(m2[0]):
    for r in range(len(m1)):  
        for c in range(len(m1[0])):
            m1[r][c]=m1[r][c]+m2[r][c]
    print(m1)
    

r=int(input('enter a rows:'))
c=int(input('enter a cols:'))
mat=[]
for rows in range(r):
    line=[]
    for cols in range(c):
        line.append(int(input('enter a values:')))
    mat.append(line)
print(mat)'''


m1=[[2,3,4],[3,5,6],[6,8,9]]
m2=[[3,4,5],[3,4,7],[8,9,2]]
mat1=[]
if len(m1[0])==len(m2):
    for r in range(len(m1)):
        line=[]
        for c in range(len(m2[0])):
            ans=0
            for v in range(len(m2)):
                ans+=m1[r][c]+[v][c]
            line.append(ans)
        mat1.append(line)
print(mat1)
        
