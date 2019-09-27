numbers_addition = lambda n1,n2:n1+n2;

print(numbers_addition(2,5))


lst = [1,2,3,4]
lst1 = list(filter(lambda x:(x%2==0),lst))
print(lst1)


str = "python"

newstr = lambda c:c.upper();

print(newstr(str))

strlst = ['python','program'];

newlist = list(filter(lambda i:(i.upper()),strlst))

print(newlist)

