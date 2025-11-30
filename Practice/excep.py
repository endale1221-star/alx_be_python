
# Write a program that takes two numbers as input from the user and divides the first number by the second number.
# Handle the ZeroDivisionError exception to inform the user if they attempt to divide by zero.
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

try:
    result=num1/num2
except ZeroDivisionError:
    print ("Can't divide by zero")
else:
    print (int(result))      

# Write a program that attempts to open and read data from a file specified by the user.
# Handle the FileNotFoundError exception to provide a meaningful message if the file does not exist.

filename=input("Enter the file name to read: ")

try:
    with open(filename,"r") as file:
        data=file.read()
except FileNotFoundError:
    print(f"The file {filename} does not exist.")
else:
    print("File contents") 
    print(data)          