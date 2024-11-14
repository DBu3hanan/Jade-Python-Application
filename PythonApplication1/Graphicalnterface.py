import os
import tkinter as tk
from tkinter import Menu
import JADEFunctions

def read_guidelines():
    JADEFunctions.clear()
   
    guidelines_text = (
        "\t\t\t SYSTEM GUIDELINES\n"
        "WELCOME TO THE GUIDELINES SCREEN OF THE JADE APPLICATION\n\n"
        "User Account Management:\n"
        "1. Register Account: To create a new account, you can use the Register Account option.\n"
        "2. Login: To log in to your account, you can use the Login option.\n"
        "3. Exit: To exit the application, you can use the Exit option.\n"
        "4. Users can create, update, view, and delete their accounts.\n\n"
        "User Support:\n"
        "1. Read Guidelines: To read the guidelines, you can use the Read Guidelines option."
    )
    
    guidelines_label.config(text=guidelines_text)
      # Clear the About text
    about_text_label.config(text="")

def about_jade():
    JADEFunctions.clear()

    about_text = (
        
        "ABOUT JADE\n\n"
        "This application is developed to support the Jamaican Association for Debating and Empowerment."
    )

    about_text_label.config(text=about_text)
    guidelines_label.config(text="")  # Clear the Guidelines text

# Create the main Tkinter window
root = tk.Tk()
root.title("JADE")
root.geometry("600x450")  # Width x Height
root.config(bg="white") #change colour


# Menu setup
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_command(label='Reload...' , command=root.update)  # `update` won’t reload; custom reload is recommended
filemenu.add_command(label='Exit', command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About', command=about_jade)
helpmenu.add_command(label='View Guidelines', command=read_guidelines)

adminmenu = Menu(menu)
menu.add_cascade(label='Adminstrator', menu=adminmenu)
adminmenu.add_command(label='Login', command=about_jade)

subjectexpertmenu = Menu(menu)
menu.add_cascade(label='Subject Expert', menu=subjectexpertmenu)
subjectexpertmenu.add_command(label='Login', command=about_jade)

# Label to display the guidelines text
guidelines_label = tk.Label(root, text="", justify="left", font=("Times New Roman", 10), wraplength=550, bg="white")
guidelines_label.pack()

# Label to display the About text
about_text_label = tk.Label(root, text="", justify="left", font=("Times New Roman", 10), wraplength=550, bg="white")
about_text_label.pack()

    #too much space between here 
# Label to display the main title
title_label = tk.Label(root, text='\n\n\nJamaican Association for Debating and Empowerment', font=("Times New Roman", 16), bg="white")
title_label.pack(pady=1)


    #too much space between here 
# Label for the title
title_label = tk.Label(root, text="User Main Menu Screen", font=("Times New Roman", 16),bg="white")
title_label.pack(pady=5)
    #too much space between here 

button1 = JADEFunctions.CustomButton(root, text='Register New Account')
button1.pack(pady=5)

button2 = JADEFunctions.CustomButton(root, text='Login')
button2.pack(pady=5)

button3 = JADEFunctions.CustomButton(root, text='Edit User Login')
button3.pack(pady=5)

button4 = JADEFunctions.CustomButton(root, text='Review Feedback')
button4.pack(pady=5)

button5 = JADEFunctions.CustomButton(root, text='Assign Roles')
button5.pack(pady=5)

root.mainloop()

