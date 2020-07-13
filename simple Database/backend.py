import sqlite3

def connect():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS routine (Id INTEGER PRIMARY KEY , date text , hours_spend integer , sleep text , language text , eat text ,favorite_coding_language text)")
    conn.commit()
    conn.close()

def insert(date , hours_spend , sleep , language , eat , favorite_coding_language):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO routine VALUES (NULL , ?,?,?,?,?,?)" , (date , hours_spend , sleep, language , eat , favorite_coding_language))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM routine WHERE id=? ", (id,))
    conn.commit()
    conn.close()

def search(date='' , hours_spend='' , sleep='' , language='' , eat='' , favorite_coding_language=''):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine WHERE date=?  OR hours_spend=? OR sleep=? OR language=? OR eat=? OR favorite_coding_language=?" , (date , hours_spend , sleep , language , eat , favorite_coding_language))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

connect()
