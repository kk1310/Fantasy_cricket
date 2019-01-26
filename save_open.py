import sqlite3

s = sqlite3.connect ( "db.db" )
b = s.cursor ()


def saving_team(name, points, value):
    try:
        sql = "insert into Teams(name,players,value) VALUES ('"+name+"', '"+points+"','"+str(value)+"');"
        b.execute(sql)
        record=b.fetchall()
        #print(record)
        s.commit()

    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format ( type ( ex ).__name__, ex.args )
        print ( "sel {}".format ( message ) )


def opening_team(teamName):
    sql="select players from Teams where name='"+teamName+"'; "
    b.execute(sql)
    record=b.fetchall()
    return record

def items_combobox():
    sql="select name from Teams"
    b.execute(sql)
    record=b.fetchall()
    remove_duplicates=set(record)
    result =list(remove_duplicates)
    #print(*result)
    return result


