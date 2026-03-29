# Exercise 1 & 2: שגיאות צפויות (TypeError)
# set([[1, 2], [3, 4]]) -> שגיאה: List היא Mutable
# {{1, 2}, {3, 4}} -> שגיאה: Set היא Mutable

# Exercise 3: Set של Tuples
set_of_tuples = {(1, 2), (3, 4)}

# Exercise 4: Membership
print(f"Is (1, 2) in set? {(1, 2) in set_of_tuples}")
print(f"Is (1, 3) in set? {(1, 3) in set_of_tuples}")

# Exercise 5: יצירת קבוצות
developers = {"Alice", "Bob", "Charlie"}
admins = {"Alice", "David"}

# Exercise 6: Membership
print(f"Is Alice a dev and admin? {'Alice' in developers and 'Alice' in admins}")

# Exercise 7 & 8: Union
print(f"Union (method): {developers.union(admins)}")
print(f"Union (operator): {developers | admins}")

# Exercise 9 & 10: Intersection
print(f"Intersection (method): {developers.intersection(admins)}")
print(f"Intersection (operator): {developers & admins}")

# Exercise 11 & 12: Difference
print(f"Difference (method): {developers.difference(admins)}")
print(f"Difference (operator): {developers - admins}")

# Exercise 13 & 14: Update vs Return
developers.intersection_update(admins)
print(f"Developers after intersection_update: {developers}")
