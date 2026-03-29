# friend_ages = {
#     "Rolf": 24,
#     "Adam": 30,
#     "Anne": 27
# }

# print(friend_ages["Anne"])

# friend_ages = {
#     "Rolf": 40,
#     "Adam": 30,
#     "Bob": 20
# }

# for n in friend_ages:
#     if "Bob" in n:
#         print("Bob attended")

# student_attendance = {
#     "Rolf": 96,
#     "Bob": 80
# }

# for s in student_attendance:
#     print(s,student_attendance[s])

# student_attendance = {
#     "Rolf": 96,
#     "Bob": 80
# }

# for name, score in student_attendance.items():
#     print(f"{name} {score}")

student_attendance = {"Rolf": 100, "Bob": 80, "Anne": 60}
scores = student_attendance.values()
average = sum(scores) / len(scores)
print(average)

# תרגיל 9 — רשימה של Dictionaries (גישה לאינדקס ולמפתח)
friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30}
]
print(friends[1]["name"])

# תרגיל 10 — סינון מתוך רשימת Dictionaries
friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 27}
]
result = []
for friend in friends:
    if friend["age"] > 25:
        result.append(friend)
print(result)