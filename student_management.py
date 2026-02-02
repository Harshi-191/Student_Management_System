import csv
import os

FILE_NAME = "students.csv"

# ---------- Utility Functions ----------

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "Fail"


def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Marks1", "Marks2", "Marks3", "Total", "Average", "Grade"])


# ---------- Core Features ----------

def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    m1 = int(input("Enter Marks for Subject 1: "))
    m2 = int(input("Enter Marks for Subject 2: "))
    m3 = int(input("Enter Marks for Subject 3: "))

    total = m1 + m2 + m3
    avg = total / 3
    grade = calculate_grade(avg)

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([sid, name, m1, m2, m3, total, avg, grade])

    print("✅ Student added successfully!\n")


def view_students():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print("{:<5} {:<10} {:<7} {:<7} {:<7} {:<7} {:<8} {:<5}".format(*row))
    print()


def search_student():
    sid = input("Enter Student ID to search: ")
    found = False

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == sid:
                print("Student Found:", row)
                found = True
                break

    if not found:
        print("❌ Student not found.\n")


def update_student():
    sid = input("Enter Student ID to update: ")
    rows = []
    updated = False

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)
        rows.append(header)

        for row in reader:
            if row[0] == sid:
                print("Enter new marks:")
                m1 = int(input("Subject 1: "))
                m2 = int(input("Subject 2: "))
                m3 = int(input("Subject 3: "))

                total = m1 + m2 + m3
                avg = total / 3
                grade = calculate_grade(avg)

                row = [sid, row[1], m1, m2, m3, total, avg, grade]
                updated = True

            rows.append(row)

    if updated:
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("✅ Student updated successfully!\n")
    else:
        print("❌ Student not found.\n")


def delete_student():
    sid = input("Enter Student ID to delete: ")
    rows = []
    deleted = False

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)
        rows.append(header)

        for row in reader:
            if row[0] != sid:
                rows.append(row)
            else:
                deleted = True

    if deleted:
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("🗑 Student deleted successfully!\n")
    else:
        print("❌ Student not found.\n")


# ---------- Menu ----------

def menu():
    initialize_file()

    while True:
        print("====== Student Management System ======")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student Marks")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


# Run the program
menu()