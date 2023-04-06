#1 If we have an object which has both instance as well as class attr, who will get preference?

# When an object has both instance attributes and class attributes with the same name, 
# the instance attribute takes precedence over the class attribute. 
# This means that if you access the attribute on the object, it will return the value of the instance attribute.

# However, if the object does not have an instance attribute with that name, 
# it will fall back to the class attribute and return its value.



#2 Create a class and make three object with different parameters and change the values when you retrive data from the class.
class insaan:
    def __init__(self, name, company, occupation):
        self.name = name
        self.company = company
        self.occupation = occupation
    
    def get_info(self):
        return f"{self.name} works in {self.company} as a {self.occupation}"
    

p1 = insaan("Shiwam", "cloudEQ", "Software Trainee")
p2 = insaan("Vaibhav", "phonePe", "SRE")
p3 = insaan("Ronak", "cloudEQ", "DevOps Engineer")

print(p1.get_info())  #output: Shiwam works in cloudEQ as a Software Trainee
print(p2.get_info())  #output: Vaibhav works in phonePe as a SRE
print(p3.get_info())  #output: Ronak works in cloudEQ as a DevOps Engineer



#3 Define Super method and Class method

# The super() method is used to call a method of the parent class from a subclass.

# A decorator that allows you to define a method that operates on the class itself, 
# rather than on instances of the class. This is often used as an alternative constructor for a class.






