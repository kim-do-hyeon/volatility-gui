import sqlite3
import os
import pathlib

path = os.getcwd() + "/plugin/init/windows.handles/windows.handles.txt"
path = pathlib.Path(path)
f = open(path, 'r', encoding='utf-8')
t = f.read()
t = t.replace('Volatility 3 Framework 1.0.0-beta.1','')
t = t.replace('PID	Process	Offset	HandleValue	Type	GrantedAccess	Name','')
t = t.replace('\n\n',"\t")
t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
my_list = t.split('\t')
result = [my_list[i * 7:(i + 1) * 7] for i in range((len(my_list) + 6) // 7 )] 

conn = sqlite3.connect("analyze.db")
cur = conn.cursor()
cur.execute("create table handles (PID int, Process text, Offset text, HandleValue text, Type text, GrantedAccess text, Name text)")

cur.executemany("insert into handles values (?, ?, ?, ?, ?, ?, ?)", result)
conn.commit()

conn.close()