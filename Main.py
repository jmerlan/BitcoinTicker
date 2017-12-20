import tkinter as tk
import json
import requests


def draw():
    global text
    frame=tk.Frame(root,width=300,height=100,relief='solid',bd=1)
    frame.place(x=10,y=10)
    root["bg"] = "black"
    root["width"] = 600
    root["height"] = 60
    text=tk.Label(frame,text='Ticker', font=("Lucida Console", 20), background="black", foreground="green")
    text.pack()


def refresher():
    global text
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    json_dump = json.dumps(r.json())
    data = json.loads(json_dump)
    text.configure(text=data['time']['updated'] + ": $" + data['bpi']['USD']['rate'])
    root.after(60000, refresher)


root = tk.Tk()
draw()
refresher()
root.mainloop()