import sys;

length=(len(sys.argv))-1;
print(length);
avg=0;

args = sys.argv;




for num in range(length):
    avg=(avg+(int(args[num+1])));

max=int(args[1]);
for i in range(length):
    if (int(args[i+1]))>max:
        max=int(args[i+1]);

min=int(args[1]);
for i in range(length):
    if (int(args[i+1]))<min:
        max=int(args[i+1]);


tavg=avg//length;

print("Average: ",tavg);
print("maximun: ",max);
print("minimum: ",min);

    



