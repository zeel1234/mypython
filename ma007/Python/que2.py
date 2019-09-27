num1 = int(input("enter number1 : "));
num2 = int(input("enter number2 : "));

val1=type(num1);
val2=type(num2);

if val1==True and val2==True:
    summ = val1 + val2;
    print(val1,"+",val2,"=",summ);
    mul=val1*val2;
    print(val1,"*",val2,"= ",mul);
    sub=val1-val2;
    print(val1,"-",num2,"=",sub);
    div=val1/val2;
    print(val1,"/",val2,"= ",div);
else:
    print("Invalid numbers ");







