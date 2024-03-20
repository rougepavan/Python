st=input("enter the given string:")
temp=st
rev=""
n=len(st)
for i in range(0,n):
    rev+=st[i]
if(rev==temp):
    print(rev , "string is a palindroem")
else:
    print(temp,"string is not a palindrome")
temp.upper()
print(temp.upper())
