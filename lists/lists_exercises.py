# servers = ["web01", "web02", "web03"]
# print(servers[-1])

servers = ["web01", "web02", "web03","web04","web05"]
# print(servers[::2])
mixed_list = ["DevOps", 2026, True]
print(mixed_list)

# 1. הגדרת הרשימה המקורית
original_list = ["web01", "web02", "web03"]

# 2. ביצוע Slicing (לקיחת שני האיברים הראשונים)
# הפעולה הזו יוצרת רשימה חדשה בזיכרון
new_list = original_list[0:2]

# 3. הדפסת הרשימה החדשה
print("New list:", new_list)

# 4. הדפסת הרשימה המקורית - היא נשארה בדיוק אותו דבר!
print("Original list:", original_list)