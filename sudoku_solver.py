# Head ends here
from itertools import chain as ch
from copy import deepcopy as dc
r=range
def ga(i):
    a=27*(i/27)+3*((i/3)%3)
    b=i/9
    return r(a,a+3)+r(9+a,a+12)+r(18+a,a+21)+r(i%9,80,9)+r(9*b,9*b+9)
def l(g):
    z=(11,0)
    for i in r(81):
        t=len(g[i])
        if z[0] > (t if t>1 else 11): z = (t,i)
    return z
s='123456789'
def sudoku_solve(g):
    g=[str(z).replace('0',s[:]) for z in ch.from_iterable(g)]
    q=[(g,[i for i in r(81) if len(g[i])==1])]
    while True:
        g,b=q[-1]
        while len(b):
            n=[]
            for i in b:
                for d in ga(i):
                    if d!=i:
                        c=g[d]
                        u=len(c)
                        g[d]=c.replace(g[i],"")
                        if len(g[d])==1 and u>1:n+=[d]
            b=n
        for i in r(81):
            if len(g[i]) == 0:
                q.pop()
                continue
        if l(g)[0]==11:
            for d in r(9): print " ".join(g[9*d:9*d+9])
            return
        f=l(g)[1]
        for h in g[f]:
            o=g[:]
            o[f] = h
            q+=[(o,[f])]
# Tail starts here

n = input()

for i in range(n):
    board = []
    for j in range(9):
        board.append([int(k) for k in raw_input().split()])
    sudoku_solve(board)
