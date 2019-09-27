class Person:
    def __init__(self,nm = "",gen = "",bdat = 1996):
        self.name = nm;
        self.bdate = bdat;
        self.gender = gen;
    def set(self,nm = "",gen = "",bdat = 1996):
        self.name = nm;
        self.bdate = bdat;
        self.gender = gen;
    def get(self):
        return (self.name,self.gen,self.bdate)
    def show(self):
        print("Name : ",self.name)
        print("Birth date : ",self.bdate)
        print("Gender : ",self.gender)

#

class Student(Person):
    def __init__(self,nm = "",gen="",bdat = 1996,sem = 0,py_mark = 0,j_mark = 0,php_mark = 0):
        self.semester = sem;
        self.py_marks = py_mark;
        self.j_marks = j_mark;
        self.php_marks = php_mark;
        super().__init__(nm,gen,bdat)
    def set(self,nm = "",gen = "",bdat = 1996,sem = 0,py_mark = 0,j_mark = 0,php_mark = 0):
        self.semester = sem;
        self.py_marks = py_mark;
        self.j_marks = j_mark;
        self.php_marks = php_mark;
        super().set(nm,gen,bdat)
    def get(self):
        super().get()
        return (sem,py_mark,j_mark,php_mark)
    def calc_total(self):
        Total = self.py_marks + self.j_marks + self.php_marks;
        return Total;
    def calc_per(self):
        Percentage = self.calc_total()//3
        return Percentage
    def calc_grade(self):
        percent = self.calc_per()
        if percent >= 90 :
            Grade = "A";
        elif percent >= 70 and percent <90:
            Grade = "B";
        elif percent >=50 and percent <70:
            Grade = "C";
        else:
            Grade = "Fail";
        return Grade;
    def show(self):
        print("semester : ",self.semester)
        print("Total : ",self.calc_total())
        print("Percentage : ",self.calc_per())
        print("Grade : ",self.calc_grade())
        super().show()

#

s1 = Student()
st_name = input("Enter name : ")
st_birthdate = int(input("enter birthdate : "))
st_gender = input("enter gender : ")
st_sem = int(input("enter semester : "))
st_python = int(input("enter python marks : "))
st_java = int(input("enter java marks : "))
st_php = int(input("enter php marks : "))

s1.set(st_name,st_birthdate,st_gender,st_sem,st_python,st_java,st_php);
s1.show();

class Employee:
    def __init__(self,nm = "",gen="",bdat = 1996,basic_sal=0,da=0.5,hra=0.5,total_sal=0):
        self.basic_salary = basic_sal
        self.da = da;
        self.hra = hra;
        self.total_sal = total_sal
        super().__init__(nm,gen,bdat)


