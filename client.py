
import threading
import socket
import argparse
import os
import sys
import tkinter as tk
import time

class Send(threading.Thread):

      def __init__(self, sock, name):
            super().__init__()
            self.sock = sock
            self.name = name
            
            
      def run(self):
            while True:
                  print('{}:'.format(self.name), end='')
                  sys.stdout.flush()
                  message = sys.stdin.readline()[:-1]
                  
                  if message == "QUIT":
                        self.sock.sendall('Server: {} sudah meninggalkan pembicaraan.'.format(self.name).encode('ascii'))
                        break
                  
                  else:
                       self.sock.sendall('{}: {} '.format(self.name, message).encode('ascii'))
                        

            print('\nMencoba keluar....')
            self.sock.close()
            os.exit(0)
            
class Receive(threading.Thread):
      
      def __init__(self, sock, name):
            super().__init__()
            self.sock = sock
            self.name = name
            self.messages = None
            
      def run(self):
            
            while True:
                  message = self.sock.recv(1024).decode('ascii')
                
                  if message:
                        if self.messages:
                            self.messages.insert(tk.END, message)
                            print('hi')
                            print('\r{}\n{}: '.format(message, self.name), end='')
                            
                        else:
                              print('\r{}\n{}: '.format(message, self.name), end='')
                            
                  else:
                        print('\n Oh tidak, kita kehilangan koneksi dengan server:(')
                        print('\nMencoba keluar....')
                        self.sock.close()
                        os.exit(0)
      

class Client:
           
           
      def __init__(self, host, port): 
            self.host = host
            self.port = port
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.name = None
            self.messages = None
            

      def start(self):
            
            print('Mencoba menghubungkan {}:{}...'.format(self.host, self.port))
            time.sleep(1)
            self.sock.connect((self.host, self.port))
            print('Berhasil! Terhubung ke {} {}'.format(self.host, self.port))
            
            print()
            self.name = input('Nama kamu: ')
            print()
            
            print('Selamat datang, {}! mempersiapkan lingkungan pembicaraan...'.format(self.name))
            time.sleep(1)
            
            
            send = Send(self.sock, self.name)
            
            receive = Receive(self.sock, self.name)
            
            send.start()
            receive.start()
            
            self.sock.sendall('Server: {} baru saja memasuki pembicaraan! Sapa dia!'.format(self.name).encode('ascii'))
            print("\rSudah siap! Tinggalkan chatroom")
            
            print('{}: '.format(self.name), end='')
            
            return receive
      def send(self, textInput):
            
            message = textInput.get()
            textInput.delete(0, tk.END)
            self.messages.insert(tk.END, '{}: {}'.format(self.name, message))
            
            
            if message == "QUIT":
                  self.sock.sendall(('Server: {} sudah meninggalkan pembicaraan.'.format(self.name).encode('ascii')))
                  
                  print('\nMencoba keluar....')
                  self.sock.close()
                  os.exit(0) 
                  
                  
            else:
                 self.sock.sendall('{}: {}'.format(self.name, message).encode('ascii'))
                  
     
def main(host, port):
      #Initialize and run GUI
      
      client = Client(host, port)
      receive = client.start()
      
      window = tk.Tk()
      window.title("Chatroom")
      
      fromMessage = tk.Frame(master=window)
      scrollBar = tk.Scrollbar(master = fromMessage)
      messages = tk.Listbox(master=fromMessage, yscrollcommand=scrollBar.set)
      scrollBar.pack(side=tk.RIGHT, fill=tk.Y, expand=False)
      messages.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
      
      client.messages = messages
      receive.messages = messages
      
      fromMessage.grid(row=0, column=0, columnspan=2, sticky="nsew")
      fromEntry = tk.Frame(master=window)
      textInput = tk.Entry(master=fromEntry)
      
      textInput.pack(fill=tk.BOTH, expand=True)
      textInput.bind("<Return>", lambda x: client.send(textInput))
      
      textInput.insert(0, "Tulis pesan anda disini.")
      
      btnSend = tk.Button(
            master=window,
            text='Send',
            command = lambda: client.send(textInput)
      )
      
      fromEntry.grid(row=1, column=0, padx=10, sticky="ew")
      btnSend.grid(row=1, column=1, pady=10, sticky="ew")
      
      window.rowconfigure(0, minsize=500, weight=1)
      window.rowconfigure(1, minsize=50, weight=0)
      window.columnconfigure(0, minsize=500, weight=1)
      window.columnconfigure(1, minsize=200, weight=0)
      
      window.mainloop()
      
if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Chatroom Server")
  parser.add_argument('host', help='Interface the server listens at')
  parser.add_argument('-p', metavar='PORT', type=int, default=1060, help='TCP port (default 1060)')
    
  args = parser.parse_args()
  
  main(args.host, args.p)
      
      
      
                   