import os,requests
from tkinter import *
from tkinter import messagebox
from dotenv import load_dotenv


load_dotenv()

FONT1 = ('Arial',13,"bold")
BUTTON_FONT = ('Arial',15,"bold")
windows = Tk()
windows.title('Weather Application')
windows.config(padx=30,pady=30)
GeoCoding_Endpoint = os.getenv('GeCoding_Endpoint')
Api_Key = os.getenv('API_KEY')
Weather_Endpoint = os.getenv('Weather_Endpoint')
# Weather_API_KEY = os.getenv('GeoCoding_API_KEY')

def get_data():
    city = city_name.get()
    country = country_name.get()
    parameters = {
        'q':(city ,country),
        'appid':Api_Key
    }
    if city =="" or country =="":
        messagebox.showerror(title='Error',message="Please don't leave any field empty")
    else:
        geocoding_response = requests.get(url=GeoCoding_Endpoint,params=parameters)
        lat = float(geocoding_response.json()[0]['lat'])
        lon = float(geocoding_response.json()[0]['lon'])
    
        weather_params = {
            'lat':lat,
            'lon':lon,
            'appid':Api_Key,
            'units':'metric'
        }
        weather_response = requests.get(url=Weather_Endpoint,params=weather_params)
        weather = weather_response.json()
        weather_condition = weather['weather'][0]['description'].title()
        weather_temp = weather['main']['temp']
        humidity = weather['main']['humidity']
        wind= float(weather['wind']['speed'])
        wind_speed = round(wind*2.237,2)
        
        messagebox.showinfo(title="Weather Information",message=f"Weather Condition:{weather_condition}\nTemp:{weather_temp}°C\nHumidity:{humidity}%\nWind Speed:{wind_speed}miles/hr")


def start():
    
    global city_name
    global country_name
    inst_1_label.config(text="")
    inst_2_label.config(text="")
    inst_3_label.config(text="")
    inst_4_label.config(text="")
    start_button.grid_remove()
    
    city_name_label = Label(text="City Name")
    city_name_label.grid(row=2,column=1)
    city_name = Entry(width=40)
    city_name.grid(row=2,column=2)
    
    country_name_label = Label(text="Country Name")
    country_name_label.grid(row=3,column=1)
    country_name = Entry(width=40)
    country_name.grid(row=3,column=2)
    
    give_data_button = Button(text='Get Data',font=BUTTON_FONT,width=15,borderwidth=10,border=5,command=get_data)
    give_data_button.grid(row=7,column=1,columnspan=2)


#Weather Image
canvas = Canvas(width=512,height=512)
weather_image = PhotoImage(file='weather_image.png')
canvas.create_image(250,245,image=weather_image)
canvas.grid(row=0,column=1,columnspan=2)

#All the instrucitons
inst_1_label = Label(text='Instruction to use Weather Application',font=FONT1)
inst_1_label.grid(row=2,column=1)
inst_2_label = Label(text='Firstly Enter the Name of the city',font=FONT1)
inst_2_label.grid(row=3,column=1)
inst_3_label = Label(text='Secondly Enter the Name of the Country ',font=FONT1)
inst_3_label.grid(row=4,column=1)
inst_4_label = Label(text='Then click on Get Data button',font=FONT1)
inst_4_label.grid(row=5,column=1)
# inst_5_label = Label(text='Now you will get your PASSWORD which you can COPY by clicking on COPY button',font=FONT1)
# inst_5_label.grid(row=6,column=1)

start_button = Button(text='Start',font=BUTTON_FONT,width=15,borderwidth=10,border=5,command=start)
start_button.grid(row=7,column=1,columnspan=2)

windows.mainloop()