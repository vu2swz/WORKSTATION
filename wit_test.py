import sys
import json
from pprint import pprint
from wit import Wit

access_token ="ERPMUCUVWFQTM3W6TKUS54E2HF2MASFQ"

def send(request, response):
    print(response['text'])

def greet():
    print "hi"
def search(context):
    return "Not Found"
def lights(context,entities):
    return "Error"
def temp(context):
    return("Error")
def identify(context):
    return "Error"

actions = {
    'send': send,
    'greet':greet,
    'search':search,
    'lights':lights,
    'temp':temp,
    'find':identify,
}


query=raw_input("Query:")
client = Wit(access_token=access_token, actions=actions)
pprint(client.run_actions('test_session',query,{}))

#msg=client.converse('test_session',query,{})
#while msg['type']!='stop':
#  if 'msg' not in msg:
#    pass
#  else:
#    print msg['msg']
#  msg=client.converse('test_session',query,{})

