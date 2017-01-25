import sqlite3

conn = sqlite3.connect('Messages/chat.db')
c = conn.cursor()

db = sqlite3.connect('master.db')
d = db.cursor()

d.execute('create table messages(date text, body text, )')

db.commit()
