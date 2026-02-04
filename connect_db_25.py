import mysql.connector
try:
    myconn  = (mysql.connector.connect
           (user='root', password='',
            host='127.0.0.1',
            database='company_db')
           )
    print("Successfully connected to MySQL database")
    print(myconn)
except mysql.connector.Error as e:
    print ("Error code:", e.errno ) # error number
    print ("SQLSTATE value:", e.sqlstate)  # SQLSTATE value
    print ("Error message:", e.msg)  # error message
    print ("Error:", e ) # errno, sqlstate, msg values
    s = str(e)
    print ("Error:", s ) # errno, sqlstate, msg values


#
#creating the cursor object
#cursor = myconn.cursor()
#

# sql = "CREATE TABLE IF NOT EXISTS friends (fid INT(4) AUTO_INCREMENT PRIMARY KEY, fname VARCHAR(100) NOT NULL ) ENGINE=INNODB;"
#
#
# cursor.execute(sql)
