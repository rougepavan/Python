n=int(input("enter the number of elements in the list"))
list=[]
list2=[]
even_sum=0
odd_sum=0
for i in range(0,n):
    element = int(input(f'Enter the {i+1}th element: '))
    list.append(element)
for i in list:
    if(i%2==0):
        even_sum+=i
    else:
        odd_sum+=i
list2.append([even_sum**2,odd_sum**2])
print(list2)
