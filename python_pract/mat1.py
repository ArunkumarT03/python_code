'''r=int(input('entr rows:'))
c=int(input('entr cols:'))
mat=[]

for ro in range(r):
    line=[]
    for cl in range(c):
        line.append(int(input('enter values:')))
    mat.append(line)

print(mat)'''

m1=[[2,3,4],[3,4,5]]
m2=[[3,4,5],[4,5,6]]

if len(m1[0])==len(m2):
  for r in range(m1):
     for c in range(m2):
        m1[r][c]=m1[r][c]+m2[r][c]
print(m1)
    
