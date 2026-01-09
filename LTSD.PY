
#--------------------------------LIST---------------------------------


my_list = [10, 20, 30, 40]

# Creating a list
numbers = [10, 20, 30, 40, 20]

# Accessing elements
print(numbers[0])     

# Modifying elements
numbers[1] = 25
print(numbers)        

# Adding elements
numbers.append(50)
print(numbers)       

# Removing elements
numbers.remove(20)
print(numbers)       


#--------------------------------TUPLE---------------------------------


my_tuple = (10, 20, 30)

# Creating a tuple
fruits = ("apple", "banana", "cherry", "apple")

# Accessing elements
print(fruits[1])     

# Tuple cannot be modified
# fruits[1] = "mango"  --- ERROR

# Length of tuple
print(len(fruits))   


#--------------------------------SET---------------------------------

my_set = {10, 20, 30}

# Creating a set
numbers = {10, 20, 30, 20, 40}

# Duplicates are removed automatically
print(numbers)   

# Adding elements
numbers.add(50)
print(numbers)

# Removing elements
numbers.remove(20)
print(numbers)

A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)   # Union: {1, 2, 3, 4, 5}
print(A & B)   # Intersection: {3}
print(A - B)   # Difference: {1, 2}


#--------------------------------DICTIONARY---------------------------------


my_dict = {"name": "John", "age": 25}

# Creating a dictionary
student = {
    "name": "Alice",
    "age": 22,
    "course": "Python"
}

# Accessing values
print(student["name"])     

# Modifying values
student["age"] = 23

# Adding new key-value
student["grade"] = "A"

# Removing a key
del student["course"]

print(student)

for key, value in student.items():
    print(key, ":", value)