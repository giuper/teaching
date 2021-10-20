from stack import Stack
from stack import EmptyStack
    
def checkParenthesis(expression,verbose=False):

    s=Stack()

    openP="([{"
    closedP=")]}"

    matchP={')':'(',
            ']':'[',
            '}':'{'}

    if verbose:
        print()
        print("*****")
        print(expression)
        
    for c in expression:
        if verbose:
            print("Ho letto: ",c)
            print(s)
        if c in openP:
            s.push(c)
            if verbose:
                print("Inserisco in stack")
                print(s)
            continue

        if c in closedP:
            try:
                v=s.pop()
            except EmptyStack as errore:
                if verbose:
                    print("Stack vuoto")
                return False
            if verbose:
                print("Ho letto ", v,"dallo stack")
            if v==matchP[c]:
                if verbose:
                    print("Si bilanciano",c,v)
                continue
            else:
                if verbose:
                    print("Non si bilanciano",c,v)
                return False

    if verbose:
        print("Stack prima di terminare",s)
    return not s
       

        
if __name__=='__main__':

    exprs=['[2)','[{s+1}*2]','((a+1)+3))','((((a+1)*2)+5)*[x+y]','(((a+1)*2)+5)*[x+y]','(3+[2-1])']
    for expr in exprs:        
        print (checkParenthesis(expr,True),"\t",expr)
    
