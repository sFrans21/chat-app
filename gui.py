import tkinter as tk
from tkinter import scrolledtext
import socket
import threading

class ChatAppGUI:
    def __init__(self, master):
        self.master = master
        master.title("Chat App")

        self.chat_box = scrolledtext.ScrolledText(master, width=40, height=10)
        self.chat_box.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.message_entry = tk.Entry(master, width=30)
        self.message_entry.grid(row=1, column=0, padx=5, pady=5)

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=5, pady=5)

        self.client_socket = socket.socket()
        self.host = socket.gethostname()
        self.port = 12345
        self.client_socket.connect((self.host, self.port))

        self.receive_thread = threading.Thread(target=self.receive_message)
        self.receive_thread.start()

    def send_message(self):
        message = self.message_entry.get()
        self.chat_box.insert(tk.END, "You: " + message + "\n")
        message = message.encode()
        self.client_socket.send(message)
        self.message_entry.delete(0, tk.END)

    def receive_message(self):
        while True:
            message = self.client_socket.recv(1024).decode()
            self.chat_box.insert(tk.END, "Client: " + message + "\n")

def main():
    root = tk.Tk()
    app = ChatAppGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
