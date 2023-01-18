import sys
#importing os-sys module
from tabulate import tabulate
#importing tabulate

try:
  #Tries to index sys.argv over the 0th index, if exception arrises goes to except block on line 38
  if len(sys.argv) == 2 and ".csv" in sys.argv[1]:
    #Checks if the right number of command line arguements were given
    try:
      #Checks if .csv file exists
      details = []
      #Creating a list for all the details in the csv file
      with open(sys.argv[1]) as file:
        #Opens the file mentioned in the command line arguement as "file"
        for line in file:
          #Iterates through the .csv file line by line
          x = line.rstrip().split(",")
          #Strips off the spaces from each line and splits each element by a comma and creates a list of the values (x represent a row)
          details.append(x)
          #appends the list x (containing each row) to the list called "details"
        print(tabulate(details[1:], headers=details[0], tablefmt="grid"))
        #uses the tabulate function to print out an ascii table
        #Takes 3 arguements: tabulate(details, headers, tablefmt)
        #Treats all the elements in the 0th index as the headers and all subsequent elements as the details
        #For eg. [["Roll No.", "Name"], ["1", "ABC"], ["2", "DEF"], ["3", "XYZ"]]
        #Splicing the details list by [1:] assigns the details the value of all the lists post the 0th index
        #Splicing the details list by [0] assigns the header variable the list at the 0th index
    except FileNotFoundError:
      #If .csv file does not exit
      sys.exit("File does not exist")
  elif (".csv" not in sys.argv[1]):
    #If the command line arguement does not consist of a .csv file
    sys.exit("Not a CSV file")
  elif len(sys.argv) > 2:
    #If too many command line arguements are provided
    sys.exit("Too many command-line arguements")
except IndexError:
  #If no command lines are given post "$python main.py"
  sys.exit("Too few command-line arguements")
