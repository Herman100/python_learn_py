# DIRTY DATA CHALLENGE: Student Management System
# Your mission: Create alternative constructors to handle this mess!


class Student:
    def __init__(self, name, age, grade, email):
        """Clean constructor - expects pristine data"""
        self.name = name
        self.age = age
        self.grade = grade
        self.email = email

    def __str__(self):
        return f"Student(name='{self.name}', age={self.age}, grade={self.grade}, email='{self.email}')"

    # YOUR TASK: Create @classmethod alternatives for the dirty data below!

    # TODO: @classmethod from_csv_line(cls, csv_line)
    # Handle: "  john DOE , 17, A+ , john.doe@school.edu  "
    @classmethod
    def from_csv_line(cls, csv_line):
        clean_data = []
        for item in csv_line.strip().split(","):
            clean_data.append(item.strip())

        clean_data[0] = clean_data[0].lower().title()
        name, age, grade, email = clean_data

        return cls(name, age, grade, email)

    # TODO: @classmethod from_form_data(cls, form_dict)
    # Handle: {'student_name': 'JANE SMITH', 'student_age': '16', 'final_grade': 'B', 'contact_email': 'jane@email.com'}

    @classmethod
    def from_form_data(cls, form_dict):
        name = form_dict["student_name"].lower().strip().title()
        age = form_dict["student_age"].lower().strip().title()
        grade = form_dict["final_grade"].strip().upper()
        email = form_dict["contact_email"].lower().strip()

        return cls(name, age, grade, email)

    # TODO: @classmethod from_pipe_separated(cls, pipe_data)
    # Handle: "mike|18|C+|mike.wilson@uni.edu"
    @classmethod
    def from_pipe_separated(cls, pipe_data):
        clean_data = pipe_data.strip().split("|")
        clean_data[0] = clean_data[0].lower().title()
        name, age, grade, email = clean_data

        return cls(name, age, grade, email)

    # TODO: @classmethod from_mixed_format(cls, weird_string)
    # Handle: "Name: sarah connor, Age: 19, Grade: A-, Email: sarah.connor@college.edu"
    @classmethod
    def from_mixed_format(cls, weird_string):
        list_data = weird_string.strip().split(",")
        clean_data = []

        for string in weird_string:
            clean_data.append(string.split(":")[1])

        name, age, grade, email = clean_data

        return cls(name, age, grade, email)

    # TODO: @classmethod from_json_like_string(cls, json_str)
    # Handle: "{'full_name': 'Bob Johnson', 'years_old': '20', 'letter_grade': 'B+', 'email_addr': 'bob.j@university.edu'}"
    @classmethod
    def from_json_like_string(cls, json_str):
        name = json_str.full_name.lower().strip().title()
        age = json_str.years_old.lower().strip().title()
        grade = json_str.letter_grade.strip().upper()
        email = json_str.email_addr.lower().strip()

        return cls(name, age, grade, email)


# DIRTY DATA SAMPLES TO TEST YOUR METHODS:

# CSV format (messy spacing, inconsistent case)
csv_samples = [
    "  john DOE , 17, A+ , john.doe@school.edu  ",
    "ALICE WONDER,16,B-,alice@wonderland.edu",
    "  bob SMITH  , 18 , C , bob.smith@college.edu  ",
]

# Form data (different field names)
form_samples = [
    {
        "student_name": "JANE SMITH",
        "student_age": "16",
        "final_grade": "B",
        "contact_email": "jane@email.com",
    },
    {
        "student_name": "TOM HARDY",
        "student_age": "17",
        "final_grade": "A",
        "contact_email": "tom.hardy@school.org",
    },
]

# Pipe separated
pipe_samples = ["mike|18|C+|mike.wilson@uni.edu", "emma|19|A-|emma.stone@college.edu"]

# Mixed format (key-value pairs)
mixed_samples = [
    "Name: sarah connor, Age: 19, Grade: A-, Email: sarah.connor@college.edu",
    "Name: JACK SPARROW, Age: 18, Grade: B+, Email: jack@pirates.edu",
]

# JSON-like strings (but not real JSON)
json_like_samples = [
    "{'full_name': 'Bob Johnson', 'years_old': '20', 'letter_grade': 'B+', 'email_addr': 'bob.j@university.edu'}",
    "{'full_name': 'LISA SIMPSON', 'years_old': '16', 'letter_grade': 'A+', 'email_addr': 'lisa@springfield.edu'}",
]

# BONUS CHALLENGE: Handle invalid data gracefully
invalid_samples = [
    "incomplete,data",  # missing fields
    "john,not_a_number,A,john@email.com",  # invalid age
    "",  # empty string
    "name only",  # completely wrong format
]

# Test your methods like this:
if __name__ == "__main__":
    # Test CSV
    for csv_line in csv_samples:
        try:
            student = Student.from_csv_line(csv_line)
            print(f"✅ CSV: {student}")
        except Exception as e:
            print(f"❌ CSV Error: {e}")

    # Test other formats...
    # student = Student.from_form_data(form_samples[0])
    # print(student)
