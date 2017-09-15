import random

msgs = ["You rolled two {}s. Move {} spaces.","You rolled a {} and a {}. Move {} spaces.", "You have rolled three doubles in a row. Go to jail."]

def rollDice():
    return [random.randint(1,6),random.randint(1,6)]

def getMsg(d1,d2,doubles):
    if d1 == d2:
        doubles += 1
        ret = msgs[0].format(d1,4*d1)
    elif d1 != d2:
        ret = msgs[1].format(d1,d2,d1+d2)
    if doubles == 3:
        ret = msgs[3]
    return [doubles,ret]

def main(doubles):
    die1,die2 = rollDice()
    double = doubles
    doubleNew,msg = getMsg(die1,die2,double)
    print(msg)
    if doubleNew - double == 1:
        main(doubleNew)
