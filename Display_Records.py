import connect_db_25
cursor = connect_db_25.myconn.cursor()

if connect_db_25.myconn and connect_db_25.myconn.is_connected():
    with connect_db_25.myconn.cursor() as cursor:
        result = cursor.execute("SELECT * FROM tbl_dept LIMIT 5")
        rows = cursor.fetchall()
        for rows in rows:
            print(rows)

    connect_db_25.myconn.close()

else:

    print("Could not connect")