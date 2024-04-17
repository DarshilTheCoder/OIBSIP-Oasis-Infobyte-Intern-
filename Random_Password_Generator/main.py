from tkinter import *
from tkinter import messagebox
from generate_password import GeneratePassword
import pyperclip


FONT1 = ('Arial',13,"bold")
BUTTON_FONT = ('Arial',15,"bold")
windows = Tk()
windows.title('Random Password Generator')
windows.config(padx=30,pady=30)



#functions to generates passwords
def simple_password_generator():
    global password
    try:
        password_length = int(password_length_input.get())
    except ValueError:
        messagebox.showerror(title='Value Error',message="Please enter the length of password")
    else:
        password_generator = GeneratePassword(password_length=password_length)
        password = password_generator.simple_password()
        
        generated_password.delete(0,END)
        generated_password.insert(0,password)

def medium_password_generator():
    global password
    try:
        password_length = int(password_length_input.get())
    except ValueError:
        messagebox.showerror(title='Value Error',message="Please enter the length of password")
    else:
        password_generator = GeneratePassword(password_length=password_length)
        password = password_generator.medium_password()
        
        generated_password.delete(0,END)
        generated_password.insert(0,password)
        
def strong_password_generator():
    global password
    try:
        password_length = int(password_length_input.get())
        print(password_length)
    except ValueError:
        messagebox.showerror(title='Value Error',message="Please enter the length of password")
    else:
        password_generator = GeneratePassword(password_length=password_length)
        password = password_generator.strong_password()
        
        generated_password.delete(0,END)
        generated_password.insert(0,password)

def copy_password():
    pyperclip.copy(password)
#function to start 
def start():
    global password_length_input
    global generated_password
    how_to_use_label.config(text="")
    inst_1_label.config(text="")
    inst_2_label.config(text="")
    inst_3_label.config(text="")
    inst_4_label.config(text="")
    inst_5_label.config(text="")
    start_button.grid_remove()
    
    password_length_label = Label(text="Enter Password length",font=FONT1)
    password_length_label.grid(row=2,column=1)
    password_length_input = Entry(width=40)
    password_length_input.grid(row=2,column=2)
    
    simple_button = Button(text='SIMPLE',font=FONT1,command=simple_password_generator)
    simple_button.grid(row=4,column=1)
    medium_button = Button(text='MEDIUM',font=FONT1,command=medium_password_generator)
    medium_button.grid(row=5,column=1)
    strong_button = Button(text='STRONG',font=FONT1,command=strong_password_generator)
    strong_button.grid(row=6,column=1)
    
    generated_password = Entry(width=40)
    generated_password.grid(row=5,column=2)
    
    button = Button(text='Copy Password',font=FONT1,width=15,borderwidth=10,border=5,command=copy_password)
    button.grid(row=7,column=2)
    

#Random Password Generator Image
canvas = Canvas(width=512,height=512)
bmi_image = PhotoImage(file='passwordgenerator.png')
canvas.create_image(250,245,image=bmi_image)
canvas.grid(row=0,column=1,columnspan=2)

how_to_use_label = Label(text="Instruction to use Random Password Generator!!",foreground='black',font=FONT1)
how_to_use_label.grid(row=1,column=1)

#All the instrucitons
inst_1_label = Label(text='First insert the length of password you want',font=FONT1)
inst_1_label.grid(row=2,column=1)
inst_2_label = Label(text='Click on SIMPLE it will generate ALPHABETIC password of given length',font=FONT1)
inst_2_label.grid(row=3,column=1)
inst_3_label = Label(text='Click on MEDIUM it will generate ALPHANUMERIC password of given length ',font=FONT1)
inst_3_label.grid(row=4,column=1)
inst_4_label = Label(text='Click on STRONG it will generate ALPHANUMERIC+SPECIAL SYMBOL password of given length',font=FONT1)
inst_4_label.grid(row=5,column=1)
inst_5_label = Label(text='Now you will get your PASSWORD which you can COPY by clicking on COPY button',font=FONT1)
inst_5_label.grid(row=6,column=1)

start_button = Button(text='Start',font=BUTTON_FONT,width=15,borderwidth=10,border=5,command=start)
start_button.grid(row=7,column=1,columnspan=2)

windows.mainloop()