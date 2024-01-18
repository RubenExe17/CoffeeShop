import tkinter as tk
from tkinter import font
from tkinter import ttk
from tkinter.ttk import *



def starter_screen():
    global mainFrame
    root = tk.Tk()
    root.geometry("400x700")
    root.eval('tk::PlaceWindow . center')
    root.config(bg = "#2b1a04",)

        # Where teh majority of content will fit in
    mainFrame = Frame(root, style="Main.TFrame")
    # mainFrame.place(width=300, height=400, x=0, y=50)
    spacer = tk.Frame(height=30,
      bg="#2b1a04",
    )
    spacer.pack()


    greeting = tk.Label(
      text="Bean &",
      fg= "#eb8305",
      bg="#2b1a04",
      font=("Arial", 20, "bold"),
    )
    greeting.pack()

    greeting = tk.Label(
      text="Brew",
      fg= "#eb8305",
      bg="#2b1a04",
      font=("Arial", 20, "bold"),
    )
    greeting.pack()

    spacer = tk.Frame(height=30,
      bg="#2b1a04",
    )
    spacer.pack()

    h1= tk.Label(
      text="BOOK LESSON",
      fg="#eb8305",
      font=("Arial", 10, "bold"),
      bg="#2b1a04",
      
    )
    h1.pack()

    h3= tk.Label(
      text="Book your next baking lesson",
      fg="#ded7ce",
      font=("Arial", 7),
      bg="#2b1a04",
      
    )
    h3.pack()

    h2= tk.Label(
      text="Pick a Lesson",
      fg="#eb8305",
      font=("Arial", 7, "bold"),
      bg="#2b1a04",
      height=3,

    )
    h2.pack()

    e1 = tk.Entry(bd =2, bg="#2b1a04", fg="#f7f3be")  
    e1.insert(0, "Pick one of the following lessons")
    e1.pack()

    h2= tk.Label(
      text="Pick a Location",
      fg="#eb8305",
      font=("Arial", 7, "bold"),
      bg="#2b1a04",
      height=3,

    )
    h2.pack()

    e1 = tk.Entry(bd =2, bg="#2b1a04", fg="#f7f3be")  
    e1.insert(0, "Pick one of the our locations")
    e1.pack()

    h2= tk.Label(
      text="Pick a date",
      fg="#eb8305",
      font=("Arial", 7, "bold"),
      bg="#2b1a04",
      height=3,

    )
    h2.pack()

    e1 = tk.Entry(bd =2, bg="#2b1a04", fg="#f7f3be")  
    e1.insert(0, "Date")
    e1.pack()

    spacer = tk.Frame(height=20,
      bg="#2b1a04",
    )
    spacer.pack()

  
    button = tk.Button(
        command=login_screen,
        text="Pay",
        width=10,
        height=2,
        bg="#f7f3be",
        fg="#2b1a04",
        pady = 5, 
        
    )
    button.pack()
    spacer = tk.Frame(height=20,
        bg="#2b1a04",
    )
    

    root.mainloop()


def login_screen():
    # Create secondary (or popup) window.
    
    login = tk.Toplevel(
        bg = "#2b1a04",
        
        
        
    )
    # login.geometry("400x700")
    # login.title("Login")
    # root = tk.Tk()
    # root.geometry("400x700")
    # root.eval('tk::PlaceWindow . center')
    # root.config(bg = "#2b1a04",)
    #    # Where teh myjority of content will fit in
   
    
    # Create a button to close (destroy) this window.
    button_close = ttk.Button(
        login,
        text="Close window",
        command=login.destroy
    )
    button_close.place(x=75, y=75)


# # Login screen
# def login_screen():
#     global mainFrame
#     login = tk.Tk()
#     login.geometry("400x700")
#     login.eval('tk::PlaceWindow . center')
#     login.config(bg = "#2b1a04",)
#        # Where teh myjority of content will fit in
#     mainFrame = Frame(login, style="Main.TFrame")
#     # mainFrame.place(width=300, height=400, x=0, y=50)
    
#     test1= tk.Label(
#         text="hello world"
#     )
#     test1.pack()
#     login.mainloop()
# # Driver Code

starter_screen()

