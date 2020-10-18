
# -*- coding: utf-8 -*-
import requests
import time

username = "M5rMBVH05MpcW87FjjBb61qkqUZ6kpHfO9gyUDMu" #takeda
username = "k5bs2MYq7IvpgC58UIPywT4L5GuHEgRil5vShOzH" #mizuochi
ip = "192.168.2.87"

HUE_API = 'http://'+ip+'/api/'+username+'/lights'

"""
requests.put(HUE_API + '/1/state', json = {"on":True, "bri":128, "xy":[0.48, 0.41]})
time.sleep(1)
requests.put(HUE_API + '/1/state', json = {"on":False})
time.sleep(1)
"""
level = 0

for i in range(100):
  level = min(level+10,255)
  requests.put(HUE_API + '/1/state', json = {"on":True, "bri":level, "transitiontime":5, "xy":[0.575, 0.1875]})
  print("on",level)
  time.sleep(0.01)
  #requests.put(HUE_API + '/1/state', json = {"on":True, "bri":0, "transitiontime":0, "xy":[0.5, 0.5]})
  #print("off")
  time.sleep(0.1)
  requests.put(HUE_API + '/1/state', json = {"on":True, "bri":level, "transitiontime":5, "xy":[0.4575, 0.445]})
  print("on",level)
  time.sleep(0.01)
  #requests.put(HUE_API + '/1/state', json = {"on":True, "bri":0, "transitiontime":0, "xy":[0.5, 0.5]})
  #print("off")
  time.sleep(0.1)
  requests.put(HUE_API + '/1/state', json = {"on":True, "bri":level, "transitiontime":5, "xy":[0.215, 0.27]})
  print("on",level)
  time.sleep(0.01)
  #requests.put(HUE_API + '/1/state', json = {"on":True, "bri":0, "transitiontime":0, "xy":[0.5, 0.5]})
  #print("off")
  time.sleep(0.1)

"""
URL: https://hub_address/api/your_username/groups/1/action
Message Body: {"alert": "select"}

"""