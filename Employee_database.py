#print hello
#import file
def convertFileToDictionary(file_pathway): #https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
  data = {}
  with open(file_pathway) as f:
    for line in f:
      line = line.strip()
      emp = line.split(',')
      key = emp[0]
      value = emp[1:]
      value[1] = int(value[1])
      value[3] = int(value[3])
      data[key] = value
  return data

# Initialize the data dictionary using the convertFileToDictionary function
file_pathway = "Employee draft.txt"  
data = convertFileToDictionary(file_pathway)

#login data
def check_role(username, password):
  # max_attempts = 5
  
  if username == "admin" and password == "admin123123":
    return "admin"
  elif username != "admin" and password == "":
    return "employee"
  return "invalid"

#add new employee
def add_new_employee(data, username, id, gender, salary):
    employee_id = list(data.keys())
    
    if employee_id:  # Check if the list is not empty
        last_employee_id = employee_id[-1]
        number = int(last_employee_id[7:])
    else:
        number = 1  # If no employee IDs are available, start from 1
    
    number += 1
    new_employee_id = f"employee{number}"
    data[new_employee_id] = [username, id, gender, salary]
    
    return data


#admin menu
def display_admin_menu():
  print( "welcome Mr.admin!Choose one of these options to go forward.\n1. Display Inventory Statistics\n 2. Add Product to Inventory\n 3. Display All Products in Inventory (sorted by product ID)\n 4. Update Product Price\n 5. Update Product Quantity\n 6. Remove Product from Inventory\n 7. Search Product by Name\n 8. Sort Products by Quantity (descending)\n 9. Exit")

print("Welcome Mr.admin/Mr.employee,//Please login")

attempts = 0
#print(data)
while True:
  if attempts < 5:
    username = input(str("Enter username: "))
    password = input("Enter password: ")
    role = check_role(username, password)
    if role == "admin":
      while True:
        display_admin_menu()

        choice = int(input("Enter choice number: "))
        
        if choice == 2:

          username = input(str("Enter username: "))
          id = input(str("Enter id: "))
          gender = str(input(str("Enter gender: ")))
          salary= int(input(str("Enter salary: ")))
          data = add_new_employee(data, username, id, gender, salary)
          print("New product added succesfully.")
    
          
        elif choice == 4:
          pass
        elif choice == 5:
          pass
        elif choice == 6:
          pass
        elif choice == 7:
          pass
        elif choice == 8:
          pass
        elif choice == 9:
          print("Exiting the program")
          break  # Exit the loop and end the program when user selects choice 9
      else:
        print("Invalid choice, please try again!")
    elif role == "employee":
      pass
    else:
      print("Incorrect username and/or password, please try again!")
      attempts += 1
  else:
    print("you reached attempts limit!Try again later!")
    exit()