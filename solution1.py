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

    @classmethod
    def from_csv_line(cls, csv_line):
        """Handle CSV with messy spacing and case"""
        parts = [item.strip() for item in csv_line.strip().split(",")]
        name = parts[0].title()
        age = int(parts[1])  # Convert to int!
        grade = parts[2].strip()
        email = parts[3].lower()
        return cls(name, age, grade, email)

    @classmethod
    def from_form_data(cls, form_dict):
        """Handle form data with different field names"""
        name = form_dict["student_name"].title().strip()
        age = int(form_dict["student_age"])  # Convert to int!
        grade = form_dict["final_grade"].strip()
        email = form_dict["contact_email"].lower().strip()
        return cls(name, age, grade, email)

    @classmethod
    def from_pipe_separated(cls, pipe_data):
        """Handle pipe-separated data"""
        parts = pipe_data.strip().split("|")
        name = parts[0].title()
        age = int(parts[1])  # Convert to int!
        grade = parts[2].strip()
        email = parts[3].lower()
        return cls(name, age, grade, email)

    @classmethod
    def from_mixed_format(cls, weird_string):
        """Handle 'Key: value' format"""
        parts = weird_string.split(", ")
        data = {}
        for part in parts:
            key, value = part.split(": ")
            data[key.lower()] = value.strip()

        name = data["name"].title()
        age = int(data["age"])
        grade = data["grade"]
        email = data["email"].lower()
        return cls(name, age, grade, email)

    @classmethod
    def from_json_like_string(cls, json_str):
        """Handle JSON-like string (but not real JSON)"""
        import ast

        data = ast.literal_eval(json_str)  # Convert string to dict

        name = data["full_name"].title()
        age = int(data["years_old"])
        grade = data["letter_grade"]
        email = data["email_addr"].lower()
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
    print("=== Testing CSV ===")
    for csv_line in csv_samples:
        try:
            student = Student.from_csv_line(csv_line)
            print(f"✅ CSV: {student}")
        except Exception as e:
            print(f"❌ CSV Error: {e}")

    print("\n=== Testing Form Data ===")
    for form_data in form_samples:
        try:
            student = Student.from_form_data(form_data)
            print(f"✅ Form: {student}")
        except Exception as e:
            print(f"❌ Form Error: {e}")

    print("\n=== Testing Pipe Separated ===")
    for pipe_data in pipe_samples:
        try:
            student = Student.from_pipe_separated(pipe_data)
            print(f"✅ Pipe: {student}")
        except Exception as e:
            print(f"❌ Pipe Error: {e}")

    print("\n=== Testing Mixed Format ===")
    for mixed_data in mixed_samples:
        try:
            student = Student.from_mixed_format(mixed_data)
            print(f"✅ Mixed: {student}")
        except Exception as e:
            print(f"❌ Mixed Error: {e}")

    print("\n=== Testing JSON-like ===")
    for json_data in json_like_samples:
        try:
            student = Student.from_json_like_string(json_data)
            print(f"✅ JSON: {student}")
        except Exception as e:
            print(f"❌ JSON Error: {e}")
