import sqlite3
s=sqlite3.connect("db.db")
b=s.cursor()

def player_value(name):
    sql="select Value from Stats where Player='"+name+"';"
    b.execute(sql)
    record=b.fetchone()
    j=str(*record)
    return j


def check_role(name):
    sql="select Ctg from Stats where Player='"+name+"';"
    b.execute(sql)
    record=b.fetchone()
    j=str(*record)
    return j

