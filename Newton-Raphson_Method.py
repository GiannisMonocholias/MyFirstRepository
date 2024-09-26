def newton_raphson(f,df,x,M,Ef,accuracy):
    n = 0
    print("------------------------------------")
    print(" n |   xn     |   f(xn)   |  f'(xn)|")
    while n<=M and abs(f(x))>Ef  and abs(df(x))>0:
        print(f" {n} |  {x:.{accuracy}f}  |  {f(x):.{accuracy}f}   |  {df(x):.{accuracy}f}|")
        x = x - f(x)/df(x)
        n+=1
    print(f" {n} |  {x:.{accuracy}f}  |  {f(x):.{accuracy}f}   |  {df(x):.{accuracy}f}|")
    print("------------------------------------")    

from math import sin,cos      
newton_raphson(lambda x: x - cos(x),lambda x: 1 + sin(x),0,10,0,"4")