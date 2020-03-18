import sqlite3
import os
import pathlib

path = os.getcwd() + "/plugin/init/windows.svcscan/windows.svcscan.txt"
path = pathlib.Path(path)
f = open(path, 'r', encoding='utf-8')
t = f.read()
t = t.replace('Volatility 3 Framework 1.0.0-beta.1','')
t = t.replace('Offset	Order	Pid	Start	State	Type	Name	Display	Binary','')
t = t.replace('\n\n',"\t")
t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
my_list = t.split('\t')
result = [my_list[i * 9:(i + 1) * 9] for i in range((len(my_list) + 8) // 9 )] 

conn = sqlite3.connect("analyze.db")
cur = conn.cursor()
cur.execute("create table svcscan (Offset text, order_text text, PID text, Start text, State text, Type text, Name text, Display text, Binary text)")

cur.executemany("insert into svcscan values (?, ?, ?, ?, ?, ?, ?, ?, ?)", result)
conn.commit()

conn.close()