#Given list of numbers
#numList=[10,20,30,40,10]
numList=list(input("Enter a list of comma seperated values: ").split(","))
print("Given list is", numList )

#Get the first element in the list
firstElement= numList[0]

#Get the last element in the list
lastElement=numList[-1]

#Check if the first and last number are equal
if(firstElement==lastElement):
    print(True)
else:
    print(False)
