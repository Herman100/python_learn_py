def from_csv(csv_line):
    clean_data = []
    for item in csv_line.strip().split(","):
        clean_data.append(item.strip())

    clean_data[0] = clean_data[0].lower().title()

    return clean_data


from_csv("  john DOE , 17, A+ , john.doe@school.edu  ")

form_sample = (
    {
        "student_name": "JANE SMITH",
        "student_age": "16",
        "final_grade": "B",
        "contact_email": "jane@email.com",
    },
)


from_form_data
