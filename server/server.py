# -*- coding:utf8 -*-
import os
import time
import json
import requests
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

username = "k5bs2MYq7Ivp*****************" #Hue ユーザー名

ip = "192.168.2.87"
HUE_API = 'http://'+ip+'/api/'+username+'/lights'

b_alert_on = False
x = 200
y = 200
volume = 255

state = [1,2,3]

NO_POST = False

def customCallback(client, userdata, message):
    print('Received a new message: ')
    print(message.payload)
    msg = eval(message.payload)
    print('from topic: ')
    print(message.topic)
    print('--------------\n\n')
    if "message" in msg.keys():
        if "volume" in msg["message"]:
            global volume
            volume = max(0,min(255,int(255 * int(msg["message"].split(":")[1]) / 400.)))
            for i in state:
                if not NO_POST:
                    requests.put(HUE_API + '/'+str(i)+'/state', json = {"on":True, "bri":volume, "xy":[x/400., y/400.]})
            
        if "drag" in msg["message"]:
            global x
            global y
            x = int(msg["message"].split(":")[1])
            y = int(msg["message"].split(":")[2])
            print(x/400.,y/400.)
            for i in state:
                if not NO_POST:
                    requests.put(HUE_API + '/'+str(i)+'/state', json = {"on":True, "bri":volume, "xy":[x/400., y/400.]})

        if "clickButton1" == msg["message"]:
            for i in state:
                if not NO_POST:
                    requests.put(HUE_API + '/'+str(i)+'/state', json = {"on":True, "bri":255, "xy":[0.35, 0.35]})

        if "clickAlertOn" == msg["message"]:
            global b_alert_on
            b_alert_on = True

        if "clickAlertOff" == msg["message"]:
            global b_alert_on
            b_alert_on = False

        if "clickButton2" == msg["message"]:
            for i in state:
                if not NO_POST:
                    requests.put(HUE_API + '/'+str(i)+'/state', json = {"on":False})

print(os.getcwd())
print(os.path.dirname(__file__))

# For certificate based connection
myMQTTClient = AWSIoTMQTTClient('myClientID') # 適当な値でOK
myMQTTClient.configureEndpoint('a1gbwzf7o***********iot.us-west-2.amazonaws.com', 8883) # 管理画面で確認
myMQTTClient.configureCredentials(os.path.join(os.path.dirname(__file__),'data/rootCA.pem'),
 os.path.join(os.path.dirname(__file__),'data/**********-private.pem.key'),
 os.path.join(os.path.dirname(__file__),'data//**********--certificate.pem.crt'))
myMQTTClient.configureOfflinePublishQueueing(-1) # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2) # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10) # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5) # 5 sec
myMQTTClient.connect()
print("server start")
while True:
    if 0:
        try:
            myMQTTClient.subscribe("myTopic", 1, customCallback)
        except KeyboardInterrupt:
            print("ctrl+c")
            break
        except:
            print("subscribe error")
    else:
        myMQTTClient.subscribe("myTopic", 1, customCallback)

    print("loop")
    global b_alert_on
    if b_alert_on:
        print("alert")
        for i in state:
            if not NO_POST:
                requests.put(HUE_API + '/'+str(i)+'/state', json = {"on":True, "bri":volume, "transitiontime":5, "xy":[0.575, 0.1875]})
        #requests.put(HUE_API + '/1/state', json = {"on":True, "bri":0, "transitiontime":0, "xy":[0.5, 0.5]})
        #print("off")
        time.sleep(0.1)
        for i in state:
            if not NO_POST:
                requests.put(HUE_API + '/'+str(i)+'/state', json = {"on":True, "bri":volume, "transitiontime":5, "xy":[0.4575, 0.445]})
        #requests.put(HUE_API + '/1/state', json = {"on":True, "bri":0, "transitiontime":0, "xy":[0.5, 0.5]})
        #print("off")
        time.sleep(0.1)
        for i in state:
            if not NO_POST:
                requests.put(HUE_API + '/'+str(i)+'/state', json = {"on":True, "bri":volume, "transitiontime":5, "xy":[0.215, 0.27]})
        #requests.put(HUE_API + '/1/state', json = {"on":True, "bri":0, "transitiontime":0, "xy":[0.5, 0.5]})
        #print("off")
        time.sleep(0.1)
