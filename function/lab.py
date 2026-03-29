#? 3.4

# def process_data_guarded(data):
#     # Guard 1: Is it empty or None?
#     if data is None or (isinstance(data, (list, str)) and len(data) == 0):
#         print("no data provided")
#         return
    
#     # Guard 2: Is it the right type?
#     if not isinstance(data, list):
#         print(f"invalid value type for data provided {type(data)} required list")
#         return

#     # Success Path
#     print(f"processing {len(data)} items...")
#     print("processed")

# # בדיקות (תרגיל 14):
# process_data_guarded([])            # פלט: no data provided
# process_data_guarded([1, 2, 3])     # פלט: processing 3 items... processed
# process_data_guarded(None)          # פלט: no data provided
# process_data_guarded("ABC")         # פלט: invalid value type... <class 'str'>
# process_data_guarded(10)            # פלט: invalid value type... <class 'int'>

# #? 3.5
# print("start")
# def hello():
#     print("hello")
# hello()
# print("end")
   

# print("Welcome to the age in seconds program")

# def user_age_in_seconds():
#     user_age = int(input("age? "))
#     age_seconds = user_age * 365 * 24 * 60 * 60 
#     print(f"Your age in seconds is: {age_seconds}")

# user_age_in_seconds()

# print("Goodbye")

# תרגיל 14 ו-15: שימוש במשתנה גלובלי בצורה נכונה
# --- חלק 1: הגדרת פונקציה בסיסית ---
# def hello():
    # print("Hello")

# אם נריץ עכשיו, לא יודפס כלום כי רק הגדרנו את הפונקציה.

# --- חלק 2 ו-3: קריאה לפונקציה וסדר ריצה ---
# print("Start")      # הדפסה לפני
# hello()             # קריאה לפונקציה - תדפיס "Hello"
# print("End")        # הדפסה אחרי

# # --- חלק 4 ו-5: פונקציה עם לוגיקה (גיל בשניות) ---
# print("\n--- Age in Seconds Program ---")
# print("Welcome to the age in seconds program")

# def calculate_age_in_seconds():
#     user_age = int(input("Enter your age: "))
#     # חישוב: שנים -> ימים -> שעות -> דקות -> שניות
#     seconds = user_age * 365 * 24 * 60 * 60
#     print(f"Your age in seconds is: {seconds}")

# calculate_age_in_seconds()
# print("Goodbye")

# # --- חלק 6: דריסת פונקציות מובנות (להבנה בלבד - לא מומלץ להריץ) ---
# # אם נכתוב:
# # def print():
# #     pass
# # הקוד print("Hi") יזרוק TypeError כי דרסנו את הפונקציה המקורית.

# # --- חלק 7 ו-8: Scope ושגיאה (הסבר) ---
# friends = ["Rolf"]

# def add_friend_error():
#     # השורה הבאה תזרוק UnboundLocalError כי פייתון חושב ש-friends הוא משתנה מקומי
#     # friends = friends + ["Bob"] 
#     pass

# # --- חלק 10 ו-11: שימוש נכון במשתנה גלובלי (Mutation) ---
# def add_friend_correctly():
#     friends.append(input("name of yor frind")) # שימוש ב-.append() משנה את האובייקט הקיים ולא דורס את השם

# print("\n--- Global Scope Testing ---")
# add_friend_correctly()
# add_friend_correctly()
# add_friend_correctly()
# print(f"Friends list after 3 calls: {friends}")

# # --- חלק 9: קריאה לפני הגדרה (להבנה) ---
# # say_hello() # יזרוק NameError אם הפונקציה מוגדרת רק מתחת לשורה הזו
# def say_hello():
#     print("Hi there!")

#? 3.6
# def fan(x,y):
#      g = x + y
#      print(g)
# fan(9,7)     

# def name(a,b):
#     print(f"helio {a} {b}")
    
# name("eli","haimov")    

# def num(x,y):
#     if x&y == 0:
#         print("You fool")
#     else:   
#         g = x / y
#         print(f"it {g}") 
# num(y=1,x=5)    

#? 3.6.1 

# a = (input("Enter Your Numbers"))
# b = a.split()
# my_tupple = []
# for i in range (len(b)):
#     c = (int(b[i])) 
#     my_tupple.append(c)
         

# new_tupple = tuple(my_tupple)
# def expa(new_tupple):
#       result = sum(new_tupple)
#       count = len(new_tupple)
#       avrage = result/count
#       return result,count,avrage 

# answer = expa(new_tupple)
# print(f"Sum: {answer[0]}, Count: {answer[1]}, Average: {answer[2]}")

a =  int(input("Enter Your Numbers")) 
b = a.split()