# while loops basics
# user_input = input("Would you like to paly? (n/y)")

# user_input = "y"
# while user_input != "n":
#     print("Game is Running...")
    # user_input = input("Would you like to play again (n/y)")
    
    
# while True:
#     user_input = input("Would you like to paly? (n/y)")
    
#     if user_input == "n":
#         break
#     print("Game is runing")

#?  [Python Basics] Hands-On Lab 4.0
# 1
# i = 1
# while i <= 5:
#     print(i)
#     i += 1
    # 
# 2 

# i = 5
# while i >= 1:
#     print(i)
#     i -= 1
 
# 3 

# i = 2
# while i <= 10:
#     print(i)
#     i += 2   

# 4 

# i = 1
# total = 0
# while i <= 5:
#     total += i
#     i += 1
# print("Sum:", total)

# 5

# i = 3
# while i <= 10:
#     print(i)
#     i += 3

# 6

# user_in = input("enter a number ")

# i = 1
# while i <= 5:
#      print(user_in)
#      i += 1
     
# 7 
# user_in = int(input("enter a number "))
# i = 1
# while i <= user_in:
#     print(i)
#     i += 1

    
# 8
# user_num = input("enter num " )
# while user_num != "0":
#     user_num = input("enter num " )
#     print("try agin")

# 9
# user_num = input("enter password " )
# while user_num != "1234":
#    user_num = input("enter password " )
#    print("try agin")

# 10
# user_in = input("y or n " )
# while user_in != "n":
#     user_in = input("y or n " )
#     print("by")

# 11
n = 1
# while n <= 10:
#     n += 1
#     if n % 2 == 0:
#         print(n)
   
# 12
# b = 0
# n = 1
# while n <= 20:
#     n += 1
#     if n % 2 == 0:
#       b += 1
# print(b)

# 13
# n = 0
# b = 0

# while n <= 9:
#     n += 1
#     if n % 2 == 1:
#        b += n
# print(b)       

# 14
 
# while True:
#     n = int(input(" number? "))
#     if n % 2 == 0:
#         print("zogi")
#     else:
#         print("e zogi")       

# 15
# count = 0
# max_val = float('-inf')
# while count < 5:
#     num = int(input("Enter a number: "))
#     if num > max_val:
#         max_val = num
#     count += 1
# print(f"Max is: {max_val}")

# 16
# while True:
#    a = input("hii ")
#    if a == "exit":
#        break

# 17
# n = 1
# while n <= 10:
#     if n == 7:
#         break
#     print(n)
#     n += 1
# # 18
# sum_val = 0
# while True:
#     num = int(input("Enter a number to sum (negative to stop): "))
#     if num < 0:
#         break
#     sum_val += num
# print(f"Total: {sum_val}")
    
# 19
f = 2
# while True:
#    p = int(input("gess "))
#    if p == f:
#        break
#    else:
#        print("try agin")

# 20
inputs_count = 0
while True:
    user_in = input("Enter something (stop to end): ")
    if user_in == "stop":
        break
    inputs_count += 1
print(f"Total inputs: {inputs_count}")