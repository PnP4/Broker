import json;
from initDB import Database

datalink=Database();
datalink.createTable()


def handleping(msg):
    print "resending message"

def getMessageType(json_obj):
    return json_obj["MessageType"]

def doRegister(json_obj):
    server=json_obj["message"]["serverip"]+":"+str(json_obj["message"]["port"])
    datalink.insertRegistration(server,json_obj["message"]["topic"])

def handlemessage(msg):
    parsed_json = json.loads(msg)
    msgtype=getMessageType(parsed_json)
    print msgtype;

    if(msgtype=="register"):
        doRegister(parsed_json)
    elif (msgtype=="ping"):
        handleping(parsed_json)

json_string = '{"message": {"serverip":"10.10.10.100","topic":"FFT","port":80}, "MessageType":"register"}'
handlemessage(json_string);




