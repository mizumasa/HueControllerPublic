# -*- coding:utf8 -*-
import time
import json
import tkinter
from tkinter import ttk, scrolledtext
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

class GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('server')
        self.main_window.geometry('500x500')

        self.button1 = ttk.Button(text="ON")
        self.button1.pack()
        self.button1.bind("<Button-1>",self.clickButton1)

        self.button2 = ttk.Button(text="OFF")
        self.button2.pack()
        self.button2.bind("<Button-1>",self.clickButton2)

        self.button3 = ttk.Button(text="Exit")
        self.button3.pack()
        self.button3.bind("<Button-1>",self.clickButton3)

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
        print("MQTT connect done")

    def customCallback(self, client, userdata, message):
        print('Received a new message: ')
        print(message.payload)
        print('from topic: ')
        print(message.topic)
        print('--------------\n\n')

    def clickButton1(self,event):
        self.sendMessage("clickButton1")
        return "break"

    def clickButton2(self,event):
        self.sendMessage("clickButton2")
        return "break"

    def clickButton3(self,event):
        exit()
        return "break"

    def update(self):
        print("update")
        self.myMQTTClient.subscribe("myTopic", 1, self.customCallback)
        self.main_window.after(50, self.update)

    def start(self):
        #self.main_window.after(50, self.update)
        #self.main_window.mainloop()
        while 1:
            self.myMQTTClient.subscribe("myTopic", 1, self.customCallback)
        return

def main():
    W = GUI()
    W.start()

if __name__ == "__main__":
    main()
