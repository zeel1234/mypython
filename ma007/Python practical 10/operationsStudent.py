import mysql.connector;
from mysql.connector import Error;
 

try:
    con=mysql.connector.connect(host="localhost",database="Student",user="root",passwd="mcalab");
    print("Established connection :  ",con)
    while(True):
        print("1.Insert records\n2.calculate total\n3.calculate percentage\n4.calculate Grade\n")
        choice = int(input("enter your choice : "))
        if choice == 1:
            roll = input("enter rollno of student : ")
            nm = input("enter name of student : ")
            bdat = input("enter birthdate of student : ")
            gen = input("enter gender of student : ")
            py = input("enter python marks of student : ")
            java = input("enter java marks of student : ")
            php =input("enter php marks of student : ")
            queryInsert = "insert into student(rollno,name,Birthdate,gender,python_marks,java_marks,php_marks) values(";
            queryInsert = queryInsert + "'"+roll+"',";
            queryInsert = queryInsert + "'"+nm+"',";
            queryInsert = queryInsert + "'"+bdat+"',";
            queryInsert = queryInsert + "'"+gen+"',";
            queryInsert = queryInsert + "'"+py+"',";
            queryInsert = queryInsert + "'"+java+"',";
            queryInsert = queryInsert + "'"+php+"');";
            print(queryInsert)
            cursor = con.cursor();
            cursor.execute(queryInsert);
            con.commit();
            print("Record inserted !")
        elif choice == 2:
            queryTotal = "update student set total_marks = python_marks+java_marks+php_marks";
            cursor = con.cursor();
            cursor.execute(queryTotal);
            con.commit();
            print("updated total !")
        elif choice == 3:
            queryPercent = "update student set Percentage = total_marks/3;";
            cursor = con.cursor();
            cursor.execute(queryPercent);
            con.commit();
            print("updated Percentage !")
        elif choice == 4:
            queryrecrods = "select * from student;";
            cursor = con.cursor()
            result = cursor.excute(queryrecrods)
            resultset = cursor.fetchall();
            for row in resultset:
                

        choice = input("enter choice [y/n]:")
        if choice == 'n':
            break;
        
    
except Error as e:
    print("Error in connection = ",e);
