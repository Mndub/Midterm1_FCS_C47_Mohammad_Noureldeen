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
      value[2] = value[2].lower() # make usre m or f is alwayss in lower
      value[3] = int(value[3])
      data[key] = value
  return data

#login data
def check_role(username, password, gender):
  # max_attempts = 5
  
  if username == "admin" and password == "admin123123":
    return "Hi admin"
  elif username in data and gender == "male" and password == "":
    return f'Hi Mr. {data[username][1]}'
  elif username in data and gender == "female" and password == "":
    return f'Hi Mrs. {data[username][1]}'
  return "Incorrect Username and/or Password"

#admin menu
def display_admin_menu():
  print( "welcome Mr.admin!Choose one of these options to go forward.\n 1. Display Statistics\n 2. Add an Employee\n 3. Display all Employees \n 4. Change Employee’s Salary\n 5. Remove Employee\n 6. Raise Employee’s Salary\n 7. Exit")

#display statistics
def display_statistics(data):
  male = 0
  female = 0
  for key, value in data.items():
    if data[2] == "male":
      male += 1
      return male
    elif data[2] == "female":
      female += 1
      return female
    return "wrong input" 
  print('Male :' + str(male))
  print('Female :' + str(female))
