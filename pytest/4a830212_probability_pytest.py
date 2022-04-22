import math
from math import factorial
def Gemetric(p):#幾何
    E=int(1/p)
    ans=0.0
    if E<=0:
        return 0
    else:
        for i in range(1,(E)):
            ans=ans+(p*((1-p)**(i-1)))
            ans=round(ans, 3)
        return ans

def Binomial(n,p): #二項式
    E=int(n*p)
    n,p=int(n),float(p)
    ans=0
    while True:
        for i in range(E):
            mathGemetric=(p**i)*((1-p)**(n-i))
            mathfactorial=(factorial(n))/((factorial(i))*(factorial(n-i)))
            ans=ans+(mathfactorial*mathGemetric)
        break
    ans=round(ans, 3)
    return ans

def Discrete_Uniform(K,l):#離散
    E=int((K+l)/2)
    K=int(K)
    l=int(l)
    ans=0
    if E>=K and E<=l:
        for i in range(K,E):
            ans=ans+(1/(l-K+1))
            ans=round(ans, 3)
        return ans
    else:
        return 0

def Poisson(a):#卜瓦松
    E=int(a)
    a=int(a)
    ans=0
    mathexp=math.exp(-a)
    if a>0:
        for i in range(0,E):
            ans=ans+(((a**i)*mathexp)/factorial(i))
            ans=round(ans, 3)
        return ans
    else:
        return 0

if __name__ == '__main__':
    while True:
        print("請輸入你要計算的機率函數(1)幾何(2)二項式(3)離散(4)卜瓦松(5)結束:(請輸入數字)")
        doing=input()
        if doing=='1':
            p=float(input("請輸入Gemetric的P值:"))
            print("Gemetric的P值為%.2f，結果為%0.3f\n"%(p,Gemetric(p)))
        elif doing=='2':
            N,P=map(float,input("請輸入Binomial的N,P值:").split())
            print("Binomial的N,P值為%.2f %.2f，結果為%0.3f"%(N,P,Binomial(N,P)))
        elif doing=='3':
            K,l=map(float,input("請輸入Discrete_Uniform的K,l值:").split())
            print("Discrete_Uniform的K,l值為%.2f %.2f，結果為%0.3f"%(K,l,Discrete_Uniform(K,l)))
        elif doing=='4':
            a=float(input("請輸入Poisson的a值:"))
            print("Poisson的a值為%.2f，結果為%0.3f"%(a,Poisson(a)))
        elif doing=='5':
            break

def test_Discrete_Uniform():
    assert Discrete_Uniform(0,6)==0.429
def test_Gemetric():
    assert Gemetric(0.333333333)==0.555
def test_Poisson():
    assert Poisson(3)==0.423
def test_Binomial():
    assert Binomial(6,0.5)==0.344