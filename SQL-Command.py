from jdatetime import datetime as dt
import sqlite3

db_path = r'\\10.120.112.70\baygan-data\ZamanBandi_Bazdid.db'
with sqlite3.connect(db_path) as database:
    # query_tb = "select id, tb, tbo from BAZDID_DATE"
    # query_qtt = "select id, dw from BAZDID_DATE WHERE dw='ق ت ت' OR dw= 'ق ت ت ' OR dw='تعیین تکلیف' OR dw='قت ت ' OR dw='قت ت' OR dw='ق ق  ت' OR dw='ق تت'"
    # query_ts = "select id, dw from BAZDID_DATE WHERE dw='تعویض' OR dw='تعویض ' OR dw='تعویص'"
    query_ap = "select id, dw from BAZDID_DATE WHERE dw=' آپارتمان' OR dw='آپارتمان' OR dw='  آپارتمان '"
    c = database.cursor()
    QuerySet = c.execute(query_ap)

    # for i in QuerySet:        ## tb and tbo
    #     id = i[0]
    #     tb = i[1]
    #     if tb != None:
    #         y = tb.split('/')
    #         if len(y[0]) < 4:
    #             tb = "13"+tb
    #         tbo = str(dt.strptime(tb, '%Y/%m/%d'))
    #         # t = str(dt.strptime('1398/3/25', '%Y/%m/%d'))
    #         # if t <= i[2]:
    #         #     print(i[2])
    #         update_tb = "UPDATE BAZDID_DATE SET tbo='{}' WHERE id = '{}'".format(tbo, id)
    #         database.execute(update_tb)
    #         database.commit()

    for i in QuerySet:          ## dw
        id = i[0]
        dw = i[1]
        if dw != None or dw != '':
            # update_tb = "UPDATE BAZDID_DATE SET dw='قانون تعیین تکلیف' WHERE id = '{}'".format(id)
            # update_tb = "UPDATE BAZDID_DATE SET dw='تعویض سند' WHERE id = '{}'".format(id)
            update_tb = "UPDATE BAZDID_DATE SET dw='تفکیک آپارتمان' WHERE id = '{}'".format(id)
            database.execute(update_tb)
            database.commit()