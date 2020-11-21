class coppie:
    ##gli oggetti della classe sono coppie di interi

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __le__(self,other):
        return self.a<=other.a

    def __str__(self):
        return "("+str(self.a)+","+str(self.b)+")"
