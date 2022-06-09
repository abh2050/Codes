import tkinter as tk
from tkinter import font
import requests
Height = 600
Width = 600

def test_function(entry):
    print("This is the Entry: ",entry)

#76fc65083d4319f9ca91ab847a8b9485
#api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid={API key}

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]["description"]
        temp = weather['main']['temp']
        final_str= 'City:  %s \nConditions: %s \n Temperature (F): %s' % (name, desc, temp)
    except:
        final_str= "There was a problem retrieving the values"

    return final_str

def get_weather(city):
    weather_key="76fc65083d4319f9ca91ab847a8b9485"
    url = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}'
    params= {'APPID': weather_key,'q':city,'units': "imperial"}
    response = requests.get(url,params=params)
    weather = response.json()
    label['text'] = format_response(weather)


root = tk.Tk()
canvas = tk.Canvas(root, height=Height, width=Width)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root,image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#80c1ff", bd=5)
frame.place(relx=0.5, rely=0.1,relwidth=0.75, relheight=0.1, anchor="n")

entry = tk.Entry(frame, font=40)
entry.place(relwidth= 0.65, relheight= 1)

button = tk.Button(root, text= "Get Weather", font=40, bg='gray',command=lambda: get_weather(entry.get()))
button.place(relx= 0.65,rely=0.1, relheight= 0.1, relwidth= 0.3)

lower_frame = tk.Frame(root,bg="#80c1ff", bd=10)
lower_frame.place(relx= 0.5, rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

label = tk.Label(lower_frame, font =('Courier',18))
label.place(relwidth=1, relheight=1)


root.mainloop()
