import random


def joke():
    f = open('jokes.txt', 'r')
    l = f.readlines()
    b = random.choice(l)
    f.close()
    g = open("Output.txt","w")
    g.write(b)
