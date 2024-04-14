# import socket

# ip = socket.gethostname()
# port = 5505

# sc = socket.socket()
# sc.bind(ip, port)
# print("Server Diaktifkan")

# sc.listen(5)
# conn,addr = sc.accept()
# print("Terhubung dengan ", addr)

# while 1:
#       pesan = input(str(">>Anda: "))
#       pesan = pesan.encode()
#       conn.send(pesan)
      
#       inbox = conn.recv(1024)
#       inbox = inbox.decode
#       print("Client:", inbox)


from socket import *
import time
import random

serverPort = 12345
serverIP = "192.168.56.1"
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(serverIP, serverPort)
print("SERVER BILANGAN ACAK")

while True:
      message, clientAddress = serverSocket.recvfrom(2048)
      print(str(message.decode())) + " dari: " + str(clientAddress)
      
      bilAcak = random.randint(6,20)\
            
      time.sleep(1)
      
      serverSocket.sendto(str(bilAcak).encode(), clientAddress)