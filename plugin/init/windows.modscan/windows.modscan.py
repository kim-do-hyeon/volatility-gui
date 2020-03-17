import sqlite3
import os
import pathlib

path = os.getcwd() + "/plugin/init/windows.modscan/windows.modscan.txt"
path = pathlib.Path(path)
f = open(path, 'r', encoding='utf-8')
t = f.read()
t = t.replace('Volatility 3 Framework 1.0.0-beta.1','')
t = t.replace('Offset	Base	Size	Name	Path','')
t = t.replace('\n\n',"\t")
t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
my_list = t.split('\t')
print(my_list)
result = [my_list[i * 5:(i + 1) * 5] for i in range((len(my_list) + 4) // 5 )] 
print(result) 

conn = sqlite3.connect("analyze.db")
cur = conn.cursor()
cur.execute("create table modscan (Offset text, Base text, Size text, Name text, Path text)")

cur.executemany("insert into modscan values (?, ?, ?, ?, ?)", result)
conn.commit()

cur.execute('select * from modscan')
for row in cur:
    print(row)

conn.close()