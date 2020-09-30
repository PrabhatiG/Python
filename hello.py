print("hello world")
print ("hi")
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x)) # Output: <class 'int'>
print(type(y)) # Output: <class 'float'>
print(type(z)) # Output: <class 'complex'>
a = "Hello, World!"
print(a[1]) # Output: "e"
txt = "The rain in Spain stays mainly in the plain"
	
x = "ain" in txt
	
y = "ain" not in txt
	
print(x) # True
	
print(y) # False

#strings
a="Hello"
b=" world"
c=a+b
print(c)

#string format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
# Output: My name is John, and I am 36

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# Output: I want 3 pieces of item 567 for 49.95 dollars.
