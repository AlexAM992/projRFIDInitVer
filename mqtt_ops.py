import paho.mqtt.client as mqtt
import time

BROKER="192.168.15.12" #probalby need to change the ip and port
TOPIC="projRFID/access"

def MQTT_Session(status):
    #first create client
    client = mqtt.Client()
    client.connect("192.168.15.12",1883,60) # local host needs to be mounted in rbpi, port and keepalive time
    #sleep for a sec
    time.sleep(1)
    #publish the topic and the value
    client.publish(TOPIC,status)
    client.disconnect()


    






    
