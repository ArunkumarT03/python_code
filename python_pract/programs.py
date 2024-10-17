def prime(num):
    for fa in range(2,num//2+1):
        if num%fa==0:
            return False
    return num
print(list(filter(prime,[8098770080])))
    
