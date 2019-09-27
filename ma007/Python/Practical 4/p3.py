class Student:
    total_count=0;
    def __init__(self,rno,name,c_marks,cpp_marks,python_marks):
        print("constructor called")
        self.rno=rno;
        self.name=name;
        self.c_marks=c_marks;
        self.cpp_marks=cpp_marks;
        self.python_marks=python_marks;
        Student.total_count=Student.total_count+1;

    def input(self):
        rno=int(input("Enter roll no: "))
        name=input("Enter name : ")
        c_marks=int(input("Enter c marks : "))
        cpp_marks=int(input("Enter cpp marks : "))
        python_marks=int(input("Enter python marks: "))

    def total_calc(self):
        Total=self.c_marks+self.cpp_marks+self.python_marks;
        return Total;
    def calc_percentage(self):
        perc = (self.total_calc()//3);
        return perc;
    def calc_grade(self):
        p = self.calc_percentage();
        if p >= 90 and p < 100:
             grade = "A";
        elif p >=70 and p < 90:
            grade = "B";
        elif p >=50 and p <70:
            grade = "c";
        elif p >=40 and p <50:
            grade = "D";
        else:
            grade = "Fail!";
        return grade;
    def show(self):
        print("Roll no : ",self.rno)
        print("Name : ",self.name)
        print("c marks : ",self.c_marks)
        print("cpp marks : ",self.cpp_marks)
        print("python marks : ",self.python_marks)
        print("total : ",self.total_calc())
        print("Percentage : ",self.calc_percentage())
        print("Grade : ",self.calc_grade())

s1 = Student(7,"vidhi",78,88,87);

#s1.input();
s1.total_calc();
s1.calc_percentage();
s1.calc_grade();
s1.show();
        
