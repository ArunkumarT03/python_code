class parent:
    def m1(self):
        print('m1 is executed')
class child(parent):
    def m1(self):
        print('m1 of child class executed')
        
obj=child()
obj.m1()
