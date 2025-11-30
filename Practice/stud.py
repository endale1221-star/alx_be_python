
#Define a Student class with attributes like name and age. Include a method to display student information.
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def display_info(self):
        print(f"student Name:{self.name}")
        print(f"student Age: {self.age}" ) 


student1=Student("Endalew",22)
student2=Student("Dagim",23)
student3=Student("Kalab",24)

student1.display_info()

#Define a Product class with attributes like name, price, and quantity. Implement a method to calculate the total value of products in stock.
class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def total_Value(self):
        return self.price*self.quantity


p1=Product("Laptops",45000,6)
p2=Product("Headsets",1250,4)
p3=Product("Books",250,12)

print(p1.total_Value())
print(p2.total_Value())
print(p3.total_Value())








