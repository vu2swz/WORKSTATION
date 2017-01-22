import sys
from wit import Wit
from random import randint
from pprint import pprint

import MySQLdb

db = MySQLdb.connect(host="localhost",                                  
                     user="root",                        
                     passwd="root",       
                     db="cabins")                               



import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)


greetings = ['Hello','Hola', 'Bonjour']

users={
    'room 1':'Tony',
    'room 2':'Natasha',
    'room 3':'Bruce',
    'room 4':'Steve',
}

room={
    'tony':'room 1',
    'natasha':'room 2',
    'bruce':'room 3',
    'steve':'room 4',
}

pinout={
    'room 1':2,
    'room 2':3,
    'room 3':4,
    'room 4':18,
}

fans={
    'room 1':17,
    'room 2':27,
    'room 3':22,
    'room 4':23,
}



access_token = '#####################'


def send(request, response):
    print(response['text'])

def greet(request):
    context=request['context']
    context['greets']=greetings[randint(0,2)]
#    pprint(context)
    return context


def find(request):
    entities=request['entities']
    context=request['context']
    if 'location' in entities:
     locn=entities['location'][0]['value']
    else:
     print("Couldn't obtain location")
     return
    if locn in users:
     cur = db.cursor()
     cur.execute("SELECT name FROM  users WHERE room='"+locn+"'")

     for row in cur.fetchall():
##       print row[0]
       val=row[0]
     db.close()
    else:
      val='Boo'
    context['name0']=val
    return context

def search(request):
    entities=request['entities']
    context=request['context']
   # contact=''
    if 'contact' in entities:
     contact=entities['contact'][0]['value']
     contact=contact.lower()
    else:
     print("Couldn't obtain contact name")
    if contact in room:    
     cur = db.cursor()
     cur.execute("SELECT room  FROM  users WHERE name='"+contact+"'")

     for row in cur.fetchall():
 #      print row[0]
       val=row[0]
     db.close()

    else:
     val='outer space'

    context['room']=val
    return context

def lights(request):
    entities=request['entities']
    context=request['context']
    if 'location' in entities:
     location=entities['location'][0]['value']
    elif 'contact' in entities:
     contact=entities['contact'][0]['value']
     contact=contact.lower()
     cur = db.cursor()
     cur.execute("SELECT room  FROM  users WHERE name='"+contact+"'")

     for row in cur.fetchall():
#       print row[0]
       location=row[0]
     db.close()
     context['contact']=contact
    else:
     print("Couldn't obtain location/contact")
    if 'lightVal' in entities:
     state=entities['lightVal'][0]['value']
    else:
     print("Couldn't obtain state")
    if location in pinout:
     pin=pinout[location]
    else:
     pin=0
    val=1 if state=='on' else 0
    GPIO.output(pin,val)
    time.sleep(1)
    context['lightVal']=state
    context['location']=location
    return context

def fanspeed(request):
    entities=request['entities']
    context=request['context']
    if 'location' in entities:
     location=entities['location'][0]['value']
    elif 'contact' in entities:
     contact=entities['contact'][0]['value']
     contact=contact.lower()
     cur = db.cursor()
     cur.execute("SELECT room  FROM  users WHERE name='"+contact+"'")

     for row in cur.fetchall():
#       print row[0]
       location=row[0]
     db.close()
     context['contact']=contact
    else:
     print("Couldn't obtain location/contact")
    if 'lightVal' in entities:
     state=entities['lightVal'][0]['value']
    else:
     print("Couldn't obtain state")
    if location in fans:
     pin=fans[location]
    else:
     pin=0
    val=1 if state=='on' else 0
    GPIO.output(pin,val)
    time.sleep(1)
    context['fanVal']=state
    context['location']=location
    return context


actions = {
    'send': send,
    'greet': greet,
    'find':find,
    'search':search,
    'lights':lights,
    'fanspeed':fanspeed,
}

def main(arg1):
    query=arg1;
    #query=raw_input("Query:")
    client = Wit(access_token=access_token, actions=actions)

    #client.interactive()

    msg=client.run_actions('session1',query,{})
    #pprint(msg)

    #if 'msg' in msg:
    #   print msg['msg']
    if 'type' in msg:
     while msg['type']!='stop':
      if 'msg' not in msg:
        pass
      else:
        print msg['msg']
      msg=client.run_actions('test_session',query,{})
    #  pprint(msg)


if __name__=="__main__":
  main(sys.argv[1]);
