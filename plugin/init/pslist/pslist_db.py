import sqlite3

f = open('../windows.pslist.txt', 'r', encoding='utf-8')
t = f.read()
t = t.replace('Volatility 3 Framework 1.0.0-beta.1','')
t = t.replace('PID	PPID	ImageFileName	Offset(V)	Threads	Handles	SessionId	Wow64	CreateTime	ExitTime','')
t = t.replace('\n\n',"\t")
t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
my_list = t.split('\t')
result = [my_list[i * 10:(i + 1) * 10] for i in range((len(my_list) + 9) // 10 )] 
print(result) 

conn = sqlite3.connect("../analyze.db")
cur = conn.cursor()
cur.execute("create table pslist (PID int, PPID int, ImageFileName text, Offset text, Threads int, Handles int, Sessionid int, Wow64 text, createtime text, exittime text)")

cur.executemany("insert into pslist values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", result)
conn.commit()

cur.execute('select * from pslist')
for row in cur:
    print(row)

conn.close()