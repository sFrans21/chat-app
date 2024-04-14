# import socket

# ip = socket.gethostname()
# port = 58638

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


import socket
import threading
from tkinter import *
from tkinter import scrolledtext

def start_server():
 server.listen()
 print("Server Menunggu Koneksi...")
 while True:
      client, address = server.accept()
      print(f"Terhubung dengan {str(address)}")
      thread = threading.Thread(target=handle_client, args=(client,))
      thread.start()
def handle_client(client):
 while True:
      try:
            message = client.recv(1024).decode('utf-8')
            chat_log.insert(END, "Client: " + message + "\n")
      except:
            client.close()
            break

def send_message():
 message = entry_message.get()
 chat_log.insert(END, "Server: " + message + "\n")
 client.send(message.encode('utf-8'))
 entry_message.delete(0, END)
 
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.1.9', 58638))
window = Tk()
window.title("Server")
chat_log = scrolledtext.ScrolledText(window, width=50, height=10)
chat_log.grid(column=0, row=0, padx=10, pady=10)
entry_message = Entry(window, width=40)
entry_message.grid(column=0, row=1, padx=10, pady=10)
send_button = Button(window, text="Kirim", command=send_message)
send_button.grid(column=0, row=2, padx=10, pady=10)
server_thread = threading.Thread(target=start_server)
server_thread.start()
window.mainloop()