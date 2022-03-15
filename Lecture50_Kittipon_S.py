#Add, Subtract, Multiply, Divide
def add(x,y):
    print("Result:",x+y)
def subtract(x,y):
    print("Result:",x-y)
def multiply(x,y):
    print("Result:",x*y)
def divide(x,y):
    print("Result:",x/y)

x = int(input("Please Enter number of x: "))
y = int(input("Please Enter number of y: "))
print(""" 1: Add +
2: Subtract -
3: Multiply x
4: Divide /
""")
chooseInput = int(input("Choose an options!"))
if chooseInput == 1:
    add(x,y)
elif chooseInput == 2:
    subtract(x,y)
elif chooseInput == 3:
    multiply(x,y)
elif chooseInput == 4:
    divide(x,y)
else:
    print("Error!")