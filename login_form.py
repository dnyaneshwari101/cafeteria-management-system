import tkinter as tk
from tkinter import messagebox

window = tk.Tk() # defining the window
window.title('Login Form')
window.geometry('440x440') #set the size of window
window.configure(bg='lavender')

def login():
    username ="Dnyaneshwari"
    password="1234"
    if username_entry.get()==username and pass_entry.get()==password :
        #print("Login Successful!")
        messagebox.showinfo(title="Login Success",message = "Login Successful!")
    else:
        #print("Invalid username or password")
        messagebox.showinfo(title="Error", message="Wrong username or password!")

frame = tk.Frame(bg="lavender") # Frame is like a container. We keep all the widgets inside the container. It is like a small box within the box

login_label = tk.Label(frame, text="Login", bg='lavender', font=("Times New Roman", 30))

username_label = tk.Label(frame, text="Username",bg='lavender', font=("Times New Roman", 18))
username_entry = tk.Entry(frame)

pass_label= tk.Label(frame,text="Passwod : ", bg='lavender', font=("Times New Roman", 18))
pass_entry = tk.Entry(frame, show="*")

login_button = tk.Button(frame, text="Login",bg="pink" ,fg="purple", font=("Times New Roman", 18), command=login)

#placing the widgets on the screen

login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1,column=0)
username_entry.grid(row=1, column=1, pady=20)
pass_label.grid(row=2,column=0)
pass_entry.grid(row=2,column=1, pady=20)
login_button.grid(row=3,column=0, columnspan=2, pady=30) # span 2 columns

frame.pack()


window.mainloop() # loop that runs continuously. as we close the window, mainllop stops working.
# mainloop is also a blocking function