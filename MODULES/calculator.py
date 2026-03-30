# Some Calc Operations
# def add(x, y):
#     return x + y

# def sub(x, y):
#     return x - y

# def mult(x, y):
#     return x * y

# def divide(x, y):
#     return x / y

# [Python Basics] Hands-On Lab 5.1
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def divide(x, y):
    if x  == 0:
        print("Error: Cannot divide by zero")
    elif y == 0:
        print("Error: Cannot divide by zero")
    else:  
     return x / y
    
def holding(x,y):
 return x ** y





def al(x,y,z):
     if callable(x):
        return x(y, z)
     else:
         print("Error: Unsupported operationr")
   