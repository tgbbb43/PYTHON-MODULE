import tkinter as tk

root = tk.Tk()
# Widgets are added here
root.title("My DevOps Tool")
root.geometry("400x300")
# יצירת תווית
label = tk.Label(root, text="Welcome, Eli!", font=("Arial", 14))
# מיקום הרכיב בחלון עם קצת מרווח (padding)
label.pack(pady=20)
def on_button_click():
    # חלק 7: עדכון ה-Label בצורה דינמית
    label.config(text="Button Clicked!", fg="blue")

# יצירת כפתור וחיבורו לפונקציה
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

import tkinter as tk

def process_input():
    # חלק 8: קבלת הערך מהשדה
    user_text = entry.get()
    
    # חלק 11: אימות (Validation) - אם השדה ריק
    if user_text.strip() == "":
        label.config(text="Please enter something!", fg="red")
    else:
        # חלק 9: הצגת הפלט
        label.config(text=f"Hello, {user_text}!", fg="green")

# הגדרות חלון (חלק 1-2)
root = tk.Tk()
root.title("DevOps Input App")
root.geometry("400x250")

# תווית הנחיה
instruction = tk.Label(root, text="Enter your name:")
instruction.pack(pady=5)

# שדה קלט (חלק 8)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# כפתור הפעלה (חלק 5-6)
submit_btn = tk.Button(root, text="Submit", command=process_input, bg="lightgrey")
submit_btn.pack(pady=10)

# תווית פלט דינמית (חלק 3+7)
label = tk.Label(root, text="Waiting for input...", font=("Arial", 12))
label.pack(pady=20)

# חלק 10: שיפור UX - הוספת כפתור יציאה
exit_btn = tk.Button(root, text="Exit", command=root.destroy, fg="white", bg="darkred")
exit_btn.pack(side="bottom", pady=10)



root.mainloop()