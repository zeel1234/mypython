import mysql.connector;
from mysql.connector import Error ;

print("Establishing Connection");
try:
    db_connection = mysql.connector.connect(host="localhost",
                                  user="root",
                                  passwd="mcalab",
                                  database="my_student");
    print("Connection Established",db_connection);
    
    
    queryCreateTable="create table student(";
    queryCreateTable = queryCreateTable + "rollno int not null ,name varchar(20),";
    queryCreateTable = queryCreateTable + "bdate date,";
    queryCreateTable = queryCreateTable + "gender char(1),";
    queryCreateTable = queryCreateTable + "semester char(1),";
    queryCreateTable = queryCreateTable + "python_marks decimal,";
    queryCreateTable = queryCreateTable + "java_marks decimal,";
    queryCreateTable = queryCreateTable + "php_marks decimal,";
    queryCreateTable = queryCreateTable + "total_marks decimal,";
    queryCreateTable = queryCreateTable + "percentage decimal,";
    queryCreateTable = queryCreateTable + "grade char(1))";
    print(queryCreateTable);
    cursor = db_connection.cursor();
    result=cursor.execute(queryCreateTable);
    print("Table Created");

    rn=input("Enter roll no :");
    nm=input("Enter Name : ");
    bdate=input("Enter Birthdate : ");
    gen=input("Enter Gender : ");
    sem=input("Enter Semester : ");
    py_marks=input("Enter python_marks : ");
    j_marks=input("Enter java_marks : ");
    php_marks=input("Enter php marks : ");

    qInsert ="insert into student(rollno,name,bdate,gender,semester,python_marks,java_marks,php_marks) values( ";
    qInsert = qInsert + rn + ",";
    qInsert = qInsert + "'" + nm + "',";
    qInsert = qInsert + "'" + bdate + "',";
    qInsert = qInsert + "'" + gen + "',";
    qInsert = qInsert + "'" + sem + "',";
    qInsert = qInsert + py_marks + ",";
    qInsert = qInsert + j_marks + ",";
    qInsert = qInsert + php_marks + ");";
    print("Rows Inserted ");
    cursor = db_connection.cursor();
    result=cursor.execute(qInsert);
    print("Table Created");
           
    
           

    
   

except Error as e :
    print("Error",e);
  
