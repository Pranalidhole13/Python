# Dictionary is used to store data values in key & value
#It is ordered and changeable
# No duplicates are allowed
student = {
    "name":"Pranali",
    "age":22,
    "marks":[93,99,87,91],
    "subject" : {
        "physics":56,
        "chemistry":89,
        "maths":97
    },
    "is_qualify":True
}

print(student["name"])  # to print one pair of key & value
print(student)          # to print whole dictionary
#subject is a nested dictionary
print(student["subject"])


# print(student.keys())