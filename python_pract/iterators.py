''''L=[3,4,5,7]
obj=iter(L)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
while True:
    print(next(obj))

for i in range (len(L)+1):
    print(next(obj))'''

#userdefined

class seq():
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def __iter__(self):
        return self
    def __next__(self):
        var=self.start
        if self.start>self.end:
            raise StopIteration
        self.start+=1
        return  var
obj=seq(10,15)
addit=iter(obj)
'''print(next(addit))
print(next(addit))
print(next(addit))
print(next(addit))
print(next(addit))
print(next(addit))
print(next(addit))'''
'''for ch in obj:
    print(ch)'''
'''while True:
    print(next(obj))'''

