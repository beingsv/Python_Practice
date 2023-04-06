#1 Difference between dump() and dumps() in python

# dump() is used to write JSON data directly to a file-like object, 
# while dumps() is used to return a string representation of the JSON data.

#2 
def funcs(**kwargs):
    for key, value in kwargs.items():
        print("%s = %s" % (key, value))

funcs(Name = 'Shiwam Vishwakarma', City = 'Varanasi', Age = '22')

#output: Name = Shiwam Vishwakarma
#        City = Varanasi    
#        Age = 22
