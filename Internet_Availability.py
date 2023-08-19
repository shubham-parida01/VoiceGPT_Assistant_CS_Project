import socket

def check_internet_connection():
    try:
        # Attempt to connect to a well-known website (e.g., Google DNS server)
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except socket.error:
        return False