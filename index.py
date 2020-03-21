from flask import Flask
from flask import render_template
app = Flask(__name__)

import sqlite3
conn = sqlite3.connect("analyze.db")
cur = conn.cursor()

cur.execute('select * from pslist')
pslist = cur.fetchall()

cur.execute('select * from pstree')
pstree = cur.fetchall()

cur.execute('select * from psscan')
psscan = cur.fetchall()

cur.execute('select * from dlllist')
dlllist = cur.fetchall()

cur.execute('select * from dlldump')
dlldump = cur.fetchall()

cur.execute('select * from handles')
handles = cur.fetchall()

cur.execute('select * from registry_certificates')
certificates = cur.fetchall()

cur.execute('select * from registry_printkey')
printkey = cur.fetchall()

cur.execute('select * from registry_userassist')
userassist = cur.fetchall()

conn.close()


@app.route('/')
def index():
    return render_template(
                    'index.html',
                    pslist = pslist
                )

@app.route('/pslist')
def process_list():
    return render_template(
                    '/plugin/pslist.html',
                    pslist = pslist
                )

@app.route('/psscan')
def process_scan():
    return render_template(
                    '/plugin/psscan.html',
                    psscan = psscan
                )

@app.route('/pstree')
def process_tree():
    return render_template(
                    '/plugin/pstree.html',
                    pstree = pstree
                )

@app.route('/dlllist')
def dll_list():
    return render_template(
                    '/plugin/dlllist.html',
                    dlllist = dlllist
                )

@app.route('/dlldump')
def dll_dump():
    return render_template(
                    '/plugin/dlldump.html',
                    dlldump = dlldump
                )

@app.route('/handles')
def handles_info():
    return render_template(
                    '/plugin/handles.html',
                    handles = handles
                )

@app.route('/registry_certificates')
def certificates_info():
    return render_template(
                    '/plugin/registry_certificates.html',
                    certificates = certificates
                )


@app.route('/registry_printkey')
def printkey_info():
    return render_template(
                    '/plugin/registry_printkey.html',
                    printkey = printkey
                )

@app.route('/registry_userassist')
def userassist_info():
    return render_template(
                    '/plugin/registry_userassist.html',
                    userassist = userassist
                )

if __name__ == '__main__':
 app.run(host='0.0.0.0')