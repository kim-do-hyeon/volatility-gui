import sqlite3
import os
import pathlib

path = os.getcwd() + "/plugin/init/windows.registry.hivescan/windows.registry.hivescan.txt"
path = pathlib.Path(path)
f = open(path, 'r', encoding='utf-8')
t = f.read()
t = t.replace('Volatility 3 Framework 1.2.1-beta.1','')
t = t.replace('Offset','')
t = t.replace('\n\n',"\t")
t = t.replace('\n',"\t")
t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
my_list = t.split('\t')
# result = [my_list[i * 1:(i) * 1] for i in range((len(my_list) + 1) // 1 )] 
print(my_list)
conn = sqlite3.connect("analyze.db")
cur = conn.cursor()
cur.execute("create table registry_hivescan (offset text)")
for i in range((len(my_list))):
    cur.executemany("insert into registry_hivescan values (?)", my_list)
conn.commit()

conn.close()