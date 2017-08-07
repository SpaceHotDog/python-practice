contQuest = input("Desea importar .csv para analisis? Yes/N: ")
assert(contQuest == Yes)
raise NameError

def import_anals (file):
  dataSet = file.csv
  
  try:
    readOnly = open("dataSet", "r")
 
 except NameError:
    Print("Wrong file maybe?")
  
 finally:
    readOnly.close()  
  
