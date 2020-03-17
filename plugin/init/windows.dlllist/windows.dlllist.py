import sqlite3
import os
import pathlib

path = os.getcwd() + "/plugin/init/windows.dlllist/windows.dlllist.txt"
path = pathlib.Path(path)
f = open(path, 'r', encoding='utf-8')
t = f.read()
t = t.replace('Volatility 3 Framework 1.0.0-beta.1','')
t = t.replace('PID	Process	Base	Size	Name	Path','')
t = t.replace('\n\n',"\t")
t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
my_list = t.split('\t')
result = [my_list[i * 6:(i + 1) * 6] for i in range((len(my_list) + 5) // 6 )] 
print(result) 

conn = sqlite3.connect("analyze.db")
cur = conn.cursor()
cur.execute("create table dlllist (PID int, Process text, Base text, Size text, Name text, Path text)")

cur.executemany("insert into dlllist values (?, ?, ?, ?, ?, ?)", result)
conn.commit()

cur.execute('select * from dlllist')
for row in cur:
    print(row)

conn.close()