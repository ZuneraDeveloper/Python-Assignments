import csv  # import from library

with open("students.csv", "w", newline="") as file: # we opened a file with the name of "student.csv" w means write any thing in file and we suppose this file name temprary "file"
    writer = csv.writer(file)  # here we assign variable to write in our cvs file
    writer.writerow(["name", "marks"]) # here we add a header row in our cvs

def add_student():  # first function that stores student data in our cvs file
  try:
    name = input("Enter your name:")
    marks = int(input("Enter your marks here:"))
    with open("students.csv","a", newline="") as file:
      writer = csv.writer(file)
      writer.writerow([name, marks])
  except ValueError:
    print("Invalid input!")

# add_student()

def view_student():  # second function for viewing the data which is stored in that cvs file
  try:
    with open("students.csv", "r", newline = "") as file:  #here "r" purpose is to get data from our cvs file
      reader = csv.reader(file) # here we assign a vraible which is == to cvs.reader(file) means it will get data from our cvsfile
      for row in reader:
        print(row)
  except FileNotFoundError:
    print("File not found.")

# view_student()

def calculator_grade(marks):   # giving grade according to marks of students who are in our cvs file
  if marks >= 90:
    print("Grade: A")
  elif marks >= 80:
    print("Grade: B")
  elif marks >= 70:
    print("Grade: C")
  elif marks >= 60:
    print("Grade: D")
  else:
    print("Grade: F")



def search_student():  # thsi function is used for student data from our cvs file
  search = input("Enter your name to search:")
  try:
    with open("students.csv", "r", newline = "") as file:
      reader = csv.reader(file)
      for row in reader:
        if search in row[0]:
          print("Name:",row[0])
          try:
            marks = int(row[1])
            print("Marks:", row[1])
            calculator_grade(marks)
          except ValueError:
            print("Invalid input!")
  except FileNotFoundError:
    print("file not found.")

# search_student()

menu = """ ========== STUDENT GRADEBOOK ==========

1. Add Student
2. View Students
3. Search Student
4. Exit"""

choice = 0
while choice != 4:  # user friendly menu funciton that will run according to user
  print(menu)
  choice = int(input("Enter your Choice:"))
  if choice == 1:
    add_student()
  elif choice == 2:
    view_student()
  elif choice == 3:
    search_student()
  elif choice == 4:
    print("Exit!")
  else:
    print("Invalid option!!")