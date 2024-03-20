def happy(n):
    sum=0
    temp=n
    while(temp!=0):
        rem=temp%10
        sum=sum+rem**2
        temp//=10
    return sum
num=int(input("enter the number"))
result=num
while result!=1 and result!=4:
    result=happy(result)
if result==1:
    print("True")
elif result==4:
    print("False")
