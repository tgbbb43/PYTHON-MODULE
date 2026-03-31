

# class Student:
#     def __init__(self, name, grades = (0, 0, 0, 0)):
#         self.name = name
#         self.grades = grades

#     def average(self):
#         return sum(self.grades) / len(self.grades)

# student1 = Student("Rolf", (90, 90, 85, 88))
# student2 = Student("Anna", (78, 82, 80, 79))
# student3 = Student("Ben", (88, 91, 87, 90))
# student4 = Student("Lila", (92, 89, 94, 91))

# # print(student1.name)
# # print(student1.grades)

# print(student1.average())
# print(student2.average())
# print(student3.average())
# print(student4.average())

# ? 6.1

# 1
# class Person:
#     def __init__(self, name, age,city,job):
#         self.name = name
#         self.age = age
#         self.city = city
#         self.job = job
        
# person1 = Person("James Wilson", 28, "London", "DevOps Engineer")
# person2 = Person("Sarah Miller", 34, "New York", "Data Scientist")
# person3 = Person("Alex Chen", 22, "Tokyo", "Student")     

# print(person1.city)   
# print(person2.job)   
# print(person3.city)   

# 2
# class Car:
#     def __init__(self, brand, model,year,color):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.color = color
        
# car1 = Car("Tesla", "Model 3", 2023, "White")
# car2 = Car("Toyota", "Corolla", 2021, "Silver")
# car3 = Car("Ford", "Mustang", 1967, "Red")    

# print(f"Car 1: {car1.brand} {car1.model} ({car1.year})")

# 20
# class GymMember:
#     def __init__(self,name,age,membership_type,months_left):
#         self.name = name
#         self.age = age
#         self.membership_type = membership_type
#         self.months_left = months_left
        
# member1 = GymMember("Michael Jordan", 23, "Premium", 12)
# member2 = GymMember("Serena Williams", 31, "Basic", 5)
# member3 = GymMember("Tom Brady", 45, "VIP", 24)
# print(f"Member: {member1.name}, Plan: {member1.membership_type}, Time left: {member1.months_left} months")

