import datetime;
class Person:

    def __init__(self,name,age,bdae,gender):
        self.name=name;
        self.age=age;
        self.bdae=bdae;
        self.gender=gender;

    def set(self,name,age,bdae,gender):
        self.name=name;
        self.age=age;
        self.bdae=bdae;
        self.gender=gender;

    def get(self):
        self.name=input("Enter name : ");
        self.age=int(input("Enter age : "));
        d=input("Enter birth date : ");
        self.bdae= datetime.datetime.strptime(d, "%d/%m/%Y")
        self.gender=input("Enter gender : ");
        
    def show(self):
        print("Name : ",self.name);
        print("Age : ",self.age);        
        print("Birthdate : ",self.bdae);
        print("Gender : ",self.gender);

class Employee(Person):
    def__init__(self,name,age,bdae,gender,salary):
        super.__init(self,name,age,bdae,gender);
        self.salary=salary;
        
p1=Employee("zeel",21,"08/12/1997","female");
p1.show();
