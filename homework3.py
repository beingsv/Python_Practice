#1. What is difference b/w == & === ?

# the == operator is used for value comparison. 
a = 5
b = 5
if a == b:
    print("a and b are equal") #output: a and b are equal

# the === operator is not used in Python. 
# In Python, the 'is' operator is used for object identity comparison.
c = [1, 2, 3]
d = c
if c is d:
    print("c and d refer to the same object") #output: c and d refer to the same object



#2. Write a program by using pass statement and continue statement in if-else

fruits = ["apple", "banana", "orange", "kiwi", "grape", "pear"]

#print the fruits in the list
for fruit in fruits:
    if fruit == "kiwi":
        continue # skip kiwi
    print(fruit) #output: apple banana orange grape pear

for fruit in fruits:
    if fruit == "kiwi":
        break # break
    print(fruit) #output: apple banana orange

#print whether a number is positive, negative or zero using if-else statement
num = 5
if num > 0:
    print("Positive") #output: Positive
elif num < 0:
    print("Negative")
else:
    pass  #"pass" when num is zero



#3. Write a program by using range() with three parameter start, stop and step-size

for i in range(2, 11, 2):
    print(i) #output: 2 4 6 8 10

#In this for loop, range(2, 11, 2) generates the sequence of even numbers 
#between 2 (inclusive) and 11 (exclusive) with a step size of 2.
