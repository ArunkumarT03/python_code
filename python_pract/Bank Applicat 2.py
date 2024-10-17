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
            print('incorrect pin:')
    def checkbalance(self):
        if self.pin==self.checkpin():
            print(f'available Bal{self.Bal}')
        else:   
            print('incorrect pin:')
    def withdraw(self):
        if self.pin==self.checkpin():
            amount=int(input('enter a amount to withdraw:')           
            if amount<=self.Bal:
                self.Bal-=amount
                print('amount depit successfully')
                print(f'available Bal{self.Bal}')
            else:
                print('check your Bal first')
        else:
            print('incorrect pin')
    @staticmethod
    def checkpin():
        enter=int(input('enter the pin:') 
                  return enter
user1=SBI('A',2178961637,26734171724,9997,'male')
user2=SBI('B',3524166272,36715243517,8342,'male')
user3=SBI('C',2981715253,18936635153,9876,'female')
use1.withdraw()
