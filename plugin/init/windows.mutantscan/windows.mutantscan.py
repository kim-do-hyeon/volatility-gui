import sqlite3
import os
import pathlib

path = os.getcwd() + "/plugin/init/windows.mutantscan/windows.mutantscan.txt"
path = pathlib.Path(path)
f = open(path, 'r', encoding='utf-8')
t = f.read()
t = t.replace('Volatility 3 Framework 1.0.0-beta.1','')
t = t.replace('Offset	Name','')
t = t.replace('\n\n',"\t")
t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
my_list = t.split('\t')
result = [my_list[i * 2:(i + 1) * 2] for i in range((len(my_list) + 1) // 2 )] 
print(result) 

conn = sqlite3.connect("analyze.db")
cur = conn.cursor()
cur.execute("create table mutantscan (Offset text, Name text)")

cur.executemany("insert into mutantscan values (?, ?)", result)
conn.commit()

cur.execute('select * from mutantscan')
for row in cur:
    print(row)

conn.close()