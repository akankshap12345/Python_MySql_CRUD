import connect_db_25
cursor = connect_db_25.myconn.cursor()

upd_sql = ("UPDATE tbl_dept set dept_name = %s , dept_location = %s where dept_id = %s ")
upd_data = ('Housekeeping' ,'Pune, Kondhava', 108)
cursor.execute(upd_sql, upd_data)
#myconn.commit()
connect_db_25.myconn.commit()