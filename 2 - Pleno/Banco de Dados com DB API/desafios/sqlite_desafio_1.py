import sqlite3

conn = sqlite3.connect(':memory:')
flag = True

if(conn and isinstance(conn, sqlite3.Connection)):
    print("Conexão realizada!")
else:
    flag = False
    print("A conexão não foi realizada!")

conn.close()
if flag:
    print("Conexão finalizada!")