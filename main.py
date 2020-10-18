# -*- coding:utf8 -*-

import time
import json
import requests
import tkinter
from tkinter import ttk, scrolledtext

"""
 How to compile 
 py2applet --make-setup test.py
 python setup.py py2app
"""
username = "**********************" #ここにユーザー名いれる

ip = "192.168.2.87" #Hue BridgeのIPアドレス

HUE_API = 'http://'+ip+'/api/'+username+'/lights'

state = [1,2,3]

NO_POST = False
SLOW_LEVEL = 0

def post(jsonData):
    if not NO_POST:
        for i in state:
            requests.put(HUE_API + '/'+str(i)+'/state', json = jsonData)
    return

class GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('hue controller')
        self.main_window.geometry('500x500')

        self.b_alert_on = False

        self.button1 = ttk.Button(text="CLEAR")
        self.button1.pack(expand = True)
        self.button1.bind("<Button-1>",self.clickButton1)

        self.button2 = ttk.Button(text="CLEAR SLOW")
        self.button2.pack(expand = True)
        self.button2.bind("<Button-1>",self.clickButton2)

        self.button4 = ttk.Button(text="FADE")
        self.button4.pack(expand = True)
        self.button4.bind("<Button-1>",self.clickButton4)

        self.buttonAlertOn = ttk.Button(text="FLASH ON")
        self.buttonAlertOn.pack(expand = True)
        self.buttonAlertOn.bind("<Button-1>",self.clickAlertOn)

        self.buttonAlertOff = ttk.Button(text="FLASH OFF")
        self.buttonAlertOff.pack(expand = True)
        self.buttonAlertOff.bind("<Button-1>",self.clickAlertOff)

        self.button3 = ttk.Button(text="Exit")
        self.button3.pack(expand = True)
        self.button3.bind("<Button-1>",self.clickButton3)


    def clickButton1(self,event):
        print("send clickButton1")
        post({"on":True, "bri":255, "xy":[0.35, 0.35]})
        return "break"

    def clickButton2(self,event):
        print("send clickButton2")
        #post({"on":False})
        post({"on":True, "bri":255, "transitiontime":300, "xy":[0.35, 0.35]})
        return "break"

    def clickButton4(self,event):
        print("send clickButton4")
        post({"on":True, "bri":180, "xy":[0.39,0.39]})
        return "break"

    def clickAlertOn(self,event):
        print("send clickAlertOn")
        self.b_alert_on = True
        return "break"

    def clickAlertOff(self,event):
        print("send clickAlertOff")
        self.b_alert_on = False
        post({"on":True, "bri":255, "xy":[0.35, 0.35]})
        return "break"

    def clickButton3(self,event):
        exit()
        return "break"

    def start(self):
        self.main_window.mainloop()
        return

    def update_clock(self):
        print("update")
        volume = 255
        if self.b_alert_on:
            print("alert")
            post({"on":True, "bri":230, "transitiontime":3, "xy":[weak(0.575,5), weak(0.1875,5)]})
            time.sleep(0.1)
            post({"on":True, "bri":150, "transitiontime":3, "xy":[weak(0.4575,3), weak(0.445,3)]})
            time.sleep(0.1)
            post({"on":True, "bri":volume, "transitiontime":3, "xy":[weak(0.215,2), weak(0.27,2)]})
            time.sleep(0.1)
        self.main_window.after(100, self.update_clock)

def weak(a,v = 4.0):
    return (a+0.35*(v-1))/v

def main():
    W = GUI()
    W.update_clock()
    W.start()

if __name__ == "__main__":
    main()


