from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
root.title("Student Marks Management System")
root.geometry("700x500")
root['bg'] = "#eaf6ff"
root.resizable(False, False)

FILENAME = "studentMarks.txt"

def grade_from_percentage(pct):
    if pct >= 70:
        return "A"
    if pct >= 60:
        return "B"
    if pct >= 50:
        return "C"
    if pct >= 40:
        return "D"
    return "F"

def parse_line(line):
    parts = [p.strip() for p in line.split(",")]
    if len(parts) < 6:
        return None
    try:
        num = parts[0]
        name = parts[1]
        coursework = list(map(int, parts[2:5]))
        exam = int(parts[5])
    except ValueError:
        return None
    cw_total = sum(coursework)
    total_score = cw_total + exam
    pct = (total_score / 160) * 100
    return {
        "number": num,
        "name": name,
        "coursework_total": cw_total,
        "exam_mark": exam,
        "percentage": pct,
        "grade": grade_from_percentage(pct)
    }

def load_data():
    students = []
    try:
        with open(FILENAME, "r") as f:
            try:
                expected = int(f.readline().strip())
            except ValueError:
                expected = None
            for line in f:
                student = parse_line(line.strip())
                if student:
                    students.append(student)
            if expected is not None and expected != len(students):
                messagebox.showwarning("Warning", f"Expected {expected} students but found {len(students)}.")
    except FileNotFoundError:
        messagebox.showerror("Error", f"File not found: {FILENAME}\nMake sure it is in the same folder as this script.")
    return students

def format_student(s):
    return (
        f"Name: {s['name']}\n"
        f"Student Number: {s['number']}\n"
        f"Total Coursework Mark: {s['coursework_total']}\n"
        f"Exam Mark: {s['exam_mark']}\n"
        f"Overall Percentage: {s['percentage']:.2f}%\n"
        f"Grade: {s['grade']}"
    )

def view_all():
    output_text.delete(1.0, END)
    if not students:
        output_text.insert(END, "No data available.")
        return
    total = 0
    for s in students:
        output_text.insert(END, format_student(s) + "\n" + "-"*40 + "\n")
        total += s["percentage"]
    avg = total / len(students)
    output_text.insert(END, f"\nNumber of Students: {len(students)}\nAverage Percentage: {avg:.2f}%")

def view_individual():
    name = student_select.get()
    if not name or name == "Select Student":
        messagebox.showinfo("Info", "Select a student from the dropdown.")
        return
    output_text.delete(1.0, END)
    student = next((s for s in students if s["name"] == name), None)
    output_text.insert(END, format_student(student) if student else "Student not found.")

def show_highest():
    output_text.delete(1.0, END)
    if not students:
        output_text.insert(END, "No data available.")
        return
    best = max(students, key=lambda s: s["percentage"])
    output_text.insert(END, "Student with Highest Score:\n\n" + format_student(best))

def show_lowest():
    output_text.delete(1.0, END)
    if not students:
        output_text.insert(END, "No data available.")
        return
    worst = min(students, key=lambda s: s["percentage"])
    output_text.insert(END, "Student with Lowest Score:\n\n" + format_student(worst))

def exit_app():
    root.destroy()

students = load_data()

title_label = Label(root, text="Student Marks Management System", font=("Arial", 18, "bold"), bg="#eaf6ff")
title_label.pack(pady=6)

main_frame = Frame(root, bg='#eaf6ff')
main_frame.pack(fill=BOTH, expand=True, padx=8, pady=6)

left_frame = Frame(main_frame, bg='#eaf6ff')
left_frame.pack(side=LEFT, fill=Y, padx=(0,10), pady=5)

button_frame = ttk.Frame(left_frame)
button_frame.pack(pady=5, anchor="n")

ttk.Button(button_frame, text="View All", command=view_all).grid(row=0, column=0, padx=5, pady=5, sticky="w")
ttk.Button(button_frame, text="View Individual", command=view_individual).grid(row=1, column=0, padx=5, pady=5, sticky="w")
ttk.Button(button_frame, text="Highest Score", command=show_highest).grid(row=2, column=0, padx=5, pady=5, sticky="w")
ttk.Button(button_frame, text="Lowest Score", command=show_lowest).grid(row=3, column=0, padx=5, pady=5, sticky="w")
ttk.Button(button_frame, text="Exit", command=exit_app).grid(row=4, column=0, padx=5, pady=5, sticky="w")

student_select = ttk.Combobox(left_frame, values=[s["name"] for s in students], state="readonly", width=28)
student_select.pack(pady=12)
student_select.set("Select Student")

right_frame = Frame(main_frame, bg='#eaf6ff')
right_frame.pack(side=RIGHT, fill=BOTH, expand=True)

output_text = Text(right_frame, wrap="word", width=60, height=20)
output_text.pack(fill=BOTH, expand=True, padx=4, pady=4)

root.mainloop()