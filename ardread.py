import serial
ser = serial.Serial('/dev/ttyACM0', 57600)
c=0

import MySQLdb

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="root",
                     db="cabins")

db.autocommit(True)

cur=db.cursor()

users={
      0:'not Logged In',
      1212:'tony',
      2121:'natasha',
      1122:'bruce',
      2212:'steve',
}

while True:
     val= ser.readline()
     data=val.split(" ",4);
     cbn=int(data[1])
     act=int(data[2])
     temp=float(data[3])
     id=int(data[4])
     if id in users:
        usr=users[id]
     else:
        usr='Unknown'

 #    cur = db.cursor()
 #    cur.execute("SELECT name FROM  users WHERE room='room "+"'str(cbn)+"'")
 #    for row in cur.fetchall():
 #     name =row[0]
     sqlcmd2="UPDATE users SET room='room "+str(cbn)+"' WHERE name='"+usr+"'"
     sqlcmd1="UPDATE users SET room='outer space' WHERE room='room "+str(cbn)+"'"
#     print sqlcmd1
#     print sqlcmd2
     cur.execute(sqlcmd1)
 #    cur.close()
#     cur2 = db.cursor()
     cur.execute(sqlcmd2)
#     db.close()


     txt=("Cabin:"+data[1]+"\t Activity:"+data[2]+"\t Temperature:"+data[3]+"\t ID:"+str(id)+"\t User:"+usr+"\n")
     #print(txt)
     if c>=27:
        f = open('/var/www/html/logs.txt', 'w')
        f.write(txt)
        f.close()
        c=0
     f = open('/var/www/html/logs.txt', 'a')
     f.write(txt)
     f.close()
     c+=1
