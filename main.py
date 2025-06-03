import sqlite3  

# create a database named backup
cnt = sqlite3.connect("db/backup.db")  

# create a table named gfg
cnt.execute('''CREATE TABLE test(
NAME TEXT,
POINTS INTEGER,
ACCURACY REAL);''')