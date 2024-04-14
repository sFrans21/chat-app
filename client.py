# import socket

# ip = "localhost"

# port = 5505

# sc = socket.socket()

# try: 
#       sc.connect((ip,port))
#       print("Terhubung dengan server")
# except:
#       print("Sambungan gagal: (")
      
# while 1:
#       inbox = sc.recv(1024)
#       inbox = inbox.decode()
#       print("server: ",inbox)
      
#       pesan = input(str(">>Anda: "))
#       pesan = pesan.encode()
#       sc.send(pesan)
      
      
from socket import *
import random
import time
import string

serverName = "192.168.56.1"
serverPort = 12345
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input("Masukkan nama anda: ")
clientSocket.sendto(message.encode(), (serverName, serverPort))

while True:
      pesan, serverAddress = clientSocket.recvfrom(2048)
      message = "Permintaan acak"
      clientSocket.sendto(message.encode(), (serverName, serverPort))
      print("Bilangan acak dari server:(" + str(serverAddress)+ "): " + str(pesan.decode()))