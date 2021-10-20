from stack import Stack


def sol1(exp):

    s=Stack()
    for c in exp:

        if c==' ':
            continue

        if c=='+':
            x=s.pop()
            y=s.pop()
            s.push(x+y)
            continue

        if c=='*':
            x=s.pop()
            y=s.pop()
            s.push(x*y)
            continue

        s.push(int(c))
    return s.pop()

def sol2(exp,vals):

    s=Stack()
    for c in exp:

        if c==' ':
            continue

        if c=='+':
            x=s.pop()
            y=s.pop()
            s.push(x+y)
            continue

        if c=='*':
            x=s.pop()
            y=s.pop()
            s.push(x*y)
            continue

        if c in vals.keys(): 
            s.push(vals[c])
            continue

        s.push(int(c))

    return s.pop()

def sol3(exp):

    s=Stack()
    f=0; x=0;
    for c in exp:

        if c==' ':
            if (f==1):
                s.push(x)
                f=0
            continue

        if (f==1):
            x=x*10+int(c)
            continue

        if c=='+':
            x=s.pop()
            y=s.pop()
            s.push(x+y)
            continue

        if c=='*':
            x=s.pop()
            y=s.pop()
            s.push(x*y)
            continue

        f=1 
        x=int(c)

    return s.pop()
        

