#method chaining
class whatsappv1:
    def __init__(self,Name,DM,DP):
        self.Name=Name
        self.DM=DM
        self.DP=DP
    def features(self):
        print(f'Name:{self.Name}')
        print(f'DM:{self.DM}')
        print(f'DP:{self.DP}')
class whatsappv2(whatsappv1):
    def __init__(self,Name,DM,Dp,status,Acall):
        super().__init__(Name,DM,Dp)
        self.status=status
        self.Acall=Acall
    def features(self):
        super().features()
        print(f'status:{self.status}')
        print(f'Acall:{self.Acall}')
class whatsappv3(whatsappv2):
    def __init__(self,Name,DM,DP,status,Acall,Vcall,payments):
        super().__init__(Name,DM,DP,status,Acall)
        self.Vcall=Vcall
        self.payments=payments
    def features(self):
        super().features()
        print(f'Vcall:{self.Vcall}')
        print(f'payments:{self.payments}')
        
obj1=whatsappv3('Arun','yes','yes','no','yes','yes','no')
obj1.features()
