import connect_db_25

#creating the cursor object
cursor = connect_db_25.myconn.cursor()

sql = "CREATE TABLE IF NOT EXISTS riends (fid INT(4) AUTO_INCREMENT PRIMARY KEY, fname VARCHAR(100) NOT NULL ) ENGINE=INNODB;"
cursor.execute(sql)