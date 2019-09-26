import mysql.connector
db_connection = mysql.connector.connect(
  host="localhost",
  user="your_username_here",
  passwd="your_password_here",
  database="my_test_db"
)
my_database = db_connection.cursor()

my_database.execute("CREATE DATABASE MY_TEST_DB")

my_database = db_connection.cursor()

my_database.execute("CREATE TABLE CodeSpeedy (category VARCHAR(255), name VARCHAR(255))")

my_database = db_connection.cursor()
sql_statement = "INSERT INTO codespeedy (category,duration,level) values(%s,%s,%s)"
values = ("Python","100 Hours","Advanced")
my_database.execute(sql_statement,values)
db_connection.commit()
sql_statement = "SELECT * FROM CODESPEEDY"

my_database.execute(sql_statement)
output = my_database.fetchall()
for x in output:
  print(x)


my_database = db_connection.cursor()
sql_statement = "UPDATE CODESPEEDY SET duration= %s where category= %s"
data = ("150 Hours", "Python")

my_database.execute(sql_statement,data)
db_connection.commit()

sql_query = "DELETE FROM codespeedy where category='Python'"

my_database.execute(sql_query)
db_connection.commit()
print("Row(s) deleted successfully!!!!")
