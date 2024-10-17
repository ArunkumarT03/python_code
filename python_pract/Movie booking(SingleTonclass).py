def singleTonclass(arg):
    L=[]
    def inner():
        if len(L)==0:
            L.append(arg())
        return L[0]
    return inner
@singleTonclass
def movie1():
    def __init__(self):
        self.maxtickets=100
    def booking(self):
        ticket=int(input('enter the number of tick:'))
        if ticket<=self.maxtickets:
            self.maxtickets-=ticket
            print('your ticket booked...')
            print(f'available ticket{self.maxtickets}')
        else:
            print('ticket not available')
@singleTonclass
def movie2():
    def __init__(self):
        self.maxtickets=200
    def booking(self):
        ticket=int(input('enter the number of tick:'))
        if ticket<=self.maxtickets:
                   self.maxtickets-=ticket
                   print('your ticket booked...')
                   print(f'available ticket{self.maxtickets}')
        else:
            print('ticket not available')
def payTM():
    print('available movies are:\n1)movie-1\n2)movie2')
    choice=int(input('choose the movie option'))
    if choice==1:
        obj1=movie1()
        obj1.booking()
    elif choice==2:
        obj2=movie2()
        obj2.booking()
    else:
        print('choose the movie correctly')
def BMys():
    print('available movies are:\n1)movie-1\n2)movie2')
    choice=int(input('choose the movie option'))
    if choice==1:
        obj1=movie1()
        obj1.booking()
    elif choice==2:
        obj2=movie2()
        obj2.booking()
    else:
        print('choose the movie correctly')
payTM()
BMys()
