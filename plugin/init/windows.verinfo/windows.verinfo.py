import sqlite3
import os
import pathlib

path = os.getcwd() + "/plugin/init/windows.verinfo/windows.verinfo.txt"
path = pathlib.Path(path)
f = open(path, 'r', encoding='utf-8')
t = f.read()
t = t.replace('Volatility 3 Framework 1.0.0-beta.1','')
t = t.replace('PID	Process	Base	Name	Major	Minor	Product	Build','')
t = t.replace('\n\n',"\t")
t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
my_list = t.split('\t')
result = [my_list[i * 8:(i + 1) * 8] for i in range((len(my_list) + 7) // 8 )] 

conn = sqlite3.connect("analyze.db")
cur = conn.cursor()
cur.execute("create table verinfo (PID text, Process text, Base text, Name text, Major int, Minor int, Product int, Build int)")

cur.executemany("insert into verinfo values (?, ?, ?, ?, ?, ?, ?, ?)", result)
conn.commit()

conn.close()