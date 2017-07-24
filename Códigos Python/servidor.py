import socket
import sys

HOST = ''
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print ('Bind failed. Error code: ' + str(msg[0]))
    sys.exit()

print ('Bind completed')

s.listen(10)
print ('Now listening')

conn, addr = s.accept()
print ('Connected to ' + addr[0] + ':' + str(addr[1]))

for i in xrange(250000):
    conn.send ("hue" + str(i) + "\n")
    conn.send ("hue" + str(i) + "\n")
    conn.sendall("aeho" + str(i) + "\n")
conn.close()

s.close()
