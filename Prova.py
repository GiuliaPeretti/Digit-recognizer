class somma:
    a, b= None, None

    def __init__ (self, a, b):
        self.a=a
        self.b=b

    def stampa(self):
        ris=self.a+self.b;
        print(ris)

c=somma(2,5)
c.stampa()
    