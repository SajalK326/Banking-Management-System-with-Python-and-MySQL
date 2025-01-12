import mysql.connector

# Establish a connection to the MySQL server
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Sajal@0306"
)

print("Successfully Connected")

# Create a cursor object
mycur = mydb.cursor()

# Create a new database
mycur.execute("CREATE DATABASE bank")
mycur.execute("USE bank")
mycur.execute("CREATE TABLE customer (Account_No bigint, Name VARCHAR(100), Mobile_No bigint, Account_Type VARCHAR(20), Amount bigint)")

# Close the connection
mydb.close()
