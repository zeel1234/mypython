import mysql.connector;
from mysql.connector import Error;

try:
    con=mysql.connector.connect(host="localhost",database="Student",user="root",passwd="mcalab");
    print("Established connection :  ",con)

    queryTable = "create table Student1(";
    queryTable = queryTable+" rollno int ,";
    queryTable = queryTable+" name varchar(20),";
    queryTable = queryTable+" Birthdate date,";
    queryTable = queryTable+" gender char(1),";
    querytable = queryTable+" semester int,";
    queryTable = queryTable+" python_marks decimal(5,2),";
    queryTable = queryTable+" java_marks decimal(5,2),";
    queryTable = queryTable+" php_marks decimal(5,2),";
    queryTable = queryTable+" total_marks decimal(5,2),";
    queryTable = queryTable+" Percentage decimal(5,2),";
    queryTable = queryTable+" grade varchar(5));";

    print(queryTable);
    cursor = con.cursor();
    cursor.execute(queryTable);
    print("Table created succesfully !");
    
except Error as e:
    print("Error  = ",e)
finally:
    if(con.is_connected()):
        cursor.close();
        con.close();
