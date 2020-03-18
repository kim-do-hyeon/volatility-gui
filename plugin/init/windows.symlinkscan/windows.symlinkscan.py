import sqlite3
import os
import pathlib

path = os.getcwd() + "/plugin/init/windows.symlinkscan/windows.symlinkscan.txt"
path = pathlib.Path(path)
f = open(path, 'r', encoding='utf-8')
t = f.read()
t = t.replace('Volatility 3 Framework 1.0.0-beta.1','')
t = t.replace('Offset	CreateTime	From Name	To Name','')
t = t.replace('\n\n',"\t")
t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
my_list = t.split('\t')
result = [my_list[i * 4:(i + 1) * 4] for i in range((len(my_list) + 3) // 4 )] 
print(result) 

conn = sqlite3.connect("analyze.db")
cur = conn.cursor()
cur.execute("create table symlinkscan (Offset text,	CreateTime text,	From_Name text,	To_Name text)")

cur.executemany("insert into symlinkscan values (?, ?, ?, ?)", result)
conn.commit()

cur.execute('select * from symlinkscan')
for row in cur:
    print(row)

conn.close()