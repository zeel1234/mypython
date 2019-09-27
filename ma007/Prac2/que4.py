import datetime;
import sys;

args = sys.argv;
start = datetime.datetime.now();
num = int(args[1]);

number = num;
r=0;
for i in range(num):
    d=num%10;
    r=(r*10)+d;
    num=num//10;

if r==number:
    print("is prime");
else:
    print("is not prime");

end = datetime.datetime.now();
elapsed = start - end;
print(elapsed);

