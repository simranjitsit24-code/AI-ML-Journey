#Iteration through Lists

lis  = [1,2,3,"Simranjit Singh" , " AI/ML"]

for i,j in enumerate(lis):
    print("Index : ",i,"Value :",j)

#Iteration through Tuples

tup = (1,2,4,"Simran" , "AI/ML")

for i in tup:
    print(i)

#Iteration through dictionary

student = {"name": "Simran", "course": "AI/ML", "year": 4}

for key in student:
    print(key, student[key])

for key, value in student.items():
    print(key, ":", value)


# Function with *args
def total_sum(*nums):
    return sum(nums)

print(total_sum(1, 2, 3, 4))

# Function with **kwargs
def student_info(**info):
    for key, value in info.items():
        print(key, ":", value)

student_info(name="Simran", course="AI/ML", year=4)

# *args plus **kwargs
def demo(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

demo(1, 2, 3, name="Simran", field="AI/ML")

#  else statement can also be added in the end of loop
i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Loop completed successfully")
