import time;
import sys;

args = sys.argv;
start = time.time();
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

end = time.time();
elapsed = start - end;
time.strftime("%H:%M:%S", time.gmtime(elapsed));

