class stu_management:
  def __init__(self):
    self.users = []
  def add_stu(self):
    name = input("Enter your name:")
    age = int(input("Enter your age:"))
    stu_id = int(input("Enter your ID:"))
    course = input("Enter your course:")
    self.users.append({"name":name,"age":age,"id":stu_id,"course":course})

  def update_stu(self):
    search = int(input("Enter your ID no to search:"))
    for i in self.users:
      if search == i["id"]:
        print("Name:",i["name"])
        print("Age:",i["age"])
        print("ID:",i["id"])
        print("Course:",i["course"])
        update_name = input("Enter your name:")
        update_age = int(input("Enter your age:"))
        update_course = input("Enter your course:")
        i["name"] = update_name
        i["age"] = update_age
        i["course"] = update_course
        print("Information is updated!")
        return
    print("No")
  
  def view(self):
    for i in self.users:
      print("Name:",i["name"])
      print("Age:",i["age"])
      print("ID:",i["id"])
      print("Course:",i["course"])


class Menu(stu_management):
  def view(self):
    for i in self.users:
      print("Registered Students")
      print("Name:",i["name"])
      print("Age:",i["age"])
      print("ID:",i["id"])
      print("Course:",i["course"])
        
  def menu(self):
    choice = 0
    while choice != 4:
    
      print("""*************Studnet Management System*****************
      
      1. Add Student
      
      2. Update Student Information
      
      3. view Student Data
      
      4. Exit""")
      
      choice = int(input("Enter your choice:"))
      
      if choice == 1:
          
          self.add_stu()

      
      elif choice == 2:
          
          self.update_stu()

      
      elif choice == 3:
          
        self.view()

      
      elif choice == 4:
          
          print("Exit!!")

      
      else:
          
          print("You entered invalid number.")

system = Menu()

system.menu()
