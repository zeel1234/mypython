sub1 = int(input("Enter marks for subject1 : "));
sub2 = int(input("Enter marks for subject2 : "));
sub3 = int(input("Enter marks for subject3 : "));
sub4 = int(input("Enter marks for subject4 : "));
total = sub1+sub2+sub3+sub4;
perc = total/4;

if perc >= 90 and perc <100:
    g='A';
elif perc >=80 and perc <90:
    g='B';
elif perc >=70 and perc <80:
    g='C';
elif perc >=60 and perc <70:
    g='D';
elif perc >=50 and perc <60:
    g='E';
else:
    g='Fail';

print("Grade : ",g);


