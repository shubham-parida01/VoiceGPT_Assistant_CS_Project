import platform
import subprocess

def open_application(application_name):
    system = platform.system()

    if system == 'Windows':
        subprocess.Popen(['start', '', application_name], shell=True)
    elif system == 'Darwin':
        subprocess.Popen(['open', '-a', application_name])
    else:
        print("Unsupported operating system.")



