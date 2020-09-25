from stack import Stack
from stack import EmptyStack
    
def checkParanthesis(expression):

    s=Stack()
    openP="([{"
    closedP=")]}"
    matchP={')':'(',
            ']':'[',
            '}':'{'}

    for c in expression:
        if c in openP:
            s.push(c)
            continue

        if c in closedP:
            try:
                v=s.pop()
            except EmptyStack as errore:
                return False
            if v==matchP[c]:
                continue
            else:
                return False

    return not s
       

        
if __name__=='__main__':

    exprs=['[2)','[{s+1}*2]','((a+1)+3))','((((a+1)*2)+5)*[x+y]','(((a+1)*2)+5)*[x+y]']
    for expr in exprs:
        print (checkParanthesis(expr),"\t",expr)
    
