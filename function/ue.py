# a =  input("Enter Your Numbers") 
# b = a.split()
# my_tupple = []
# for i in range (len(b)):
#     c = (int(b[i]))
#     my_tupple.append(c)
    
# new_tupple = tuple(my_tupple) 
# def pok(new_tupple):
#     result = sum(new_tupple)
#     count = len(new_tupple)
#     avrage =  result / count
    
#     print(f"the result: {result} \nthe count: {count} \nthe avrage {avrage}")  
    
# pok(new_tupple) 


# a = input("Enter Your Numbers ")
# b = a.split()
# my_tupple = []
# for i in range (len(b)): 
#     c = (int(b[i]))
#     my_tupple.append(c)
    
# def kk():
#     low = min(my_tupple)
#     high = max(my_tupple)
#     print(f"hige {high} \nlow {low}")
# # kk()    

# def bb():
#     new_lisr = [n for n in my_tupple if n % 2 == 0]
#     print(new_lisr)
#     gg = sorted(my_tupple)
#     print(gg)  
# bb()

# def hh(x):
#      if x % 2 == 0:
#          print("even")
#      else:
#         print("odd")         
# hh(13)   

# def filter_passing_grades(grades):
#     passing = [grade for grade in grades if grade > 60]
#     return passing 
# my_grades = [45, 67, 88, 55, 92, 100]
# result = filter_passing_grades(my_grades)
# print(f"your pass grade: {result}")
# list = [2,5,7,4,42]
# def non():
#     if  not list :
#         print("none")
#     else:
#           result = sum(list)
#           count = len(list)
#           avrage =  result / count
#           print(avrage)
# non()          

# list = [21,4,5,32,875]

# def yt(x = 10):
#     for x in x:
#       if x >= 10:
#           print(x)
# yt(list)

# def kok(*args):
#     x = max(args)
#     print(x)
# kok(43,5,23,78,111,789)    

# def bob(*args):    
#      for args in args:
#       if args % 2 == 0:
#        print(args)
# bob(32,7,9,2)     

# def nike(name,age):
#     print(f"hello {name} your {age} old")
# nike("eli",25)    

# def bz(*args):
#     m = min(args)
#     h = max(args)
#     s = sum(args)
#     print(f"low {m} \n high {h} \n sum {s}")
    
# bz(23,7,4,98,32)    

# def cor():
#        def kor(*args):
#            s = sum(args)
#            print(s) 
#        kor(23,55)   

# cor()        

# x = "dvid"

# def tony():
#     print(x)
# tony()        

# g = "liel"
# def bb():
#     eli = "sabba"
#     def hh():
#         nonlocal eli 
#         print(eli + "kk")
#     hh()    
# bb()        

# 1. הגדרת הפונקציה מהתרגיל (ה"מנוע")
# def apply_to_list(my_list, func):
#     # כאן אנחנו יוצרים רשימה חדשה ומפעילים את func על כל איבר
#     result_list = []
#     for item in my_list:
#         new_value = func(item)
#         result_list.append(new_value)
#     return result_list

# # 2. הגדרת פונקציית עזר (ה"פעולה" שנרצה לעשות)
# def double(n):
#     return n * 2

# # 3. יצירת הנתונים
# numbers = [1, 2, 3, 4, 5]

# # 4. הקריאה לפונקציה - כאן קורה הקסם!
# # שים לב: אנחנו שולחים את double בלי סוגריים!
# final_result = apply_to_list(numbers, double)

# # 5. הדפסה למסך (בלי זה לא תראה כלום)
# print("original list",numbers)
# print("new list:", final_result)

# def do(x=1):
#     n = x * 2
#     print(n) 

# # do()

# def jj(x,a):
#      a(x)
# jj(10,do)     

# def eli(num_list,t,r):
#     num = []
#     for x in  num_list:
#         if x > t:
#             num.append(x)
#     #         
#     if r == True:
#         num = num[::-1]  
#     return num        
# a = eli([54,76,21,12,87],20,True)  
# print(a)      

# def tal(*args):
#    a = sum(args)
#    b = max(args)
#    c = min(args)   
#    return(a,b,c)

# m = tal(5,3,6)
# print(m) 

def zogi(num_list):
    ez = []
    zogi_list =[]
    for n in num_list:
     if n % 2 == 0:
         zogi_list.append(n)
     else:       
         ez.append(n)
    return zogi_list,ez     
res = zogi([54,86,71,23,44,8])
print(res)