def funA(calc_tax):
    minus=88000+120000 #208,000
    calc_tax=calc_tax-minus 
    total=0
    if(calc_tax<=540000):
        total=calc_tax*0.05
    elif(540000<calc_tax<=1210000):
        total=calc_tax*0.12-37800
    elif(1210000<calc_tax<=2420000):
        total=calc_tax*0.2-134600
    elif(2420000<calc_tax<=4530000):
        total=calc_tax*0.3-376600
    elif(4530000<calc_tax):
        total=calc_tax*0.4-829600
    return total

def test_answer():
    assert funA(500000)==14600 #292,000

def test_answer1():
    assert funA(800000)==33240 #592,000

def test_answer2():
    assert funA(5000000)==1087200 #4,792,000

def test_answer3():
    assert funA(2120000)==247800 #1,912,000

def test_answer4():
    assert funA(3330000)==560000 #3,122,000