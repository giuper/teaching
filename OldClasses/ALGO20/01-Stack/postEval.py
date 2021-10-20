from stack import Stack
from stack import EmptyStack

class BadExpression(Exception):
    def __str__(self):
        return "Bad expression"
    
def postEval(expression):

    digits=['0','1','2','3','4','5','6','7','8','9']
    operators=['+','*','-']
    s=Stack()
    for c in expression:

        if c==' ':
            continue

        if c in digits:
            s.push(c)
            continue
        
        if c in operators:
            try:
                op1=s.pop()
            except EmptyStack as errore:
                raise BadExpression
            try:
                op2=s.pop()
            except EmptyStack as errore:
                raise BadExpression
            
            if c=='-':
                s.push(int(op2)-int(op1))
            if c=='*':
                s.push(int(op1)*int(op2))
            if c=='+':
                s.push(int(op1)+int(op2))

            continue

        raise BadExpression

    val=s.pop()

    if not s:
        return val
    else:
        raise BadExpression

    return s.pop()

        
        
    

        
if __name__=='__main__':

    exprs=['2 3 +','2 3 + 4 5 * -','7 4 * 2 + 3 *','2 3 4 *']
    for expr in exprs:
        try: 
            val=postEval(expr)
        except BadExpression as errore:
            print(expr,": espressione mal formata")
        else:
            print(expr,"\t--> ",val)
