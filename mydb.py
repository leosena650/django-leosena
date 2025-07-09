
import pymysql

pymysql.install_as_MySQLdb()

dataBase = pymysql.connect(
    host="localhost",
    user="root",
    passwd="admin",
    charset= 'utf8mb4',
    )
cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE IF NOT EXISTS elderco")
print("Database created successfully")
dataBase.close()
