import json;
import initDB
def getMessageType(json_obj):
    return json_obj["MessageType"]

def doRegister(json_obj):
    initDB.insertRegistration()

def handlemessage(msg):
    parsed_json = json.loads(msg)
    msgtype=getMessageType(parsed_json)
    print msgtype;
    if(msgtype=="register"):
        doRegister(parsed_json)


json_string = '{"message": {"serverip":"10.10.10.10","service":"FFT","port":80}, "MessageType":"register"}'
handlemessage(json_string);




