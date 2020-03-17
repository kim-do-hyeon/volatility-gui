print("Update Later")
# import sqlite3

# f = open('windows.malfind.txt', 'r', encoding='utf-8')
# t = f.read()
# t = t.replace('Volatility 3 Framework 1.0.0-beta.1','')
# t = t.replace('PID	Process	Start VPN	End VPN	Tag	Protection	CommitCharge	PrivateMemory	Hexdump	Disasm','')
# t = t.replace('\n\n',"\t")
# t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
# my_list = t.split('\t')
# print(my_list)
# result = [my_list[i * 9:(i + 1) * 9] for i in range((len(my_list) + 8) // 9 )] 
# print(result) 

# conn = sqlite3.connect("analyze.db")
# cur = conn.cursor()
# cur.execute("create table malfind (PID int, Process text, Start_VPN text, End_VPN text,	Tag text, Protection text, CommitCharge text, PrivateMemory text, Hexdump_Disasm text)")

# cur.executemany("insert into malfind values (?, ?, ?, ?, ?, ?, ?, ?, ?)", result)
# conn.commit()

# cur.execute('select * from malfind')
# for row in cur:
#     print(row)

# conn.close()