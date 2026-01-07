#LISTS
lis = [1,2,3,4]  #this is basic list (same data type)

lis2 = [1,"Simran","AI/ML"] #this is list containing different data types

lis.append(3)
print (lis)
#Output = [ 1, 2, 3, 4, 3]

lis.extend([4,5])
print (lis)
#Output = [1, 2, 3, 4, 3, 4, 5]

print(lis.count(3))
#Output = 2

lis.insert(1,10)
print(lis)
#Output = [1, 10, 2, 3, 4, 3, 4, 5]

lis.pop()
print (lis)
#Output = [1, 10, 2, 3, 4, 3, 4]

print(lis.index(10)) 
#Output = 1

lis.clear()
print(lis)
#Output = 0

#List Comprehension

a = [i for i in range(10)]
print (a) 
#Output = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

b = [[i for i in range(3)] for j in range(3)]
print(b)
#Output = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

c= [i for i in range(1,10) if i%2==0]
print (c)
#Output = [2, 4, 6, 8]


# TUPLES

# Tuples are ordered, immutable (cannot be changed)

tup = (1, 2, 3, 4)   # basic tuple
print(tup)
# Output = (1, 2, 3, 4)

tup2 = (1, "Simran", "AI/ML")  # tuple with different data types
print(tup2)
# Output = (1, 'Simran', 'AI/ML')

print(tup[1])
# Output = 2

print(tup.count(2))
# Output = 1

print(tup.index(3))
# Output = 2

# Tuples cannot be modified
# tup[0] = 10  ERROR (immutable)

# Tuple unpacking
a, b, c, d = tup
print(a, b, c, d)
# Output = 1 2 3 4

#There is no Tuple Comprehension

# DICTIONARY

# Dictionary stores data in key-value pairs

dic = {
    "name": "Simran",
    "course": "AI/ML",
    "age": 21
}
print(dic)
# Output = {'name': 'Simran', 'course': 'AI/ML', 'age': 21}

print(dic["name"])
# Output = Simran

# Add new key-value pair
dic["college"] = "B.Tech"
print(dic)
# Output includes college key

# Update value
dic["age"] = 22
print(dic)

# Remove key
dic.pop("course")
print(dic)

#Remove Last Item
dic.popitem()
print(dic)

# Get all keys
print(dic.keys())

# Get all values
print(dic.values())

# Get all key-value pairs
print(dic.items())

# Dictionary comprehension
squares = {i: i*i for i in range(5)}
print(squares)
# Output = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
