num=5
space=0
for lines in range(num,0,-1):
    for sp in range(space):
        print(' ',end=' ')
    for val in range(lines):
        print(lines,end=' ')
    print()
space+=1
num-=1
