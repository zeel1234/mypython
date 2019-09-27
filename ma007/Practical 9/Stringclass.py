class String:

    def __init__(self,st = ""):
        self.str = st
    def set(self,st = ""):
        self.str = st;
    def get(self):
        return self.str;
    def length(self):
        return len(self.str)
    def join(self,str2 = ""):
        return self.str+str2.str;
    def Compare(self,str3 = ""):
        if self.str == str3.str:
            print("Strings are same")               
        else:
            print("Strings are not same")
    def Reverse(self):
        print("reverse string : ",self.str[::-1])
    def check_Palindrome(self):
        str_rev = self.str[::-1]
        if self.str == str_rev:
            print("Strings are palindrome !")
        else:
            print("Strings are not palindrome !")
    def word_in_sentence(self):
        if self.str in "This is ddu ":
            print("word found !")
        else:
            print("word not found !")
        
      

#

s1 = String()
temp = input("enter string : ")
s1.set(temp)
print("string  = ",s1.get())
print("length : ",s1.length())
s2 = String()
temp2  = input("enter join string : ")
s2.set(temp2)
print("joining strings : ",s1.join(s2))
s1.Compare(s2)
s1.Reverse()
s1.check_Palindrome()
s1.word_in_sentence()
                

