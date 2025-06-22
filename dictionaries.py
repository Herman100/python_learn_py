from greetings import greetingUser

student = {
    "name": "John Doe",
    "age": 20,
    "major": "Computer Science",
    "courses": ["Data Structures", "Algorithms", "Operating Systems"],
    "gpa": 3.8,
    "is_full_time": True,
    "graduation_year": 2024,
    "advisor": {
        "name": "Dr. Smith",
        "department": "Computer Science",
        "office": "Room 101",
    },
}


# print(student["advisor"]["name"])


greetingUser(student["name"])
