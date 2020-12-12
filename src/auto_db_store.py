import sqlite3
import os
import pathlib


print("                                                                                        ")
print(" #     #  ####  #        ##   ##### # #      # ##### #   #                              ")
print(" #     # #    # #       #  #    #   # #      #   #    # #                               ")
print(" #     # #    # #      #    #   #   # #      #   #     #                                ")
print("  #   #  #    # #      ######   #   # #      #   #     #                                ")
print("   # #   #    # #      #    #   #   # #      #   #     #                                ")
print("    #     ####  ###### #    #   #   # ###### #   #     #                                ")
print("                                                                                        ")
print("                                                                                        ")
print("   # #   #    # #####  ####       # #   #    #   ##   #      #   # ###### ###### #####  ")
print("  #   #  #    #   #   #    #     #   #  ##   #  #  #  #       # #      #  #      #    # ")
print(" #     # #    #   #   #    #    #     # # #  # #    # #        #      #   #####  #    # ")
print(" ####### #    #   #   #    #    ####### #  # # ###### #        #     #    #      #####  ")
print(" #     # #    #   #   #    #    #     # #   ## #    # #        #    #     #      #   #  ")
print(" #     #  ####    #    ####     #     # #    # #    # ######   #   ###### ###### #    # ")
                                                                                        


