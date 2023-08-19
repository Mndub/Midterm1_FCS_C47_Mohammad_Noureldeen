#print hello
#import file
def convertFileToDictionary(file_pathway):
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
