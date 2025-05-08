class dog:
    def __init__(self, name , age , color,owner):
        self.name = name 
        self.age =age 
        self.color = color
        self.owner = owner


    def bark(self):
        print("WOOF WOOF")

    def run(self):
        print("RUN RUN")

class Owner:
    def __init__(self, name ,  address , contact_number):
        self.name = name
        self.address = address
        self.contact_number = contact_number

    def walk(self,dog):
        print(f"{self.name} is walking {dog.name}")


        


owner1 = Owner("John", "123 Main St", "555-1234")
dog1 = dog("Buddy", 3, "Brown",owner1)
dog1.bark()
owner1.walk(dog1)
print(dog1.owner.address)