import connect_db_25
cursor = connect_db_25.myconn.cursor()

def addDept(dname, location, status):
    insert_stmt = (
        "INSERT INTO tbl_dept (dept_name, dept_location, status) VALUES (%s, %s, %s)"
    )
    data = (dname,location, status )
    cursor.execute(insert_stmt, data)
    connect_db_25.myconn.commit()

    #select_stmt = "SELECT * FROM employees WHERE emp_no = %(emp_no)s"
    #cursor.execute(select_stmt, {'emp_no': 2})
#addDept('Production', 'Pune', '1')
#addDept('Research and Development ', 'Chennai', '1')
#addDept('House ', 'Pune, Katraj', '1')
addDept('UI-UX', 'Mumbai, Dadar', '1')


def addEmp(dept_id, emp_name, sal, jdate):
    insert_stmt = (
        "INSERT INTO tbl_emp (dept_id, empname, salary, join_date) VALUES (%s, %s, %s, %s)"
    )
    data = (dept_id,emp_name, sal, jdate )
    cursor.execute(insert_stmt, data)
    connect_db_25.myconn.commit()

#addEmp(101, 'Nikit S.', 45000, '2012-10-02')
#addEmp(101, 'Priya D.', 47000, '2012-12-01')
#addEmp(107, 'Abhijeet H.', 120000, '2000-05-01')
#addEmp(102, 'Sakshi P.', 150000, '2000-10-16')