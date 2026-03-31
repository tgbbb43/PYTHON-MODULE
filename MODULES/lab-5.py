#? 5.1
# from calculator import *

# print(al(0,5,3))
# print(al(sub,10,4))
# print(al(mult,6,2))
# print(al(divide,8,0))

# ? 5.2
# import math
# from datetime import datetime, timedelta
# 2
# x = datetime.datetime.now()
# print(x.strftime("%X"))

# 3
# x = datetime.datetime.now()
# print(x.strftime("%Y"))

# 4
# a = 2000
# x = datetime.datetime.now()
# y = int(x.strftime("%Y"))
# print(y - a)

# 5
# x = datetime.datetime.now()
# y = int(x.strftime("%j"))
# print(365 - y)

# 6
# x = datetime.datetime.now()
# print(x.strftime("%A"))

# 7
# x = datetime.now()
# ten = timedelta(days=10)
# f = x + ten
# print(x)
# print(f)

# 8
# date1 = datetime(2026, 3, 25)
# date2 = datetime(2026, 3, 30)

# diff = date2 - date1
# print(diff)

# 9
# now = datetime.now()
# custom_format = now.strftime("%d/%m/%Y %H:%M")

# print(f"9. Formatted time: {custom_format}")

# 10
# now = datetime.now()
# day_num = now.weekday()
# is_weekend = day_num == 5 or day_num == 6

# print(f"10. Is it weekend? {is_weekend}")

# 11
# x = math.sqrt(16)
# print(x)

# 12
# x = pow(2, 3)
# print(x)

# 13,14
# x = math.ceil(4.2)
# y = math.floor(4.8)
# print(x)
# print(y)

# 15
# num = -10
# x = abs(num)
# print(x)

# 16,17

# x = math.pi
# b = pow(10,2)
# s = x * b
# print(s)

# 18
# num1 = 10
# num2 = 3
# distance = abs(num1 - num2)
# print(distance)

# 19
# numbers = [4, 8, 6, 10]
# average = sum(numbers) / len(numbers)
# print(average)

# 20

# now = datetime.now()
# hours_passed = now.hour + (now.minute / 60)
# result = math.floor(hours_passed * 2)
# print(f"20. Current hour: {now.hour}:{now.minute}")
# print(f"20. Result (Hours * 2, floored): {result}")

# ? 4.3
import os
import sys

# 1
# x = os.name
# print(x)

# 2
# print( os.getcwd())

# 3
# print(os.listdir())

# 4
# folder_name = "test_folder"
# if not os.path.exists(folder_name):
#     os.mkdir(folder_name)
#     print("4. Folder created")

# # 5
# os.chdir(folder_name)
# print(f"5. Changed directory to: {os.getcwd()}")

# 6
# def final_scenario():
#     target = "scenario_folder"
#     filename = "log.txt"
    
#     # 1. צור תיקייה
#     if not os.path.exists(target):
#         os.mkdir(target)
#         print("Folder created")
    
#     # 2. צור קובץ בתוכה
#     file_path = os.path.join(target, filename)
#     with open(file_path, 'w') as f:
#         f.write("Log data")
#     print("File created")
    
#     # 3. בדוק קיום
#     print(os.path.exists(file_path))
    
#     # 4. מחיקה (ניקוי)
#     os.remove(file_path)
#     os.rmdir(target)
#     print("Cleanup done")

# final_scenario()

# ? 4.3

