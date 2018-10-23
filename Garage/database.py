import mysql.connector

mydb = mysql.connector.connect(
    host = 'se-project.cqeckwiwnfhm.us-east-2.rds.amazonaws.com',
    user = 'root',
    passwd = '12345678',
    database = 'se'
)

def getCursor():
    return mydb.cursor()

def commit():
    mydb.commit()