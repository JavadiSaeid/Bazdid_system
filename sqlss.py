from jdatetime import datetime as dt
import sqlite3

with sqlite3.connect("Data\ZamanBandi_Bazdid.db") as database:
    query = "select id, tb, tbo from BAZDID_DATE"
    c = database.cursor()
    QuerySet = c.execute(query)
    for i in QuerySet:
        id = i[0]
        tb = i[1]
        if tb != None:
            y = tb.split('/')
            if len(y[0]) < 4:
                tb = "13"+tb
            tbo = str(dt.strptime(tb, '%Y/%m/%d'))
            # t = str(dt.strptime('1398/3/25', '%Y/%m/%d'))
            # if t <= i[2]:
            #     print(i[2])
            update_tb = "UPDATE BAZDID_DATE SET tbo='{}' WHERE id = '{}'".format(tbo, id)
            database.execute(update_tb)
            database.commit()
