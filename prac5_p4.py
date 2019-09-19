import datetime;
class Person:

    def __init__(self,name,age,bdate,gender):
        self.name=name;
        self.age=age;
        self.bdate=bdate;
        self.gender=gender;

    def set(self,name,age,bdate,gender):
        self.name=name;
        self.age=age;
        self.bdate=bdate;
        self.gender=gender;

    def get(self):
        self.name=input("Enter name : ");
        self.age=int(input("Enter age : "));
        d=input("Enter birth date : ");
        self.bdate= datetime.datetime.strptime(d, "%d/%m/%Y")
        self.gender=input("Enter gender : ");
        
    def show(self):
        print("Name : ",self.name);
        print("Age : ",self.age);        
        print("Birthdate : ",self.bdate);
        print("Gender : ",self.gender);

#
class Student(Person):
    def __init__(self,name,age,bdate,gender,sem,pyt,java,php):
        super().__init__(name,age,bdate,gender);
        self.sem=sem;
        self.pyt =pyt;
        self.java=java;
        self.php =php;

    def set(self,sem,pyt,java,php):
        super().set();
        self.sem=sem;
        self.pyt =pyt;
        self.java=java;
        self.php =php;
        
    def get(self):
        super().get();
        self.sem=int(input("Enter semester  : "));
        self.pyt=int(input("Enter python marks  : "));
        self.java=int(input("Enter java marks  : "));
        self.php=int(input("Enter php marks  : "));

    def show(self):
        super().show();
        print("Semester : ",self.sem);
        print("Python marks : ",self.pyt);        
        print("Java marks : ",self.java);
        print("PHP marks : ",self.php);
        print("total : ",self.total);
        

    def calc_total(self):
        self.total = self.pyt+ self.java+self.php;
        

    def calc_grade(self):
        self.per = self.total/3;
        print("Percentage :",self.per);

        if(self.per<=100 and self.per>90):
            print("Distinction");
        elif(self.per<=90 and self.per>80):
            print("First Class");
        elif(self.per<=80 and self.per>70):
            print("Second Class");
        elif(self.per<=70 and self.per>60):
            print("Second Class");
        else:
            print("Fail");

            

s1 = Student("zeel",21,"08/12/1997","female",3,56,80,70);
s1.calc_total();
s1.show();
s1.calc_grade();

