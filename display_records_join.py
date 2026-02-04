import connect_db_25
cursor = connect_db_25.myconn.cursor()
def getDept():
    sql = "select dept_id , dept_name from tbl_dept "
    result = cursor.execute(sql)
    rows = cursor.fetchall()
    dept_dict ={}
    for rows in rows:
        dept_dict[rows[0]] = rows[1]
    return dept_dict

print(getDept())
#
# if connect_db_25.myconn and connect_db_25.myconn.is_connected():
#     with connect_db_25.myconn.cursor() as cursor:
#         sql = "SELECT e.*, d.dept_name from tbl_emp e inner join tbl_dept d on e.dept_id = d.dept_id order by e.emp_id "
#         result = cursor.execute(sql)
#         rows = cursor.fetchall()
#         for rows in rows:
#             print(rows)
#
#     connect_db_25.myconn.close()
# else:
#     print("Could not connect")