# get user input
main = input("Expression: ")
# convert these into variables
x, y, z = main.split(" ")
# change type of vbariable x and z to float
float_x = float(x)
float_z = float(z)
# calc result

def mul():
    print(float_x * float_z)

def add():
    print(float_x + float_z)

def sub():
    print(float_x - float_z)

def div():
    print(float_x / float_z)

if '*' in main:
    mul()

elif '+' in main:
    add()

elif '-' in main:
    sub()
    
elif '/' in main:
    div()