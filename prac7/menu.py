def menu():
    print("1.String Length");
    print("2.Join Strings");
    print("3.Compare Strings");
    print("4.Reverse Strings");
    print("5.Check String is Palindrome or not");
    print("6.Check word in sentence");

def get_choice():
    ch=int(input("Enter your choice:"));
    return ch;

menu();
ch=get_choice();

def getlength(str):
    print("String length:");
    l=len(str);
    return l;

def getjoin(str,str1):
    str2=str+str1;
    return str2

def com_str(str,str1):
    if((str,str1)==0):
        return 0;
    else:
        return 1;

def rev_str(str):
    str="".join(reversed(str));
    return str;

def palindrome(str):
    str="".join(reversed(str));
    if(str==0):
        return 0;
    else:
        return 1;

def check_word(str):
    if(str==0):
        return 0;
    else:
        return 1;

if(ch==1):
    s="Godiwala";
    len=getlength(s);
    print("Lenth=",len);

elif(ch==2):
    s1=" Liza ";
    s2=" Godiwala ";
    string=getjoin(s1,s2);
    print("String is=",string);

elif(ch==3):
    st1="Abc";
    st2="Abc";
    st3=com_str(st1,st2);
    if(st3 !=0):
        print ("Strings are same");
    else:
        print("Strings are not same");

elif(ch==4):
    s1="Godiwala";
    re=rev_str(s1);
    print(s1,"Reverse String is",re);

elif(ch==5):
    s1="abc";
    p=palindrome(s1);
    if(p==0):
        print(s1,"palindrome");
    else:
        print (s1,"not palindrome");

elif(ch==6):
    s1="Liza Godiwala";
    ser=input("enter word to be search:");
    f=s1.find(ser);
    if(f==0):
        print("Word is found");
    else:
        print("Word is not found");
    


    
    


    
    

