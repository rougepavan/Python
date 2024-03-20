m=int(input("Enter the number of fresh loves purchased:"))
n=int(input("Enter the number of day old loaves purchased"))
regular_cost=185.00
print("regular price",regular_cost)
old=regular_cost*0.6
re1_cost=regular_cost-old
print("amount of new leaves:",regular_cost*m)
print("amount of old leaves:",re1_cost*n)
total=regular_cost*m+re1_cost*n
print("total cost is:",total)
