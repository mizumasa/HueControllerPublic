# -*- coding:utf8 -*-

import time
import json
import requests
import tkinter
from tkinter import ttk, scrolledtext
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

"""
 How to compile 
 py2applet --make-setup test.py
 python setup.py py2app

"""

class GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('hue controller')
        self.main_window.geometry('500x800')
        self.press = False
        self.press2 = False

        self.canvas = tkinter.Canvas(
        self.main_window, # キャンバスの作成先アプリ
        width = 400, # キャンバスの横サイズ
        height = 400, # キャンバスの縦サイズ
        bg = "white" # キャンバスの色
        )
        self.canvas.pack()

        self.canvas2 = tkinter.Canvas(
        self.main_window, # キャンバスの作成先アプリ
        width = 400, # キャンバスの横サイズ
        height = 50, # キャンバスの縦サイズ
        bg = "blue" # キャンバスの色
        )
        self.canvas2.pack()

        self.button1 = ttk.Button(text="ON")
        self.button1.pack()
        self.button1.bind("<Button-1>",self.clickButton1)

        self.button2 = ttk.Button(text="OFF")
        self.button2.pack()
        self.button2.bind("<Button-1>",self.clickButton2)

        self.buttonAlertOn = ttk.Button(text="Alert ON")
        self.buttonAlertOn.pack()
        self.buttonAlertOn.bind("<Button-1>",self.clickAlertOn)

        self.buttonAlertOff = ttk.Button(text="Alert OFF")
        self.buttonAlertOff.pack()
        self.buttonAlertOff.bind("<Button-1>",self.clickAlertOff)

        self.button3 = ttk.Button(text="Exit")
        self.button3.pack()
        self.button3.bind("<Button-1>",self.clickButton3)

        self.canvas.bind(
            "<Motion>", # 受付けるイベント
            self.mouse_move_func # そのイベント時に実行する関数
        )

        self.canvas.bind(
            "<ButtonPress>", # 受付けるイベント
            self.mouse_click_func # そのイベント時に実行する関数
        )

        self.canvas.bind(
            "<ButtonRelease>", # 受付けるイベント
            self.mouse_release_func # そのイベント時に実行する関数
        )

        self.canvas2.bind(
            "<Motion>", # 受付けるイベント
            self.mouse_move_func2 # そのイベント時に実行する関数
        )

        self.canvas2.bind(
            "<ButtonPress>", # 受付けるイベント
            self.mouse_click_func2 # そのイベント時に実行する関数
        )

        self.canvas2.bind(
            "<ButtonRelease>", # 受付けるイベント
            self.mouse_release_func2 # そのイベント時に実行する関数
        )

        self.setupAWSIoT()
    
    def setupAWSIoT(self):
        self.myMQTTClient = AWSIoTMQTTClient('myClientID2') # 適当な値でOK
        self.myMQTTClient.configureEndpoint('a1gbwzf7otibfp-ats.iot.us-west-2.amazonaws.com', 8883) # 管理画面で確認
        self.myMQTTClient.configureCredentials('data/rootCA.pem', 'data/fd35544055-private.pem.key', 'data/fd35544055-certificate.pem.crt')
        self.myMQTTClient.configureOfflinePublishQueueing(-1) # Infinite offline Publish queueing
        self.myMQTTClient.configureDrainingFrequency(2) # Draining: 2 Hz
        self.myMQTTClient.configureConnectDisconnectTimeout(10) # 10 sec
        self.myMQTTClient.configureMQTTOperationTimeout(5) # 5 sec
        self.myMQTTClient.connect()

    def sendMessage(self,message):
        self.myMQTTClient.publish("myTopic2", json.dumps({'message' : message}), 1)

    def mouse_move_func(self,event):
        # 現在のマウスの位置
        x = event.x
        y = event.y

        # マウスボタンが押されている時だけ円を描画
        if self.press:
            self.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill = "blue", width=0)
            print("drag "+str(x)+":"+str(y))
            self.sendMessage("drag:"+str(x)+":"+str(y))

    def mouse_click_func(self,event):
        # マウスボタンが押された
        self.press = True

    def mouse_release_func(self,event):
        # マウスボタンが離された
        self.press = False


    def mouse_move_func2(self,event):
        if self.press2:
            x = event.x
            print("volume "+str(x))
            self.sendMessage("volume:"+str(x))
        return

    def mouse_click_func2(self,event):
        self.press2 = True
        return

    def mouse_release_func2(self,event):
        self.press2 = False
        return


    def clickButton1(self,event):
        print("send clickButton1")
        self.sendMessage("clickButton1")
        return "break"

    def clickButton2(self,event):
        print("send clickButton2")
        self.sendMessage("clickButton2")
        return "break"

    def clickAlertOn(self,event):
        print("send clickAlertOn")
        self.sendMessage("clickAlertOn")
        return "break"

    def clickAlertOff(self,event):
        print("send clickAlertOff")
        self.sendMessage("clickAlertOff")
        return "break"

    def clickButton3(self,event):
        exit()
        return "break"

    def start(self):
        self.main_window.mainloop()
        return

def main():
    W = GUI()
    W.start()

if __name__ == "__main__":
    main()


