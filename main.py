import tkinter as tk
import random
# main window
root = tk.Tk()
root.title("Chat-App")

# widget

label = tk.Label(root, text="Hello there !")
label.pack()
def click():
      label.config(text="Tombol Ditekan!")

      
button = tk.Button(root, text="Press This", command=click)

button.pack()

root.mainloop()