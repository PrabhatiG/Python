#Given Lists
listOne=[10,20,23,11,17]
listTwo=[13,43,24,36,12]
	
# Print the lists
print("First List", listOne)
print("Second List",listTwo)
	
# Declare a third list that will contain the result
thirdlist=[]

# Iterate through first list to get odd elements
for num in listOne:
    if(num%2!=0):
      thirdlist.append(num)

# Iterate through second list to get even elements
for num in listTwo:
    if(num%2==0):
      thirdlist.append(num)

#Print Result
print("result list is:")
print(thirdlist)
       
   