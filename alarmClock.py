from tkinter import*
import datetime
from threading import*
import webbrowser
import random
from time import sleep
import time
from time import strftime



root = Tk()
root.title('Alarm Clock')
root.geometry("400x400")
root.config(background = "navajo white")




def Threading():
    t1= Thread(target=alarm)
    t1.start()


def time():
    string = strftime("%H:%M:%S")
    clock.config(text = string)
    clock.after(1000, time)


def randomVideo():
    with open("youtube_links.txt","r") as file:
        allText = file.read()
        line = allText.split('\n')
        link = random.choice(line)
    return link


def alarm():
    
    link = randomVideo()
    while True:
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)  

        if current_time== set_alarm_time:
            webbrowser.open(link)
            text1 = Label(root, font = ('arial 20 bold'), text = "Time up", fg = 'black').grid(row=8, column=2) 
            text2 = Label(root, font = ('arial 10 bold'), text = "Playing a random youtube video...", fg = 'hotpink1').grid(row=9, column = 2)
            
  


Label(root, text='Alarm Clock', font=('Helvatica 20 bold'), fg='black', bg='navajo white').grid(row=1, column=2, padx=20)


clock = Label(root, font = ('arial 30'), fg = 'black', bg= "lavender blush")
clock.grid(row=3, column= 2, padx=10, pady=40)


Label(root, text='Set Alarm:', font=('Helvatica 15 bold'), fg ='medium violet red' ,bg='navajo white').grid(row=5, column =1, padx= 0, pady= 20)


frame = Frame(root, background= 'yellow')
frame.grid(row=5, column=2, padx=0, pady=20)

hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
        )
hour.set(hours[0])
 
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)
 
minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0])
 
mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)
 
second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
second.set(seconds[0])
 
secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)


Button(root,text="Done",font=("Helvetica 15"),bg ='green3', fg= 'white',command=Threading).grid(row=7, column=2, pady= 10)
 
time()
root.mainloop()

