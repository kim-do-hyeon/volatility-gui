import sqlite3
import os
import pathlib

path = os.getcwd() + "/plugin/init/windows.ssdt/windows.ssdt.txt"
path = pathlib.Path(path)
f = open(path, 'r', encoding='utf-8')
t = f.read()
t = t.replace('Volatility 3 Framework 1.0.0-beta.1','')
t = t.replace('Index	Address	Module	Symbol','')
t = t.replace('\n\n',"\t")
t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
my_list = t.split('\t')
result = [my_list[i * 4:(i + 1) * 4] for i in range((len(my_list) + 3) // 4 )] 

conn = sqlite3.connect("analyze.db")
cur = conn.cursor()
cur.execute("create table ssdt (num int, Address text, Module text, Symbol text)")

cur.executemany("insert into ssdt values (?, ?, ?, ?)", result)
conn.commit()

conn.close()