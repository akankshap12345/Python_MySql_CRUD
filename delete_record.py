import connect_db_25
cursor = connect_db_25.myconn.cursor()

del_sql = ("DELETE from tbl_dept where dept_id = %s")
del_data = (108,)
cursor.execute(del_sql, del_data)
connect_db_25.myconn.commit()