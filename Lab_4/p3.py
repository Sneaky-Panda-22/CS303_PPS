database = {"Nishal" : ["UG25CSE068"],
            "Om" : ["UG25CSE069", "UG25CSE070"]}

new_database = {rollno: name for name,rollnos in database.items() for rollno in rollnos}

print(new_database)