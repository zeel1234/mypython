rno=int(input("Enter Rno:"));
name=(input("Enter Name:"));
c_marks=int(input("Enter C marks:"));
cpp_marks=int(input("Enter c++ marks:"));
p_marks=int(input("Enter Python marks:"));


class student:
    
    def __init__(self):
        self.rno=rno;
        self.name=name;
        self.c_marks=c_marks;
        self.cpp_marks=cpp_marks;
        self.p_marks=p_marks;
        self.tot=c_marks+cpp_marks+p_marks;
        #self.t_marks=300;
        self.per=(self.tot/300)*100;

    def data(self):
        print("______________________________________");
        print("RollNo=",self.rno);
        print("Name=",self.name);
        print("C Marks=",self.c_marks);
        print("C++ Marks=",self.cpp_marks);
        print("Python Marks=",self.p_marks);
        print("Total=",self.tot);
        print("percentage=",self.per,"%");
        if self.per<99 and self.per>80:
            print(self.per,"% is in  distiction")
            print("Grade=A1");
        elif self.per<80 and self.per>60:
            print(self.per,"% is in  First Class")
            print("Grade=A2");
        elif self.per<60 and self.per>50:
            print(self.per,"% is in Second class")
            print("Grade=B1");
        elif self.per<50 and self.per>35:
            print(self.per,"% is in pass class")
            print("Grade=B2");
        else:
            print(self.per,"% is fail")
        print("______________________________________");

s1=student()

s1.data()
