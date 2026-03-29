# print("Welcome to Python!")

# print( "Python", "is", "fun" ,sep="" )
# print("Eli", ",", "Haimov", sep="")

# print("Loading" , " ...Done!", end="" )
# print("Loading", end="")  # מה צריך לשים בתוך הגרשיים כדי שלא יהיה רווח או ירידת שורה?
# print("... Done!")

# print("Name", "Eli", sep=": ")

# print(1, 2, 3, sep=" | ", end=".\n")

# 1. הדפסת שורת סטטוס עם רווח כמפריד
# אנחנו מדפיסים שתי מחרוזות נפרדות וקובעים שהמפריד ביניהן הוא רווח
print("[STATUS]", "System ready.", sep=" ")

# 2. הדפסת שורת זמן עם נקודתיים ורווח כמפריד
# שים לב איך ה-sep חוסך לנו כתיבה ידנית של ": " בתוך המחרוזת
print("Time", "14:30",  sep=":")

# 3. הדפסת הודעת סיום
# כאן בחרנו להדפיס אותה כרגיל בשורה חדשה
print("End of report.")