from tabulate import tabulate


def main():
  while True:
    x = str(input("Enter .csv file name: "))
    try:
      print(table_maker(x))
      break
    except:
      print("Invalid input")
      pass


def table_maker(file_name):
  details = []
  with open(file_name) as file:
    for line in file:
      x = line.rstrip().split(",")
      details.append(x)
    return (tabulate(details[1:], headers=details[0], tablefmt="grid"))


if __name__ == "__main__":
  main()
