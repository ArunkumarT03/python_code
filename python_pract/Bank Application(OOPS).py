class SBI:
    IFSC='SBIN00123'
    branch='kkdi'
    ROI=0.07
    def __init__(self,name,Aadhar,mno,Bal,pin,gender):
        self.name  =name
        self.Aadhar=Aadhar
        self.mno   =mno
        self.Bal   =Bal
        self.pin   =pin
        self.gender=gender
    @classmethod
    def changebranch(cls):
        cls.branch='marathahalli'
    def Deposite(self):
        if self.pin==self.checkpin(): 
            self.Bal+=int(input('enter a deposite amount:'))
            print('amount credit successfully..')
            print(f' available Bal{self.Bal}')
        else:
            count=0
            while count<=2:
                if self.pin!=self.checkpin():
                    print('inavlid pin')
                count+=1
           
    def checkbalance(self):
        if self.pin==self.checkpin():
            print(f'available Bal{self.Bal}')
        else:
            count=0
            while count<=2:
                if self.pin!=self.checkpin():
                    print('inavlid pin')
                count+=1
           
    def pinlimit(self):
        count=0
        while count<=2:
            if self.pin!=self.checkpin():
                print('invalid pin')
            count+=1
    def changepin(self):
        changepin=int(input('enter new pin:'))
        if self.pin==self.checkpin:
            print('enter a new pin:')
    def withdraw(self):
        if self.pin==self.checkpin():
            amount=int(input('enter a amount to withdraw:'))
            if amount <= self.Bal:
                self.Bal -= amount
                print('amount debit successfully')
                print(f'available Bal{self.Bal}')
            else:
                print('check your Bal first')
        else:
            count=0
            while count<=2:
                if self.pin!=self.checkpin():
                    print('inavlid pin')
                count+=1
           
           
    @staticmethod
    def checkpin():
        enter=int(input('enter the pin:')) 
        return enter
user1=SBI('A',2178961637,26734171724,70000,9997,'male')
user2=SBI('B',3524166272,36715243517,80000,8342,'male')
user3=SBI('C',2981715253,18936635153,90000,9876,'male')
user1.changepin()
