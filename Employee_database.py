#import file
def convertFileToDictionary(file_pathway):#https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
  data = {}
  with open(file_pathway) as f:#https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
    for line in f:
      line = line.strip()
      items = line.split(',')
      key = items[0]
      value = items[1:]
      value[1] = int(value[1])
      value[2] = value[2].lower() # make sure m or f is alwayss in lower
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
  return "invalid"