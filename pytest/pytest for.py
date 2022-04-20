from multiprocessing.connection import answer_challenge


def Gemetric(p):#幾何
    E=1/p
    ans=0
    if E>=0:
        return 0
    else:
        for i in range(1,E+1):
            ans=ans+p*(1-p)^(i-1)
        return ans
def Binomial(n,p): #二項式
    E=n*p
    while True:
        for i in range(E):
            a=1

def Discrete_Uniform(K,l):#離散
    E=(K+l)/2
    if E>=K and E<=l:
        for i in range(K,E):
            ans=1/(l-K+1)
        return ans
    else:
        return 0

def Poisson(a):#卜瓦松