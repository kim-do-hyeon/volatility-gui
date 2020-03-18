import sqlite3
import os
import pathlib

path = os.getcwd() + "/plugin/init/windows.statistics/windows.statistics.txt"
path = pathlib.Path(path)
f = open(path, 'r', encoding='utf-8')
t = f.read()
t = t.replace('Volatility 3 Framework 1.0.0-beta.1','')
t = t.replace('Valid pages (all)	Valid pages (large)	Swapped Pages (all)	Swapped Pages (large)	Invalid Pages (all)	Invalid Pages (large)	Other Invalid Pages (all)','')
t = t.replace('\n\n',"\t")
t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
my_list = t.split('\t')
result = [my_list[i * 7:(i + 1) * 7] for i in range((len(my_list) + 6) // 7 )] 

conn = sqlite3.connect("analyze.db")
cur = conn.cursor()
cur.execute("create table statistics (Valid_pages_All text, Valid_Pages_Large text, Swapped_Pages_All text, Swapped_Pages_Large text, Invalid_Pages_All text, Invalid_Pages_Large, Other_Invalid_Pages_ALL text)")

cur.executemany("insert into statistics values (?, ?, ?, ?, ?, ?, ?)", result)
conn.commit()

conn.close()