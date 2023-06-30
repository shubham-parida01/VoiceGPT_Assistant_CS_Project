import webbrowser
import urllib.parse

def search_on_google(query):
    search_url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
    webbrowser.open_new_tab(search_url)



