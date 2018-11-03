import mysql.connector

#create database connection object
mydb = mysql.connector.connect(
    host = 'se-project.cqeckwiwnfhm.us-east-2.rds.amazonaws.com',
    user = 'root',
    passwd = '12345678',
    database = 'se',
    autocommit = "True"
)

#return cursor for dB
def getCursor():
    return mydb.cursor()

#method to commit changes to dB
def commit():
    mydb.commit()