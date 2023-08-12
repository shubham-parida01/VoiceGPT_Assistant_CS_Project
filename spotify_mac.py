import subprocess


def play():
    subprocess.Popen(['open', '-a', 'Spotify'])
    script = 'tell application "Spotify" to play'
    subprocess.Popen(['osascript', '-e', script])


def play_song():
    f = open("Input.txt","r")
    b = f.readline()
    a = b[5:]


    script = (f'\n'
              f'    tell application "Spotify" to activate\n'
              f'    tell application "System Events"\n'
              f'       keystroke "k" using command down\n'
              f'	   set song_name to "{a}" \n'
              f'	   keystroke song_name\n'
              f'	   keystroke (return) using shift down\n'
              f'    end tell')
    subprocess.Popen(['osascript', '-e', script])


def pause():
    script = 'tell application "Spotify" to pause'
    subprocess.Popen(['osascript', '-e', script])


def next_track():
    script = 'tell application "Spotify" to next track'
    subprocess.Popen(['osascript', '-e', script])


def prev_track():
    script = 'tell application "Spotify" to previous track'
    subprocess.Popen(['osascript', '-e', script])


def control_spotify():
    f = open("Input.txt", "r")
    a = f.readline()
    if 'play' in a:
        if len(a) == 4:
            play()
        else:
            play_song()
    elif 'pause' in a:
        pause()
    elif 'next' in a:
        next_track()
    elif 'previous' in a:
        prev_track()
    else:
        print("Error in command")




