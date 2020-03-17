import sqlite3
import os
import pathlib

path = os.getcwd() + "/plugin/init/windows.cmdline/windows.cmdline.txt"
path = pathlib.Path(path)
f = open(path, 'r', encoding='utf-8')
t = f.read()
t = t.replace('Volatility 3 Framework 1.0.0-beta.1','')
t = t.replace('PID	Process	Args','')
t = t.replace('\n\n',"\t")
t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
my_list = t.split('\t')
result = [my_list[i * 3:(i + 1) * 3] for i in range((len(my_list) + 2) // 3 )] 
print(result) 

conn = sqlite3.connect("analyze.db")
cur = conn.cursor()
cur.execute("create table cmdline (PID int, Process text, Args text)")

cur.executemany("insert into cmdline values (?, ?, ?)", result)
conn.commit()

cur.execute('select * from cmdline')
for row in cur:
    print(row)

conn.close()