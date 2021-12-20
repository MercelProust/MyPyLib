# !/usr/bin/env python
# encoding:utf-8
import CommonLib.dbwrapper as db

userdb = db.DBWrapper()
success = userdb.connect()
if not success:
    print("db 连接失败")
else :
    conn = userdb.get_cursor()
    for i in range(1000000000):
        sql = "INSERT INTO `otadb`.`t_area_code`" \
              "(`area_code`,`nation`)" \
              "VALUES('" + str(i) +"','nation_" + str(i) + ")"
        conn.execute(sql)
        print(str(i))
    conn.close()

