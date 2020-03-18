import sqlite3
import os
import pathlib

path = os.getcwd() + "/plugin/init/windows.procdump/windows.procdump.txt"
path = pathlib.Path(path)
f = open(path, 'r', encoding='utf-8')
t = f.read()
t = t.replace('Volatility 3 Framework 1.0.0-beta.1','')
t = t.replace('PID	Process	Result','')
t = t.replace('\n\n',"\t")
t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
my_list = t.split('\t')
result = [my_list[i * 3:(i + 1) * 3] for i in range((len(my_list) + 2) // 3 )] 

conn = sqlite3.connect("analyze.db")
cur = conn.cursor()
cur.execute("create table procdump (PID int, Process text, Result text)")

cur.executemany("insert into procdump values (?, ?, ?)", result)
conn.commit()

conn.close()