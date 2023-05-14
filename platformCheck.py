import platform

def check_operating_system():
    system = platform.system()
    if system == "Windows":
        return "Windows"
    elif system == "Darwin":
        return "macOS"
    else:
        return "Unknown"

# Check the operating system
operating_system = check_operating_system()
print("Operating System:", operating_system)
