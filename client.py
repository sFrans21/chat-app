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
      
