import platform
import subprocess
import time
import urllib
import webbrowser
import pyautogui

def check_application_installed(application_name):
    command = 'which {}'.format(application_name) if platform.system() == 'Darwin' else 'where {}'.format(application_name)
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.returncode == 0

def open_chrome_and_play_song(song_name):
    try:
        subprocess.Popen(["C:/Program Files/Google/Chrome/Application/chrome.exe"])  # Replace with "chrome" on Windows
        print("Opened Google Chrome")

        # Wait for Chrome to open
        time.sleep(2)

        # Search and play the song on Spotify Web Player
        search_query = f"https://open.spotify.com/search/{urllib.parse.quote(song_name)}"
        webbrowser.open_new_tab(search_query)
        pyautogui.sleep(8)
        pyautogui.hotkey('ctrl', 'k')
        pyautogui.write(song_name)
        time.sleep(3)
        pyautogui.hotkey('shift', 'enter')
    except FileNotFoundError:
        print("Google Chrome not found on the system")

def open_spotify_and_play_song(song_name):
    try:
        subprocess.Popen(["spotify"])
        print("Opened Spotify")

        # Wait for Spotify to open
        time.sleep(20)

        # Search and play the song on Spotify desktop app
        pyautogui.hotkey('ctrl', 'k')
        pyautogui.write(song_name)
        time.sleep(3)
        pyautogui.hotkey('shift', 'enter')
        print(f"Playing song '{song_name}' on Spotify desktop app")
    except FileNotFoundError:
        print("Spotify not found on the system")

def music_play(song_name):
    if not check_application_installed('Spotify'):
        open_spotify_and_play_song(song_name)
    else:
        open_chrome_and_play_song(song_name)


