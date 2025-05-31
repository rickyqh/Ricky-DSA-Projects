import random
import time

money=1500
buncost=2
meatcost=4
vegcost=3


b=0
m=0
v=0
bu=0



input("Hello!Your objective of the game is to earn as much money as posible. You are operating a fast food stall.\nnext")
input("1 burger needs 1bun,1meat and 1veg\nnext")
input("1 burger is sold for $15\nnext")
while True:
    peo=0
    print(f"you have ${money},\n{b} bread,\n{m} meat,\n{v} veg\nand {bu} burger")
    coose=input("1. buy bun\n2.buy meat\n3.buy veg\n4.Make burger\n5.open shop\nchoose:")
    if coose=="1":
        x=int(input("How much bun?\n:"))
        money-=x*buncost
        b+=x
        print("processing payment...")
        time.sleep(2)
        print(money,b)
    elif coose=="2":
        y=int(input("How much meat?\n:"))
        money-=y*meatcost
        m+=y
        print("processing payment...")
        time.sleep(2)
        print(money,m)
    elif coose=="3":
        z=int(input("How much veg?\n:"))
        money-=z*vegcost
        v+=y
        print("processing payment...")
        time.sleep(2)
        print(money,v)
    elif coose=="4":
        bur=int(input("how much?"))
        if b<bur:
            print("invalid items.You fool\npenalty!!!!!!!!!!!!!!!!!!!")
            time.sleep(5)
        elif m<bur:
            print("invalid items.You fool\npenalty!!!!!!!!!!!!!!!!!!!")
            time.sleep(5)
        elif v<bur:
            print("invalid items.You fool\npenalty!!!!!!!!!!!!!!!!!!!")
            time.sleep(5)
        else:
            b-=bur
            m-=bur
            v-=bur
            bu+=bur
            print("making burger...")
            time.sleep(2)
            print(bu)
    elif coose=="5":
        peo=random.randint(1,100)
        if bu<peo:
            peo=bu
        bu-=peo
        money=money+peo*15
        print("open for the day...")
        time.sleep(1)
        print(f"you earned ${peo*15}")


