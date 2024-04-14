# import socket

# ip = "localhost"

# port = 58638
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
      
      
      
import socket
import threading
from tkinter import *
from tkinter import scrolledtext
def receive_message():
 while True:
      try:
            message = client.recv(1024).decode('utf-8')
            chat_log.insert(END, "Server: " + message + "\n")
      except:
            client.close()
            break

def send_message():
 message = entry_message.get()
 chat_log.insert(END, "Client: " + message + "\n")
 client.send(message.encode('utf-8'))
 entry_message.delete(0, END)
 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 58638))
window = Tk()
window.title("Client")
chat_log = scrolledtext.ScrolledText(window, width=50, height=10)
chat_log.grid(column=0, row=0, padx=10, pady=10)
entry_message = Entry(window, width=40)
entry_message.grid(column=0, row=1, padx=10, pady=10)
send_button = Button(window, text="Kirim", command=send_message)
send_button.grid(column=0, row=2, padx=10, pady=10)
receive_thread = threading.Thread(target=receive_message)
receive_thread.start()
window.mainloop()
