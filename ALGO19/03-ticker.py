class Ticker:

    def __init__(self):
        self.np=0
    
    def inc(self):
        self.np+=1

    def dec(self):
        if(self.np>0):
            self.np-=1

    def reset(self):
        self.np=0

    def current(self):
        return self.np



t=Ticker()
s=Ticker()
t.inc()
s.inc()
t.inc()
s.inc()
t.inc()
s.inc()
s.dec()

print (t.current())
print (s.current())
