students = {}
for i in range(3):
    roll_no = input(f"Enter roll number for student {i+1}: ")
    name = input(f"Enter name for student {i+1}: ")
    students[roll_no] = name
print("\nStudent Dictionary:")
for roll, name in students.items():
    print(f"Roll No: {roll}, Name: {name}")
