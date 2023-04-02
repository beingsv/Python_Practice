def fact(x):
    if x == 1:
        return 1
    else:
        return (x * fact(x-1))

num = 3
print("The factorial of", num, "is", fact(num))