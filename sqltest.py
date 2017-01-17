import MySQLdb

db = MySQLdb.connect(host="localhost",   
                     user="root",        
                     passwd="root", 
                     db="cabins")      


cur = db.cursor()


cur.execute("SELECT name FROM  users WHERE room='room 1'")

for row in cur.fetchall():
    print row[0]

db.close()


