import sys
import json
from pprint import pprint
from wit import Wit
from random import randint

access_token ="ERPMUCUVWFQTM3W6TKUS54E2HF2MASFQ"

greetings = ['Hello','Hola', 'Bonjour']

def send(request, response):
    print(response['text'])

def greet(request):
    context=request['context']
    context['greets']=greetings[randint(0,2)]
    return context

actions = {
    'send': send,
    'greet':greet,
}


query=sys.argv[1]
client = Wit(access_token=access_token, actions=actions)
pprint(client.converse('test_session',query,{}))

#msg=client.converse('test_session',query,{})
#while msg['type']!='stop':
#  if 'msg' not in msg:
#    pass
#  else:
#    print msg['msg']
#  msg=client.converse('test_session',query,{})

client.interactive()
