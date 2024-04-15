from tkinter import *
from tkinter import messagebox


FONT1 = ('Arial',10,"bold")
BUTTON_FONT = ('Arial',15,"bold")
windows = Tk()
windows.title('BMI Calculator')
windows.config(padx=30,pady=30)

#Main Function
def calculate_bmi():
    try:
        name = name_input.get()
        weight = float(weight_input.get())
        height = float(height_input.get())
        isOk = messagebox.askokcancel(title="Information",message=f"Is given information is perfect? \n Name = {name} \n Weight = {weight}\nHeight = {height}")
        if isOk:
            category=None
            BMI_of_person = round(weight/height**2,2)
            print(BMI_of_person)
            if BMI_of_person< 18.5:
                category = "Under Weight"
            elif 18.8<=BMI_of_person<=24.9:
                category = "Healthy Weight"
            elif 25<=BMI_of_person<29.9:
                category = "Over Weight"
            else:
                category = "Obesity"
            result_input.delete(0,END)
            result_input.insert(0,BMI_of_person)
            category_input.delete(0,END)
            category_input.insert(0,category)
            with open('datafile.csv',mode="a") as dataFile:
                dataFile.write(f"\n{name},{weight},{height},{BMI_of_person},{category}")
    except ValueError:
        messagebox.showerror(title="Information Missing",message="Please don't leave any  field empty!")
    
def start():
    global weight_input
    global height_input
    global result_input
    global name_input
    global category_input
    how_to_use_label.config(text="")
    inst_1_label.config(text="")
    inst_2_label.config(text="")
    inst_3_label.config(text="")
    inst_4_label.config(text="")
    inst_5_label.config(text="")
    
    name_label = Label(text='Enter Your Name',font=FONT1)
    name_label.grid(row=1,column=1)
    name_input = Entry(width=40)
    name_input.grid(row=1,column=2)
    
    weight_label = Label(text='Enter Your Weight',font=FONT1)
    weight_label.grid(row=2,column=1)
    weight_input= Entry(width=40)
    weight_input.grid(row=2,column=2)
    
    height_label = Label(text='Enter Your Height',font=FONT1)
    height_label.grid(row=3,column=1)
    height_input = Entry(width=40)
    height_input.grid(row=3,column=2)
    
    result_label = Label(text='Result',font=FONT1)
    result_label.grid(row=4,column=1)
    result_input = Entry(width=20)
    result_input.grid(row=4,column=2)
    
    category_label = Label(text='Category',font=FONT1)
    category_label.grid(row=5,column=1)
    category_input = Entry(width=20)
    category_input.grid(row=5,column=2)
    
    button = Button(text='Result',font=BUTTON_FONT,width=15,borderwidth=10,border=5,command=calculate_bmi)
    button.grid(row=7,column=1,columnspan=2)

#BMI Image
canvas = Canvas(width=500,height=400)
bmi_image = PhotoImage(file='BMI_image2.png')
canvas.create_image(250,200,image=bmi_image)
canvas.grid(row=0,column=1,columnspan=2)

how_to_use_label = Label(text="Instruction to use BMI Calculator!!",foreground='black',font=FONT1)
how_to_use_label.grid(row=1,column=1)

#All the instrucitons
inst_1_label = Label(text='First insert your Name',font=FONT1)
inst_1_label.grid(row=2,column=1)
inst_2_label = Label(text='Second insert your Weight',font=FONT1)
inst_2_label.grid(row=3,column=1)
inst_3_label = Label(text='Thind insert your Height in meters',font=FONT1)
inst_3_label.grid(row=4,column=1)
inst_4_label = Label(text='Founth Now click on "Calculate Button" to calculate your BMI',font=FONT1)
inst_4_label.grid(row=5,column=1)
inst_5_label = Label(text='Now you will get your results that show under which category you are falling',font=FONT1)
inst_5_label.grid(row=6,column=1)

button = Button(text='Start',font=BUTTON_FONT,width=15,borderwidth=10,border=5,command=start)
button.grid(row=7,column=1,columnspan=2)

windows.mainloop()