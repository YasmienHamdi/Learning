print("helloworld")
print(2*"\n")
print("Welcome to", end=" ")
print("Guru99!")


#Declare and redeclare variable
f = 50
print(f)
f = "python"
print(f)

#String concatenation and variable
#example1
a = "guru"
b = 99
print(a+str(b))
#example2
print("guru"+"99")
a = 99
print("guru"+str(a))

#Local and global variable
x = 100
print(x)
def somefunction():
    x="I am learning python"
    print(x)
somefunction()
print(x)

#Referencing the global variable inside a function
z = 123
print(z)
def somefunction():
    global z
    print(z)
    z = "changing global variable"
somefunction()
print(z)

#Escape character \t
print("Manually\tadd\tspace\tin\tguru99")

#chr() and ord()
print("the unicode character is")
ord = ord("\t")
print(ord)
print("guru"+chr(9)+"99")

#Python version
from platform import python_version
print("Current python version is",python_version())



