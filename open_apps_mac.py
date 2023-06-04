import os


def open_app(a):
    b = a.split()
    c = b[-1]

    os.system("open -a" + c)





