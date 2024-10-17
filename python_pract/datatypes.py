var=[[5,'mi','csk',[1,'gt','srh',[0,'rcb','lsg'],'dc']]]
'''print(var)
print (var[0][0])
print(var[0][1])
print(var[0][1][0])
print(var[0][1][1])
print(var[0][2])
print(var[0][2][0])
print(var[0][2][1])
print(var[0][2][2])
print(var[0][3][0])
print(var[0][3][1][0])
print(var[0][3][1][1])
print(var[0][3][2][0])
print(var[0][3][2][1])
print(var[0][3][2][2])
print(var[0][3][3][0])
print(var[0][3][3][1])
print(var[0][3][3][1][0])
print(var[0][3][3][1][1])
print(var[0][3][3][1][2])
print(var[0][3][3][2])
print(var[0][3][3][2][0])
print(var[0][3][3][2][1])
print(var[0][3][3][2][2])
print(var[0][3][4])
print(var[0][3][4][0])
print(var[0][3][4][1])'''
#negative
#var=[[5,'mi','csk',[1,'gt','srh',[0,'rcb','lsg'],'dc']]]
'''print(var[-1][-1])
print(var[-1][-1][-1])
print(var[-1][-1][-2])
print(var[-1][-1][-1][-1])
print(var[-1][-1][-1][-2])
print(var[-1][-1][-2][-1])
print(var[-1][-1][-2][-1][-1])
print(var[-1][-1][-2][-1][-2])
print(var[-1][-1][-2][-1][-3])
print(var[-1][-1][-2][-2])     
print(var[-1][-1][-2][-2][-1])
print(var[-1][-1][-2][-2][-2])
print(var[-1][-1][-2][-2][-3])
print(var[-1][-1][-2][-3])
print(var[-1][-1][-3])
print(var[-1][-1][-3][-1])
print(var[-1][-1][-3][-2])
print(var[-1][-1][-3][-3])
print(var[-1][-1][-4])
print(var[-1][-1][-4][-1])
print(var[-1][-1][-4][-2])
print(var[-1][-1][-5])
print(var[-1][-2])
print(var[-1][-2][-1])
print(var[-1][-2][-2])
print(var[-1][-2][-3])
print(var[-1][-3])
print(var[-1][-3][-1])
print(var[-1][-3][-2])
print(var[-1][-4])
'''
def max_sum(arr):
    max_sum=float('-inf')
    current_sum=0
    for num in arr:
        current_sum=max(num,current_sum+num)
        max_sum=max(max_sum,current_sum)
    return max_sum

print(max_sum([1987,6543,98,3725,63]))








_