def cmdline():
    path = os.getcwd() + "/src/data/windows.cmdline.txt"
    path = pathlib.Path(path)
    f = open(path, 'r', encoding='utf-8')
    t = f.read()
    t = t.replace('Volatility 3 Framework 2.0.0-beta.1','')
    t = t.replace('PID	Process	Args','')
    t = t.replace('\n\n',"\t").replace('\n',"\t")
    t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
    my_list = t.split('\t')
    result = [my_list[i * 3:(i + 1) * 3] for i in range((len(my_list) + 2) // 3 )]
    conn = sqlite3.connect("analyze.db")
    cur = conn.cursor()
    cur.execute("create table cmdline (PID int, Process text, Args text)")
    cur.executemany("insert into cmdline values (?, ?, ?)", result)
    conn.commit()
    conn.close()

# def dlldump():
#     path = os.getcwd() + "/src/data/windows.dlldump.txt"
#     path = pathlib.Path(path)
#     f = open(path, 'r', encoding='utf-8')
#     t = f.read()
#     t = t.replace('Volatility 3 Framework 2.0.0-beta.1','')
#     t = t.replace('PID	Process	Result','')
#     t = t.replace('\n\n',"\t")
#     t = t.replace('\n',"\t")
#     t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
#     my_list = t.split('\t')
#     result = [my_list[i * 3:(i + 1) * 3] for i in range((len(my_list) + 2) // 3 )] 
#     print(result)
#     conn = sqlite3.connect("analyze.db")
#     cur = conn.cursor()
#     cur.execute("create table dlldump (PID int, Process text, Result text)")
#     cur.executemany("insert into dlldump values (?, ?, ?)", result)
#     conn.commit()
#     conn.close()

def dlllist():
    path = os.getcwd() + "/src/data/windows.dlllist.txt"
    path = pathlib.Path(path)
    f = open(path, 'r', encoding='utf-8')
    t = f.read()
    t = t.replace('Volatility 3 Framework 2.0.0-beta.1','')
    t = t.replace('PID	Process	Base	Size	Name	Path	LoadTime	Dumped','')
    t = t.replace('\n\n',"\t").replace('\n',"\t")
    t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
    my_list = t.split('\t')
    result = [my_list[i * 8:(i + 1) * 8] for i in range((len(my_list) + 7) // 8 )]
    conn = sqlite3.connect("analyze.db")
    cur = conn.cursor()
    cur.execute("create table dlllist (PID int, Process text, Base text, Size text, Name text, Path text, LoadTime text, Dumped text)")
    cur.executemany("insert into dlllist values (?, ?, ?, ?, ?, ?, ?, ?)", result)
    conn.commit()
    conn.close()

def filescan():
    path = os.getcwd() + "/src/data/windows.filescan.txt"
    path = pathlib.Path(path)
    f = open(path, 'r', encoding='utf-8')
    t = f.read()
    t = t.replace('Volatility 3 Framework 2.0.0-beta.1','')
    t = t.replace('Offset	Name','')
    t = t.replace('\n\n',"\t")
    t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
    my_list = t.split('\t')
    result = [my_list[i * 2:(i + 1) * 2] for i in range((len(my_list) + 1) // 2 )] 
    conn = sqlite3.connect("analyze.db")
    cur = conn.cursor()
    cur.execute("create table filescan (offset text, Name text)")
    cur.executemany("insert into filescan values (?, ?)", result)
    conn.commit()
    conn.close()

def handles():
    path = os.getcwd() + "/src/data/windows.handles.txt"
    path = pathlib.Path(path)
    f = open(path, 'r', encoding='utf-8')
    t = f.read()
    t = t.replace('Volatility 3 Framework 2.0.0-beta.1','')
    t = t.replace('PID	Process	Offset	HandleValue	Type	GrantedAccess	Name','')
    t = t.replace('\n\n',"\t").replace('\n', "\t")
    t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
    my_list = t.split('\t')
    result = [my_list[i * 7:(i + 1) * 7] for i in range((len(my_list) + 6) // 7 )] 
    conn = sqlite3.connect("analyze.db")
    cur = conn.cursor()
    cur.execute("create table handles (PID int, Process text, Offset text, HandleValue text, Type text, GrantedAccess text, Name text)")
    cur.executemany("insert into handles values (?, ?, ?, ?, ?, ?, ?)", result)
    conn.commit()
    conn.close()

def info():
    path = os.getcwd() + "/src/data/windows.info.txt"
    path = pathlib.Path(path)
    f = open(path, 'r', encoding='utf-8')
    t = f.read()
    t = t.replace('Volatility 3 Framework 2.0.0-beta.1','')
    t = t.replace('Variable','')
    t = t.replace('Value','')
    t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
    t = t.replace('\n',"\t")
    my_list = t.split('\t')
    result = [my_list[i * 2:(i + 1) * 2] for i in range((len(my_list) + 1) // 2 )] 
    conn = sqlite3.connect("analyze.db")
    cur = conn.cursor()
    cur.execute("create table info (Variable text, Value text)")
    cur.executemany("insert into info values (?, ?)", result)
    conn.commit()
    conn.close()

def malfind():
    print("MalFind Update Later")

# def moddump():
#     path = os.getcwd() + "/src/data/windows.moddump.txt"
#     path = pathlib.Path(path)
#     f = open(path, 'r', encoding='utf-8')
#     t = f.read()
#     t = t.replace('Volatility 3 Framework 2.0.0-beta.1','')
#     t = t.replace('Base	Name	Result','')
#     t = t.replace('\n\n',"\t")
#     t = t.replace('\n',"\t")
#     t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
#     my_list = t.split('\t')
#     result = [my_list[i * 3:(i + 1) * 3] for i in range((len(my_list) + 2) // 3 )] 
#     conn = sqlite3.connect("analyze.db")
#     cur = conn.cursor()
#     cur.execute("create table moddump (Base text, Name text, Result text)")
#     cur.executemany("insert into moddump values (?, ?, ?)", result)
#     conn.commit()
#     conn.close()

def modscan():
    path = os.getcwd() + "/src/data/windows.modscan.txt"
    path = pathlib.Path(path)
    f = open(path, 'r', encoding='utf-8')
    t = f.read()
    t = t.replace('Volatility 3 Framework 2.0.0-beta.1','')
    t = t.replace('Offset	Base	Size	Name	Path	Dumped','')
    t = t.replace('\n\n',"\t").replace('\n',"\t")
    t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
    my_list = t.split('\t')
    result = [my_list[i * 6:(i + 1) * 6] for i in range((len(my_list) + 5) // 6 )] 
    conn = sqlite3.connect("analyze.db")
    cur = conn.cursor()
    cur.execute("create table modscan (Offset text, Base text, Size text, Name text, Path text, Dumped text)")
    cur.executemany("insert into modscan values (?, ?, ?, ?, ?, ?)", result)
    conn.commit()
    conn.close()

def modules():
    path = os.getcwd() + "/src/data/windows.modules.txt"
    path = pathlib.Path(path)
    f = open(path, 'r', encoding='utf-8')
    t = f.read()
    t = t.replace('Volatility 3 Framework 2.0.0-beta.1','')
    t = t.replace('Offset	Base	Size	Name	Path	Dumped','')
    t = t.replace('\n\n',"\t").replace('\n',"\t")
    t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
    my_list = t.split('\t')
    result = [my_list[i * 6:(i + 1) * 6] for i in range((len(my_list) + 5) // 6 )] 
    conn = sqlite3.connect("analyze.db")
    cur = conn.cursor()
    cur.execute("create table modules (Offset text, Base text, Size text, Name text, Path text, Dumped text)")
    cur.executemany("insert into modules values (?, ?, ?, ?, ?, ?)", result)
    conn.commit()
    conn.close()

def mutantscan():
    path = os.getcwd() + "/src/data/windows.mutantscan.txt"
    path = pathlib.Path(path)
    f = open(path, 'r', encoding='utf-8')
    t = f.read()
    t = t.replace('Volatility 3 Framework 2.0.0-beta.1','')
    t = t.replace('Offset	Name','')
    t = t.replace('\n\n',"\t").replace('\n',"\t")
    t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
    my_list = t.split('\t')
    result = [my_list[i * 2:(i + 1) * 2] for i in range((len(my_list) + 1) // 2 )] 
    conn = sqlite3.connect("analyze.db")
    cur = conn.cursor()
    cur.execute("create table mutantscan (Offset text, Name text)")
    cur.executemany("insert into mutantscan values (?, ?)", result)
    conn.commit()
    conn.close()

def poolscanner():
    path = os.getcwd() + "/src/data/windows.poolscanner.txt"
    path = pathlib.Path(path)
    f = open(path, 'r', encoding='utf-8')
    t = f.read()
    t = t.replace('Volatility 3 Framework 2.0.0-beta.1','')
    t = t.replace('Tag	Offset	Layer	Name','')
    t = t.replace('\n\n',"\t").replace('\n',"\t")
    t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
    my_list = t.split('\t')
    result = [my_list[i * 4:(i + 1) * 4] for i in range((len(my_list) + 3) // 4 )] 
    conn = sqlite3.connect("analyze.db")
    cur = conn.cursor()
    cur.execute("create table poolscanner (Tag text, Offset text, Layer text, Name text)")
    cur.executemany("insert into poolscanner values (?, ?, ?, ?)", result)
    conn.commit()
    conn.close()

# def procdump():
#     path = os.getcwd() + "/src/data/windows.procdump.txt"
#     path = pathlib.Path(path)
#     f = open(path, 'r', encoding='utf-8')
#     t = f.read()
#     t = t.replace('Volatility 3 Framework 2.0.0-beta.1','')
#     t = t.replace('PID	Process	Result','')
#     t = t.replace('\n\n',"\t")
#     t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
#     my_list = t.split('\t')
#     result = [my_list[i * 3:(i + 1) * 3] for i in range((len(my_list) + 2) // 3 )] 
#     conn = sqlite3.connect("analyze.db")
#     cur = conn.cursor()
#     cur.execute("create table procdump (PID int, Process text, Result text)")
#     cur.executemany("insert into procdump values (?, ?, ?)", result)
#     conn.commit()
#     conn.close()

def pslist():
    path = os.getcwd() + "/src/data/windows.pslist.txt"
    path = pathlib.Path(path)
    f = open(path, 'r', encoding='utf-8')
    t = f.read()
    t = t.replace('Volatility 3 Framework 2.0.0-beta.1','')
    t = t.replace('PID	PPID	ImageFileName	Offset(V)	Threads	Handles	SessionId	Wow64	CreateTime	ExitTime	Dumped','')
    t = t.replace('\n\n',"\t").replace('\n',"\t")
    t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
    my_list = t.split('\t')
    result = [my_list[i * 11:(i + 1) * 11] for i in range((len(my_list) + 10) // 11 )] 
    conn = sqlite3.connect("analyze.db")
    cur = conn.cursor()
    cur.execute("create table pslist (PID int, PPID int, ImageFileName text, Offset text, Threads int, Handles int, Sessionid int, Wow64 text, createtime text, exittime text, Dumped text)")
    cur.executemany("insert into pslist values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", result)
    conn.commit()
    conn.close()

def psscan():
    path = os.getcwd() + "/src/data/windows.psscan.txt"
    path = pathlib.Path(path)
    f = open(path, 'r', encoding='utf-8')
    t = f.read()
    t = t.replace('Volatility 3 Framework 2.0.0-beta.1','')
    t = t.replace('PID	PPID	ImageFileName	Offset	Threads	Handles	SessionId	Wow64	CreateTime	ExitTime	Dumped','')
    t = t.replace('\n\n',"\t").replace('\n',"\t")
    t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
    my_list = t.split('\t')
    result = [my_list[i * 11:(i + 1) * 11] for i in range((len(my_list) + 10) // 11 )] 
    conn = sqlite3.connect("analyze.db")
    cur = conn.cursor()
    cur.execute("create table psscan (PID int, PPID int, ImageFileName text, Offset text, Threads int, Handles int, Sessionid int, Wow64 text, createtime text, exittime text, Dumped text)")
    cur.executemany("insert into psscan values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", result)
    conn.commit()
    conn.close()

def pstree():
    path = os.getcwd() + "/src/data/windows.pstree.txt"
    path = pathlib.Path(path)
    f = open(path, 'r', encoding='utf-8')
    t = f.read()
    t = t.replace('Volatility 3 Framework 2.0.0-beta.1','')
    t = t.replace('PID	PPID	ImageFileName	Offset(V)	Threads	Handles	SessionId	Wow64	CreateTime	ExitTime','')
    t = t.replace('\n\n',"\t").replace('\n',"\t")
    t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
    my_list = t.split('\t')
    result = [my_list[i * 10:(i + 1) * 10] for i in range((len(my_list) + 9) // 10 )] 
    conn = sqlite3.connect("analyze.db")
    cur = conn.cursor()
    cur.execute("create table pstree (PID int, PPID int, ImageFileName text, Offset text, Threads int, Handles int, Sessionid int, Wow64 text, CreateTime text, ExitTime text)")
    cur.executemany("insert into pstree values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", result)
    conn.commit()
    conn.close()

def registry_hivelist():
    path = os.getcwd() + "/src/data/windows.registry.hivelist.txt"
    path = pathlib.Path(path)
    f = open(path, 'r', encoding='utf-8')
    t = f.read()
    t = t.replace('Volatility 3 Framework 2.0.0-beta.1','')
    t = t.replace('Offset	FileFullPath	Dumped','')
    t = t.replace('\n\n',"\t")
    t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
    my_list = t.split('\t')
    result = [my_list[i * 3:(i + 1) * 3] for i in range((len(my_list) + 2) // 3 )] 
    conn = sqlite3.connect("analyze.db")
    cur = conn.cursor()
    cur.execute("create table registry_hivelist (Offset	text, FileFullPath text, Dumped text)")
    cur.executemany("insert into registry_hivelist values (?, ?, ?)", result)
    conn.commit()
    conn.close()

# def registry_hivescan():
#     path = os.getcwd() + "/src/data/windows.registry.hivescan.txt"
#     path = pathlib.Path(path)
#     f = open(path, 'r', encoding='utf-8')
#     t = f.read()
#     t = t.replace('Volatility 3 Framework 2.0.0-beta.1','')
#     t = t.replace('Offset','')
#     t = t.replace('\n\n',"\t")
#     t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
#     my_list = t.split('\t')
#     result = [my_list[i * 1:(i + 1) * 1] for i in range((len(my_list)) // 1 )] 
#     conn = sqlite3.connect("analyze.db")
#     cur = conn.cursor()
#     cur.execute("create table registry_hivescan (Offset	text)")
#     cur.executemany("insert into registry_hivescan values (?)", result)
#     conn.commit()
#     conn.close()

def registry_certificates():
    path = os.getcwd() + "/src/data/windows.registry.certificates.txt"
    path = pathlib.Path(path)
    f = open(path, 'r', encoding='utf-8')
    t = f.read()
    t = t.replace('Volatility 3 Framework 2.0.0-beta.1','')
    t = t.replace('Certificate path	Certificate section	Certificate ID	Certificate name','')
    t = t.replace('\n\n',"\t")
    t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
    my_list = t.split('\t')
    result = [my_list[i * 4:(i + 1) * 4] for i in range((len(my_list) + 3) // 4 )] 
    conn = sqlite3.connect("analyze.db")
    cur = conn.cursor()
    cur.execute("create table registry_certificates (Certificate_path text, Certificate_section text, Certificate_ID text,	Certificate_name text)")
    cur.executemany("insert into registry_certificates values (?, ?, ?, ?)", result)
    conn.commit()
    conn.close()

def registry_printkey():
    path = os.getcwd() + "/src/data/windows.registry.printkey.txt"
    path = pathlib.Path(path)
    f = open(path, 'r', encoding='utf-8')
    t = f.read()
    t = t.replace('Volatility 3 Framework 2.0.0-beta.1','')
    t = t.replace('Last Write Time	Hive Offset	Type	Key	Name	Data	Volatile','')
    t = t.replace('\n\n',"\t").replace('\n',"\t")
    t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
    my_list = t.split('\t')
    result = [my_list[i * 7:(i + 1) * 7] for i in range((len(my_list) + 6) // 7 )] 
    conn = sqlite3.connect("analyze.db")
    cur = conn.cursor()
    cur.execute("create table registry_printkey (Last_Write_Time text, Hive_Offset text, Type text, Key text, Name text, Data text, Volatile text)")
    cur.executemany("insert into registry_printkey values (?, ?, ?, ?, ?, ?, ?)", result)
    conn.commit()
    conn.close()

def registry_userassist():
    path = os.getcwd() + "/src/data/windows.registry.userassist.txt"
    path = pathlib.Path(path)
    f = open(path, 'r', encoding='utf-8')
    t = f.read()
    t = t.replace('Volatility 3 Framework 2.0.0-beta.1','')
    t = t.replace('Hive Offset	Hive Name	Path	Last Write Time	Type	Name	ID	Count	Focus Count	Time Focused	Last Updated	Raw Data','')
    t = t.replace('\n\n',"\t").replace('\n',"\t")
    t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
    my_list = t.split('\t')
    result = [my_list[i * 12:(i + 1) * 12] for i in range((len(my_list) + 11) // 12 )] 
    conn = sqlite3.connect("analyze.db")
    cur = conn.cursor()
    cur.execute("create table registry_userassist (Hive_Offset text,	Hive_Name_Path text,	Last_Write_Time text,	Type text, 	Name text,	ID text,	Count	text, Focus text, Count_Time text, Focused text,	Last_Updated text, Raw_Data text)")
    cur.executemany("insert into registry_userassist values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", result)
    conn.commit()
    conn.close()

def ssdt():
    path = os.getcwd() + "/src/data/windows.ssdt.txt"
    path = pathlib.Path(path)
    f = open(path, 'r', encoding='utf-8')
    t = f.read()
    t = t.replace('Volatility 3 Framework 2.0.0-beta.1','')
    t = t.replace('Index	Address	Module	Symbol','')
    t = t.replace('\n\n',"\t").replace('\n',"\t")
    t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
    my_list = t.split('\t')
    result = [my_list[i * 4:(i + 1) * 4] for i in range((len(my_list) + 3) // 4 )] 
    conn = sqlite3.connect("analyze.db")
    cur = conn.cursor()
    cur.execute("create table ssdt (num int, Address text, Module text, Symbol text)")
    cur.executemany("insert into ssdt values (?, ?, ?, ?)", result)
    conn.commit()
    conn.close()

def statistics():
    path = os.getcwd() + "/src/data/windows.statistics.txt"
    path = pathlib.Path(path)
    f = open(path, 'r', encoding='utf-8')
    t = f.read()
    t = t.replace('Volatility 3 Framework 2.0.0-beta.1','')
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

# def strings():
#     print("Update Later")

def svcscan():
    path = os.getcwd() + "/src/data/windows.svcscan.txt"
    path = pathlib.Path(path)
    f = open(path, 'r', encoding='utf-8')
    t = f.read()
    t = t.replace('Volatility 3 Framework 2.0.0-beta.1','')
    t = t.replace('Offset	Order	Pid	Start	State	Type	Name	Display	Binary','')
    t = t.replace('\n\n',"\t")
    t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
    my_list = t.split('\t')
    result = [my_list[i * 9:(i + 1) * 9] for i in range((len(my_list) + 8) // 9 )] 
    conn = sqlite3.connect("analyze.db")
    cur = conn.cursor()
    cur.execute("create table svcscan (Offset text, order_text text, PID text, Start text, State text, Type text, Name text, Display text, Binary text)")
    cur.executemany("insert into svcscan values (?, ?, ?, ?, ?, ?, ?, ?, ?)", result)
    conn.commit()
    conn.close()

def symlinkscan():
    path = os.getcwd() + "/src/data/windows.symlinkscan.txt"
    path = pathlib.Path(path)
    f = open(path, 'r', encoding='utf-8')
    t = f.read()
    t = t.replace('Volatility 3 Framework 2.0.0-beta.1','')
    t = t.replace('Offset	CreateTime	From Name	To Name','')
    t = t.replace('\n\n',"\t").replace('\n',"\t")
    t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
    my_list = t.split('\t')
    result = [my_list[i * 4:(i + 1) * 4] for i in range((len(my_list) + 3) // 4 )] 
    conn = sqlite3.connect("analyze.db")
    cur = conn.cursor()
    cur.execute("create table symlinkscan (Offset text,	CreateTime text,	From_Name text,	To_Name text)")
    cur.executemany("insert into symlinkscan values (?, ?, ?, ?)", result)
    conn.commit()
    conn.close()

# def vaddump():
#     path = os.getcwd() + "/src/data/windows.vaddump.txt"
#     path = pathlib.Path(path)
#     f = open(path, 'r', encoding='utf-8')
#     t = f.read()
#     t = t.replace('Volatility 3 Framework 2.0.0-beta.1','')
#     t = t.replace('PID	Process	Result','')
#     t = t.replace('\n\n',"\t")
#     t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
#     my_list = t.split('\t')
#     result = [my_list[i * 3:(i + 1) * 3] for i in range((len(my_list) + 2) // 3 )] 
#     conn = sqlite3.connect("analyze.db")
#     cur = conn.cursor()
#     cur.execute("create table vaddump (PID int, Process text, Result text)")
#     cur.executemany("insert into vaddump values (?, ?, ?)", result)
#     conn.commit()
#     conn.close()

# def vadinfo():
#     print("Update Later")

def verinfo():
    path = os.getcwd() + "/src/data/windows.verinfo.txt"
    path = pathlib.Path(path)
    f = open(path, 'r', encoding='utf-8')
    t = f.read()
    t = t.replace('Volatility 3 Framework 2.0.0-beta.1','')
    t = t.replace('PID	Process	Base	Name	Major	Minor	Product	Build','')
    t = t.replace('\n\n',"\t").replace('\n', "\t")
    t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
    my_list = t.split('\t')
    result = [my_list[i * 8:(i + 1) * 8] for i in range((len(my_list) + 7) // 8 )]
    conn = sqlite3.connect("analyze.db")
    cur = conn.cursor()
    cur.execute("create table verinfo (PID text, Process text, Base text, Name text, Major int, Minor int, Product int, Build int)")
    cur.executemany("insert into verinfo values (?, ?, ?, ?, ?, ?, ?, ?)", result)
    conn.commit()
    conn.close()

def virtmap():
    print("Update Later")

plugin_list = [cmdline(), dlllist(), modscan(), modules(), mutantscan(),
                poolscanner(), filescan(), handles(), info(),
                pslist(), psscan(), pstree(),
                registry_certificates(), registry_hivelist(),
                registry_printkey(), registry_userassist(),
                ssdt(), statistics(), symlinkscan(), verinfo()]
for plugin in plugin_list :
    plugin
# cmdline()
# dlllist()
# vadinfo() -> 구현 못함
# malfind() -> DB Store Error
# moddump()
# dlldump()
# driverirp()
# driverscan()
# procdump()
# registry_hivescan() -> DB Store Error
# strings()
# vaddump()
#virtmap()
print("Memory Result Store in DB Successful")