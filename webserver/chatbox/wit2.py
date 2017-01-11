import sys
from wit import Wit
from random import randint
from pprint import pprint

greetings = ['Hello','Hola', 'Bonjour']

access_token = ########################

def send(request, response):
    print(response['text'])

def greet(request):
    context=request['context']
    context['greets']=greetings[randint(0,2)]
    return context
actions = {
    'send': send,
    'greet': greet,
}

query=sys.argv[1]
#query=raw_input("Query:")
client = Wit(access_token=access_token, actions=actions)

#client.interactive()

#pprint(client.converse('test_session',query,{}))

msg=client.converse('test_session',query,{})
if 'metadata' in msg:
   print msg['metadata']
if 'msg' in msg:
   print msg['msg']
#while msg['type']!='stop':
#  if 'msg' not in msg:
#    pass
#  else:
#    print msg['msg']
#  msg=client.converse('test_session',query,{})

