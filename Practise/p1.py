# determine if you're in this course
# find Santa's email address
# modify Banta's grade
# Add youself and two other friends in it
# create a list of all student email address


# initial dict
students = {
    "Santa" : {
        "ID" : 1234567 ,
        "email" : "santa@iiitsurat.ac.in",
        "grade" : "A"
    },
    "Banta" : {
        "ID" : 3456789 ,
        "email" : "banta@iiitsurat.ac.in" ,
        "grade" : "B"
    }
}


if "Parth" in students:
    print(f"Yes I'm present!")
else:
    print(f"I'm not present!")


print(f"Santa's email address : {students["Santa"]["email"]}")


students["Banta"]["grade"] = "A"
# for student,student_d in students.items():
#     print(f"Student : {student}")
#     print(f"Details : {student_d}")


students["Parth"] = {
    "ID" : 1234,
    "email" : "p@iiitsurat.ac.in",
    "grade" : "B"
}
students["Kshitij"] = {
    "ID" : 1235,
    "email" : "k@iiitsurat.ac.in",
    "grade" : "AB"
}
students["Omi"] = {
    "ID" : 1236,
    "email" : "o@iiitsurat.ac.in",
    "grade" : "A+"
}

print("")
for student,student_d in students.items():
    print(f"Student : {student}")
    print(f"Details : {student_d}")

student_email = []
for student in students:
    student_email.append(students[student]["email"])

print(f"\nStudent emails addresses:")
print(f"{student_email}")