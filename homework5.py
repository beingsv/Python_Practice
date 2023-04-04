#1 In dumps function what are the parameters that we have and what do they do, explain with small program

# We call the dump() function with the following parameters:
# data: The dictionary to be serialized into a JSON formatted string and saved to a file.
# outfile: A file object to which the JSON formatted string will be written.
# indent: Set to 4 to indent the output JSON with 4 spaces.
# sort_keys: Set to True to sort the keys of dictionaries in the output JSON.


import json

data = {
    "name": "Bob",
    "age": 30,
    "isStudent": True,
    "subjects": ["math", "science", "english"],
    "grades": {
        "math": 90,
        "science": 85,
        "english": 95
    },
    "address": "123 Main Street"
}

# Serialize the dictionary with various options
with open("data.json", "w") as outfile:
    json.dump(data, outfile, indent=4, sort_keys=True)

# Deserialize the JSON formatted string from the file
with open("data.json", "r") as infile:
    json_str = infile.read()
    data = json.loads(json_str)

# Print the deserialized data
print(data)



#2 How can we raise an exception, WAP.

x = 10

try:
    if x > 5:
        raise ValueError("x should not exceed 5.")
except ValueError as error:
    print(error) #output: x should not exceed 5.



#3 WAP on normal list comprehension and another program on list comprehension by using conditions 

# Normal List Comprehension
# create a list of squares of numbers from 1 to 10 using list comprehension
sq = [num ** 2 for num in range(1, 11)]
print(sq) #output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# List Comprehension with Conditions
# create a list of even numbers from 1 to 20 using list comprehension and conditions
evens = [num for num in range(1, 21) if num % 2 == 0]
print(evens) #output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]




