#import file
def convertFileToDictionary(file_pathway):#https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
  data = {}
  with open(file_pathway) as f:
    for line in f:
      line = line.strip()
      items = line.split(',')
      key = items[0]
      value = items[1:]
      value[1] = int(value[1])
      value[2] = value[2].lower() # make sure m or f is alwayss in lower
      value[3] = int(value[3])
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
def change_employee_salary(data,id,salary):
  data[id] = [id,salary]
  print("salary change succesful")
  return data  
