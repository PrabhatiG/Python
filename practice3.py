def test(i,j):
    if(i==0):
        return j
    else:
        return test(i-1,i+j)

print(test(4,7))

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a) 

def test(i,j):
    if(i==0):
        return j
    else:
        return test(i-1,i+j)

print(test(2,1))