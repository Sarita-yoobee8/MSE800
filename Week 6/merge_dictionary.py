# Dictionary 1
student1 = {
    "name": "Alex",
    "age": 42,
    "course": "Data Analytics",
    "city": "Auckland",
    "status": "Lecturer"
}
 
# Dictionary 2
student2 = {
    "name": "Sophia",
    "age": 29,
    "course": "Software Engineering",
    "city": "Wellington",
    "status": "Student"
}
 
# Dictionary 3
student3 = {
    "name": "Michael",
    "age": 35,
    "course": "Cyber Security",
    "city": "Christchurch",
    "status": "Researcher"
}



merged_students = {
    **{k: v for k, v in student1.items() if "ex" in student1["name"].lower()},
    **{k: v for k, v in student2.items() if "ex" in student2["name"].lower()},
    **{k: v for k, v in student3.items() if "ex" in student3["name"].lower()}
}

print(merged_students)

