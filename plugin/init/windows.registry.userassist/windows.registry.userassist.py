import sqlite3
import os
import pathlib

path = os.getcwd() + "/plugin/init/windows.registry.userassist/windows.registry.userassist.txt"
path = pathlib.Path(path)
f = open(path, 'r', encoding='utf-8')
t = f.read()
t = t.replace('Volatility 3 Framework 1.0.0-beta.1','')
t = t.replace('Hive Offset	Hive Name	Path	Last Write Time	Type	Name	ID	Count	Focus Count	Time Focused	Last Updated	Raw Data','')
t = t.replace('\n\n',"\t")
t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
my_list = t.split('\t')
result = [my_list[i * 12:(i + 1) * 12] for i in range((len(my_list) + 11) // 12 )] 

conn = sqlite3.connect("analyze.db")
cur = conn.cursor()
cur.execute("create table registry_userassist (Hive_Offset text,	Hive_Name_Path text,	Last_Write_Time text,	Type text, 	Name text,	ID text,	Count	text, Focus text, Count_Time text, Focused text,	Last_Updated text, Raw_Data text)")

cur.executemany("insert into registry_userassist values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", result)
conn.commit()

conn.close()