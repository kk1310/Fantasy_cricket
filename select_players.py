import sqlite3

s = sqlite3.connect ( "db.db" )
b = s.cursor ()

def fetch_batsmen():
    nm = "BAT"
    sql = "select Player from Stats where Ctg='" + nm + "';"
    b.execute ( sql )
    record = b.fetchall ()
    return record

def fetch_bowler():
    nm = "BWL"
    sql = "select Player from Stats where Ctg='" + nm + "';"
    b.execute ( sql )
    record = b.fetchall ()
    return record

def fetch_allRounders():
    nm = "AR"
    sql = "select Player from Stats where Ctg='" + nm + "';"
    b.execute ( sql )
    record = b.fetchall ()
    return record

def fetch_wicketKeeper():
    nm = "WK"
    sql = "select Player from Stats where Ctg='" + nm + "';"
    b.execute ( sql )
    record = b.fetchall ()
    return record

def fetch_points(nm1):
    sql1 = "select Value From Stats where Player='" + nm1 + "';"
    b.execute ( sql1 )
    record1 = b.fetchall()
    h = list ( record1 )
    z = sum ( *h )
    return z

