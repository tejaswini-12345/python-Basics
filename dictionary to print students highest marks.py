students = {
    "Tejaswini":100,
    "Rahul": 92,
    "Priya": 79,
    "Aman": 95,
    "Kiran": 85
}
highest_student = max(students, key=students.get)
print("Topper:", highest_student, "with marks", students[highest_student])
