empno = int(input("Enter employee no : "));
name = input("Enter employee name : ");
gender = input("Enter Gender : ");
basic_salary = int(input("Enter basic salary : "));

if gender == "male" or gender == "Male":
    DA=basic_salary*0.8;
    HRA=basic_salary*0.1;
    Bonus=basic_salary*0.5;
else:
    DA=basic_salary*0.7;
    HRA=basic_salary*0.15;
    Bonus=basic_salary*0.52;


net_salary=basic_salary+DA+HRA+Bonus;
print("Net salary : ",net_salary);
gross=net_salary*12;
print("Gross salary : ",gross);


