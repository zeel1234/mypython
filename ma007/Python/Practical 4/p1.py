def strings_fun():
    str1="python"
    ll = ['python','program','work']
    sp = " "
    str2="program"
    print("1.string length\n2.join strings\n3.compare strings\n4.reverse string\n5.check palindrome\n6.check word in sentance\n");
    choice=int(input("Enter choice: "))
    if choice==1:
        print("length of ",str1,"is ",len(str));
    elif choice==2:
        print(sp.join(ll))
    elif choice==3:
        if str1==str2:
            print("same")
        else:
            print("not same")
    elif choice==4:
        print(str1[::-1])
    elif choice==5:
        newstr = str1[::-1]
        if str1 == newstr:
            print("palindrome")
        else:
            print("not palindrome")
    elif choice==6:
        str3 = "python program lab"
        word = "lab"
        val = str3.find(word,0,len(str3))
        if val == -1:
            print(word ," not found")
        else:
            print(word," found !")
   
            

strings_fun()
