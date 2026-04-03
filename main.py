import csv

def start_prgrm():
  loop = True
  while loop:
    ui = input("//Start Rocket Program? (y/n): ")
    if ui == "y":
      token = 0
      loop = False
      print("\n//Starting . . .\n")
    elif ui == "n":
      token = 1
      loop = False
    else:
      print(f"//Error, input: {ui} not recognized.")
  return token

def read_file():
  d_temp = {}
  count = 0
  fp = open("rockets.csv", "r")
  reader = csv.reader(fp)
  print()
  for line in reader:
    display(line)
    if count >= 1:
      line1 = float(line[1])
      line2 = float(line[2])
      line3 = float(line[3])
      line4 = float(line[4])
      d_temp[line[0].lower()] = [line1, line2, line3, line4]
    count += 1
  return d_temp

def display(line):
  print(f"{line[0]:15} {line[1]:15} {line[2]:15} {line[3]:20} {line[4]:15}")

def select_prev():
  d_temp = read_file()
  rocket_list = list(d_temp.keys)
  loop = True
  while loop:
    ui = input("//Choose Previously Created Rocket or Enter Q to Quit: ").lower()
    if ui in rocket_list:
      loop= False
      rocket_specs = d_temp[ui]
      token = 0
    elif ui == "q":
      loop = False
      rocket_specs = ""
      token = 1
    else:
      print(f"//Error, input: {ui} not recognized.")
  return rocket_specs, token

def rocket_template():
  use_prev = input("//Use Previously Created Rocket? (y/n): ").lower()
  if use_prev == "y":
    rocket_specs, token = select_prev()


  return rocket_specs, token

def main():
  token = start_prgrm()
  while token == 0:
    rocket_specs, token = rocket_template()


  print("//Program Terminated")

