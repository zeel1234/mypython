import mysql.connector;
from mysql.connector import Error;

try:
    con = mysql.connector.connect(host="localhost",database="Student",user="root",passwd="mcalab");
    
    print("connected = ",con)
except Error as e:
    print("Error ",e)
