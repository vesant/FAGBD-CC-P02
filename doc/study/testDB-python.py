import sqlite3  

# create a database named backup
cnt = sqlite3.connect("doc/study/db/backup.db")  

# drop table if exists query
cnt.execute('''DROP TABLE IF EXISTS test;''')

# create a table named test
cnt.execute('''CREATE TABLE test(
NAME TEXT,
POINTS INTEGER,
ACCURACY REAL);''')

# insert in default order
cnt.execute('''INSERT INTO test(NAME, POINTS, ACCURACY) VALUES(
'Count Inversion',20,80.5);''')

# commit the transaction
cnt.commit()

# optional: close the connection
cnt.close()