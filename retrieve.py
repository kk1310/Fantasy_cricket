import points_
import sqlite3
def fetch_points_2(name):
    s = sqlite3.connect ( "db.db" )
    b = s.cursor ()
    sql = "select * from Match where Player='" +name+ "';"
    b.execute ( sql )
    record = b.fetchone ()
    #print("the record value is {}".format(record))
    b.execute ( "select * from Stats where Player='" +name+ R"';" )
    record_2 = b.fetchone ()
    #print("the value of record2 is {}".format(record_2))
    b=rr(record,record_2)
    #print("this is the calling function {}".format(b))
    return b




def rr(record,record_2):

    runs = record[1]                                 #46
    balls = record[2]                                #65
    fours = record[3]                                #5
    sixes = record[4]                                 #1
    field = record[9] + record[10] + record[11]         #1
    wickets = record[8]
    overs = int ( record[5] / 6 )
    given = record[7]

    if record_2[6] == "AR":
        a=points_.bat (runs,balls,fours,sixes,field )
        b=points_.bowl ( wickets,overs,given,field )
        c=(a+b)
        #print("this c {}".format(c))
        return c

    elif record_2[6] == "BAT" or record_2[6] == "WK":
        a=points_.bat ( runs,balls,fours,sixes,field )
        #print("this is a {}".format(a))
        return a

    else:
        a=points_.bowl ( wickets,overs,given,field )
        #print("this is a1 {}".format(a))
        return a






