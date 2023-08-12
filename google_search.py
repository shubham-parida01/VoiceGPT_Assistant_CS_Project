import webbrowser
def search_on_google(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open_new_tab(search_url)


search_query = "the capital of india"

search_on_google(search_query)

