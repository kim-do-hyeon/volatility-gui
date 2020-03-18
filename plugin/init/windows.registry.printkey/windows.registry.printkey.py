import sqlite3
import os
import pathlib

path = os.getcwd() + "/plugin/init/windows.registry.printkey/windows.registry.printkey.txt"
path = pathlib.Path(path)
f = open(path, 'r', encoding='utf-8')
t = f.read()
t = t.replace('Volatility 3 Framework 1.0.0-beta.1','')
t = t.replace('Last Write Time	Hive Offset	Type	Key	Name	Data	Volatile','')
t = t.replace('\n\n',"\t")
t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
my_list = t.split('\t')
result = [my_list[i * 7:(i + 1) * 7] for i in range((len(my_list) + 6) // 7 )] 

conn = sqlite3.connect("analyze.db")
cur = conn.cursor()
cur.execute("create table registry_printkey (Last_Write_Time text, Hive_Offset text, Type text, Key text, Name text, Data text, Volatile text)")

cur.executemany("insert into registry_printkey values (?, ?, ?, ?, ?, ?, ?)", result)
conn.commit()

conn.close()