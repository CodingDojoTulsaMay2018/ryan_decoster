
import random

def randInt(min=0,max=0):
    if max==0:
        max=100
    if min!=0:
        max-=min
    x=random.random()*max+min
    print(round(x))

randInt()
randInt(max=50)
randInt(min=50)
randInt(min=50, max=500)