import sys;

args = sys.argv;

num1 = int(args[1]);
num2 = int(args[2]);

if num1>num2:
    for n in range(num2-1,num1,1):
        if n % 2!=0:
            print(n);
