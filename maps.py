import webbrowser
import urllib.parse

def open_maps(destination:str):
    query = f"Your Location+to+{destination}"
    url = f"https://www.google.com/maps/search/{urllib.parse.quote(query)}"

    webbrowser.open(url)



