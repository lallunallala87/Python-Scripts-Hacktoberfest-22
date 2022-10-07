import ipaddress
from datetime import date, datetime
from os import stat
import socket
import sys
from time import time
print("Welcome to port scanner")
user_input = input("Enter a hostname or ipaddress: ")
# converts
ipaddr = socket.gethostbyname(user_input)
start_time = datetime.now()
print("-"*50)
print(f"Scanning: {ipaddr}")
print("-"*50)

try:
    for port in range(1, 5000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        # trys to connect to the port, returns non zero value if connection is failed
        is_open = s.connect_ex((ipaddr, port))
        if (is_open == 0):
            print(f"the port {port} is open")
        s.close()
    endtime = datetime.now()
    time_taken = endtime-start_time

    print(f"Scanning completed in {time_taken.seconds} seconds")
except KeyboardInterrupt:
    # Ctrl+C pressed
    print("exiting...")
    sys.exit()
except socket.gaierror:
    print("\n error invalid hostname")
    sys.exit()
except socket.error:
    print("\n server did not respond!")
    sys.exit()
