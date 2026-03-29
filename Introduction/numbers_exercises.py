import math

# --- Part 2: Integer vs Float ---

# Exercise 1
print(type(1))          # <class 'int'>

# Exercise 2
print(type(1.0))        # <class 'float'>

# Exercise 3
print(type(10))         # <class 'int'>
print(type(10.0))       # <class 'float'>

# --- Part 3: Precision Issues ---

# Exercise 4 & 5
print("When comparing floats directly, we may run into precision issues")
comparison = (0.1 * 3 == 0.3)
print(f"0.1 * 3 == 0.3: {comparison}") # False

# --- Part 4: Using math.isclose ---

# Exercise 6 & 7
# (הייבוא של math מופיע בתחילת הקובץ)
print(math.isclose(0.1 * 3, 0.3))      # True

# --- Part 5: Arithmetic Operators (True Division) ---

# Exercise 8
print(7 / 2)            # 3.5

# Exercise 9
print(8 / 2)            # 4.0 (שים לב שחלוקה רגילה תמיד מחזירה float)

# Exercise 10
print(type(8 / 2))      # <class 'float'>

# --- Part 6: Floor Division (//) ---

# Exercise 11
print(8 // 2)           # 4

# Exercise 12
print(5 // 3)           # 1

# Exercise 13
print(5 // 3.0)         # 1.0 (אם אחד הצדדים הוא float, התוצאה תהיה float)

# --- Part 7: Modulo (%) ---

# Exercise 14
print(5 % 3)            # 2

# Exercise 15
print(5 % 3)            # 2
print(6 % 3)            # 0
print(7 % 3)            # 1
print(8 % 3)            # 2
print(9 % 3)            # 0
print(10 % 3)           # 1