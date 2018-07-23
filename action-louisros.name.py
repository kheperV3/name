#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes
import time
import datetime

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

def PyString(s) :
      if s[len(s)-1] == '\0' :
            s = s[0:len(s)-1]
      return s
      
def CString(s):
      if s[len(s)-1] != '\0' :
            s = s + '\0'
      return s 

def intents_callback(hermes, intentMessage) : 
    

    if intentMessage.intent.intent_name == 'louisros:name' :
            n = ""
            hermes.publish_continue_session(intentMessage.session_id,"premier caractère",["louisros:signe"])
            v = intentMessage.slots.v.first().value 
            resul = v
      
    elif intentMessage.intent.intent_name == 'louisros:signe' :
            v = intentMessage.slots.s.first().value 
            if v != 'fin' :
                  n = n + v
                  hermes.publish_continue_session(intentMessage.session_id,"suivant",["louisros:signe"])
            else:
                  resul = n
                  
              
    
    current_session_id = intentMessage.session_id
    hermes.publish_end_session(current_session_id, resul)


if __name__ == "__main__":
    with Hermes(MQTT_ADDR) as h:           
        h.subscribe_intents(intents_callback).start()
        
