import time
import database

mycursor = database.getCursor()
query = "Select * FROM Users"
mycursor.execute(query)
res = mycursor.fetchall()
print(res)