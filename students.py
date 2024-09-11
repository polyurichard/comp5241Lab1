import json

# Step 2: Open and read the JSON file
with open('students.json', 'r') as file:
    data = json.load(file)

# Step 4: Extract the list of students
students = data['students']

# Step 5: Iterate through the list and print each student's details
for student in students:
    print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")

# print the second student's name
print(f"Second student's name: {students[1]['name']}")
print(f"Second student's age: {students[1]['age']}")