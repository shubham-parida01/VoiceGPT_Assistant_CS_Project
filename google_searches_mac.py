import subprocess


def search_query():
    f = open("Input.txt","r")
    x = f.readline()
    y = x.split()
    z = y.pop(0)
    a = y

    search_url = "https://www.google.com/search?q="
    b = "+".join(a)

    subprocess.Popen(["open", "-a", "Google Chrome", search_url + b])

