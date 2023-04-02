#1 WAP using recursive function

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 6
ans = fibonacci(n)
print(ans)  #output: 8  [which is the 6th Fibonacci number]



#2 WAP to use lambda() into a another function

def op(num1, num2, opr):
    return opr(num1, num2)

result = op(5, 7, lambda x, y: x * y)
print(result) #output: 35  



#3 Make file and use read, write, open, with_open and append functions in python

# Create a new file named 'new.txt' and write some data to it
with open('new.txt', 'w') as f:
    f.write('This is a new file.')

# Read the data from the file
with open('new.txt', 'r') as f:
    data = f.read()
    print(data)

# Write additional data to the file
with open('new.txt', 'a') as f:
    f.write('\nHere is some additional data.')

# Read the data from the file again
with open('new.txt', 'r') as f:
    data = f.read()
    print(data)

# Overwrite the contents of the file
with open('new.txt', 'w') as f:
    f.write('This is the new content of the file.')

# Read the data from the file once more
with open('new.txt', 'r') as f:
    data = f.read()
    print(data)


