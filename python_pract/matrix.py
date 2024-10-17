#rows=int(input('enter a rows:'))
#columns=int(input('enter a columns:'))
'''mat=[]
for r in range(rows):
            line=[]
            for c in range(columns):
              line.append(int(input('enter a values:')))
            mat.append(line)
print(mat)'''


#list comphrehension

#print([[int(input('enter a values:'))for c in range(columns)]for r in range(rows)])

#add
'''m1=[[1,5,3],[6,5,4]]
m2=[[2,5,8],[1,0,2]]
mat=[]
if len(m1)==len(m2) and len(m1[0])==len(m2[0]):
    for r in range(len(m1)):
        line=[]
        for c in range(len(m1[0])):
            line.append(m1[r][c]-m2[r][c])
        mat.append(line)
print(mat)
else:
    print('np')'''
    
#mul
m1=[[1,5,3],[6,5,4]]
m2=[[2,5,8],[1,0,2],[2,3,4]]
mat=[]
if len(m1[0])==len(m2):
    for r in range(len(m1)):
        line=[]
        for c in range(len(m2[0])):
            ans=0
            for v in range(len(m2)):
                ans+=m1[r][v]*m2[v][c]
            line.append(ans)
        mat.append(line)
    print(mat)
else:
    print
