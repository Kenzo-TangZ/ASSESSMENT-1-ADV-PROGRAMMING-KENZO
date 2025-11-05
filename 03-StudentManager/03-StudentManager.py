import tkinter as tk
from tkinter import ttk, messagebox
import os

def load_data():
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, "studentMarks.txt")

    students = []
    try:
        with open(file_path, "r") as f:
            num_students = int(f.readline().strip())
            for line in f:
                parts = [p.strip() for p in line.strip().split(",")]
                if len(parts) < 6:
                    continue
                student_number = parts[0]
                student_name = parts[1]
                coursework_marks = list(map(int, parts[2:5]))
                exam_mark = int(parts[5])
                total_coursework = sum(coursework_marks)
                total_score = total_coursework + exam_mark
                percentage = (total_score / 160) * 100
                if percentage >= 70:
                    grade = "A"
                elif percentage >= 60:
                    grade = "B"
                elif percentage >= 50:
                    grade = "C"
                elif percentage >= 40:
                    grade = "D"
                else:
                    grade = "F"
                students.append({
                    "number": student_number,
                    "name": student_name,
                    "coursework_total": total_coursework,
                    "exam_mark": exam_mark,
                    "percentage": percentage,
                    "grade": grade
                })
            if len(students) != num_students:
                messagebox.showwarning("Warning", f"Expected {num_students} students but found {len(students)}.")
    except FileNotFoundError:
        messagebox.showerror("Error", f"File not found.\nExpected path:\n{file_path}")
    return students

def display_student(student):
    return (f"Name: {student['name']}\n"
            f"Student Number: {student['number']}\n"
            f"Total Coursework Mark: {student['coursework_total']}\n"
            f"Exam Mark: {student['exam_mark']}\n"
            f"Overall Percentage: {student['percentage']:.2f}%\n"
            f"Grade: {student['grade']}")

def view_all():
    output_text.delete(1.0, tk.END)
    if not students:
        output_text.insert(tk.END, "No data available.")
        return
    total_percentage = 0
    for s in students:
        output_text.insert(tk.END, display_student(s) + "\n" + "-"*40 + "\n")
        total_percentage += s["percentage"]
    avg = total_percentage / len(students)
    output_text.insert(tk.END, f"\nNumber of Students: {len(students)}\nAverage Percentage: {avg:.2f}%")

def view_individual():
    selection = student_select.get()
    if not selection:
        messagebox.showinfo("Info", "Select a student from the dropdown.")
        return
    student = next((s for s in students if s["name"] == selection), None)
    output_text.delete(1.0, tk.END)
    if student:
        output_text.insert(tk.END, display_student(student))
    else:
        output_text.insert(tk.END, "Student not found.")

def show_highest():
    output_text.delete(1.0, tk.END)
    if not students:
        output_text.insert(tk.END, "No data available.")
        return
    top = max(students, key=lambda s: s["percentage"])
    output_text.insert(tk.END, "Student with Highest Score:\n\n" + display_student(top))

def show_lowest():
    output_text.delete(1.0, tk.END)
    if not students:
        output_text.insert(tk.END, "No data available.")
        return
    low = min(students, key=lambda s: s["percentage"])
    output_text.insert(tk.END, "Student with Lowest Score:\n\n" + display_student(low))

def exit_app():
    root.destroy()

students = load_data()

root = tk.Tk()
root.title("Student Marks Management System")
root.geometry("700x500")

title_label = ttk.Label(root, text="Student Marks Management System", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

button_frame = ttk.Frame(root)
button_frame.pack(pady=5)

ttk.Button(button_frame, text="View All", command=view_all).grid(row=0, column=0, padx=5, pady=5)
ttk.Button(button_frame, text="View Individual", command=view_individual).grid(row=0, column=1, padx=5, pady=5)
ttk.Button(button_frame, text="Highest Score", command=show_highest).grid(row=0, column=2, padx=5, pady=5)
ttk.Button(button_frame, text="Lowest Score", command=show_lowest).grid(row=0, column=3, padx=5, pady=5)
ttk.Button(button_frame, text="Exit", command=exit_app).grid(row=0, column=4, padx=5, pady=5)

student_select = ttk.Combobox(root, values=[s["name"] for s in students], state="readonly", width=30)
student_select.pack(pady=10)
student_select.set("Select Student")

output_text = tk.Text(root, wrap="word", width=80, height=20)
output_text.pack(padx=10, pady=10)

root.mainloop()