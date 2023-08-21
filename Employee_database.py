#import file
def convertFileToDictionary(file_pathway):#https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
  data = {} #https://docs.python.org/3/reference/simple_stmts.html#the-global-statement
  with open(file_pathway) as f:
    for line in f:
      line = line.strip()
      items = line.split(',')
      key = items[0]
      value = items[1:]
      value[1] = int(value[1])
      value[2] = value[2].lower() # make sure m or f is alwayss in lower
      value[3] = float(value[3])
      data[key] = value
      # print(data)
  return data
 
#login data
def check_role(username, password):
  # max_attempts = 5
  
  if username == "admin" and password == "admin123123":
    return "admin"
  elif username in data and password == "":
    return "user"
  return "Incorrect Username and/or Password"

#admin menu
def display_admin_menu():
  print( "welcome Mr.admin!Choose one of these options to go forward.\n 1. Display Statistics\n 2. Add an Employee\n 3. Display all Employees \n 4. Change Employee’s Salary\n 5. Remove Employee\n 6. Raise Employee’s Salary\n 7. Exit")

#display statistics
def display_statistics(data):
  male = 0
  female = 0
  for key,value in data.items():
    if value[2] == "male":
      male += 1
    elif value[2] == "female":
      female += 1
      
  print('Male :' + str(male))
  print('Female :' + str(female))

#add new employee
def add_new_employee(data, username, id, gender, salary):
  employee_serial = list(data.keys())
  last_employee_id = employee_serial[-1]
  number = int(last_employee_id[3:])
  number = number + 1
  key='emp'+str(number).zfill(3) #(https://docs.python.org/3/library/stdtypes.html#str.zfill)
  id = [value[1] for value in data.values()]
  last_id_number = id[-1]
  auto_id = int(last_id_number)
  auto_id = auto_id + 1
  data[key] = [username, auto_id, gender, salary]
  return data

#Display all Employee sorted (https://docs.python.org/3/howto/sorting.html)
def display_all_employee(data):
  my_keys = list(data.keys())
  my_keys.sort()
  sorted_dict = {i:data[i] for i in my_keys} 
  for key,value in sorted_dict.items():
    print(key,value)
    
#Check id existance
def check_id_existance(data, id):
  for key, value in data.items():
    if value[1] == id:
      return key
  return False    
  
#Change Employee’s Salary
def change_employee_salary(data, key,salary):
  
  data[key][3] = salary
  print("salary changed succesfully")
  return data  


  
#Remove Employee
def remove_employee(data, key):
  del data[key] #(https://docs.python.org/3/reference/simple_stmts.html#the-del-statement)
  print("Employee removed succesfully")
  return data
#Raise Employee’s Salary
def raise_employee_salary(data, key , percentage):
  salary = data[key][3]
  salary = salary + (salary * percentage)/100
  data[key][3] = salary
  print("Salary raised succesfully")
  return data
#save and exit
def save_to_file(file_pathway, data):
  with open(file_pathway, 'w') as f: #https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
    for key, value in data.items():
      line = ','.join([key] + value)
      file_pathway.write(line + "\n")
  exit() #https://docs.python.org/3/library/functions.html#exit 


#user menu
def display_user_menu():
   print("1.salary\n 2. Exit")

#------------End of Functions-------------
# if __name__ == 'main':
data = convertFileToDictionary("employee_database.txt")

print("Welcome Mr.admin/Mr./Mrs.User,//Please login")

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
        if choice == 1:
          display_statistics(data)
        elif choice == 2:

          username = input(str("Enter username: "))
          valid_genders = "male" or "female"
          while True:
            gender = input(str("Enter gender male/female: "))
            if gender == valid_genders:
              break
            else:
              print("invalid gender.Please enter male or female")
          salary = int(input(str("Enter salary: ")))
          # print(username,id,gender,salary)
          data = add_new_employee(data, username, id, gender, salary)
          print("New employee added succesfully.")
    
        elif choice == 3:
          display_all_employee(data)
        elif choice == 4:
          id = int(input(str("Enter id: ")))
          key = check_id_existance(data, id)
          if key != False:
            
            salary = float(input(str("Enter updated salary: ")))
            data = change_employee_salary(data, key,salary)
          else:
            print("id not found, try again later!")
        elif choice == 5:
          id = int(input(str("Enter id: ")))
          key = check_id_existance(data, id)
          if key != False:
            
            data = remove_employee(data, key)
          else:
            print("id not found, try again later!")
        elif choice == 6:
          id = int(input(str("Enter id: ")))
          key = check_id_existance(data, id)
          if key != False:
            
            percentage = float(input(str("Enter raise percentage: ")))
            data = raise_employee_salary(data, key , percentage)
          else:
            print("id not found, try again later!")
          
        elif choice == 7: 
          print("Exiting the program")