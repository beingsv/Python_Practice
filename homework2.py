#1. How to access a particular element in set?
#we can't access becasue its immutable but we can confirm either it is present or not
s = {1,2,3,4,5,6}
if 5 in s:
    print("Yes! 5 is in Set") #output = "Yes! 5 is in Set"
else:
    print("No! 5 is not in Set")

#or we can do is to convert set into list and then access
ly = list(s)
print(ly[4]) #output = 5



#2. Difference b/w remove func and discard func
s.remove(3)
print(s) #output = {1, 2, 4, 5, 6}
#if item does not exist, remove() will give an error.
    #s.remove(7)
    #KeyError: 7

s.discard(4)
print(s) #output = {1, 2, 5, 6}
#if item does not exist, discard() will not give an error.



#3. What is intersection_update()
# intersection_update() is a built-in Python set method that updates a set object with the intersection of itself and another iterable.
seta = {1, 2, 3, 4}
setb = {2, 3, 4, 5}
seta.intersection_update(setb)
print(seta) #output = {2, 3, 4}



#4. What is symmetric_difference_update()
# it is a built-in Python set method that updates a set object with the symmetric difference of itself and another iterable.
setc = {1, 2, 3, 4}
setd = {2, 3, 4, 5}
setc.symmetric_difference_update(setd)
print(setc) #output = {1, 5}

#it is a built-in Python set method that returns a new set object with the symmetric difference of two sets.
set1 = {1, 2, 3, 4}
set2 = {2, 3, 4, 5}
nset = set1.symmetric_difference(set2)
print(nset) #output = {1, 5}



#5. What is dict() func
#this function is a way to create a new dictionary 
dictFruit = dict([('apple', 2), ('banana', 6), ('orange', 10)])
print(dictFruit) #output = {'apple': 2, 'banana': 6, 'orange': 10}



#6 Use append() by converting tuple into list
my_tuple = (1, 2, 3, 4)
my_list = list(my_tuple)  
my_list.append(5)
print(my_list)  #output = [1, 2, 3, 4, 5]



