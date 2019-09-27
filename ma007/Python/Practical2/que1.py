num1=int(input("enter number1: "));
num2=int(input("enter number2: "));

if num1>num2:
    for n in range(num2-1,num1,1):
        if n % 2!=0:
            print(n);         

        
            
