import mysql.connector

databse = mysql.connector.connect(
	 host = 'localhost',
	 user = 'root',
	 passwd = 'lmb097789543',

	 )

cursorObject = databse.cursor()

cursorObject.execute("CREATE DATABASE borat")

print("All Done!")
