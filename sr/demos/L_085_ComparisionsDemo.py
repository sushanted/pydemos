list_one = [1,2,3]
list_two = [1,2,3]

# Objects comparisions
print("Equals:",list_one==list_two)
print("Same:",list_one is list_two)
print("Not Same:",list_one is not list_two)

# Contains
print("In:", 1 in list_one)
print("Not in:",5 not in list_two)

# Chained comparisions : all comparisions should be true
# Same as 3 < 4 and 4 == 4
print("3 < 4 == 4",3 < 4 ==4)
print("3 < 4 == 5",3 < 4 ==5)
print("5 < 4 == 4",5 < 4 == 4)

if(3==3 and (4>2 or 6<2)):
    print(True)

# Assignment inside expressions : use walrus operator ":="
b=(a:=4)
print(a,b)

a=5
while((a:=a-1)>0):
    print(a)

# Comparing types:
print("(1,2,3)>(1,1,0): ",(1,2,3)>(1,1,0))

print("List is different than a tuple:",[1,2,3]!=(1,2,3))
print("List is different than a set:",[1,2,3]!={1,2,3})

