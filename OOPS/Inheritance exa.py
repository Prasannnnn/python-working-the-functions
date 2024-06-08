class CSK:
    def __init__(self) -> None:
        print("Ruturaj")

    def batting(self):
        print("Rachin, Gaikwad , Mitchell, Ali, Jadeja, Dhoni, Rizhivi")

    def bowling(self):
        print("Pathi,Theekshana,Rahaman,tushar,chhahar, thakur")

class RCB:
    def __init__(self) -> None:
        print("faf")
    
    def bat(self):
        print("kholi,faf,dk")

    def bowl(self):
        print("siraj,chachal,karan")

class MI(RCB,CSK):
    def __init__(self) -> None:
        super().__init__()
        print("Pandya")
   
    def bati(self):
        print("vada paw, surya, pandya")

    def bow(self):
        print("bumrah")

c =MI()
'''
Method Resolution order (MRO)
'''