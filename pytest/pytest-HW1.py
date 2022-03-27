def funA(calc_tax):
    minus=120000+200000 #320000 單身+標準扣除額+薪資所得特別扣除額
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
    assert funA(500000)==9000

def test_answer1():
    assert funA(800000)==24000 

def test_answer2():
    assert funA(5000000)==1042400

def test_answer3():
    assert funA(2120000)==225400

def test_answer4():
    assert funA(3330000)==526400
