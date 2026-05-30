def add(a,b):
    return a+b

def subtract(a,b):
    return a-b 

def multiply(a,b):
    return a*b

def devide(a,b):
    return a/b

print("      ==CALCULATOR APP==")
for i in range(100000):
    try:
       a = int(input("Enter your first num :"))
       b = int(input("Enter your second num:"))
    except ValueError:
        print("Please enter a number")
        break

    print("1-add\n2-subtract\n3-multiply\n4-devide")
    try:
      n = int(input("Enter your choise number:"))
      if n ==1:
          print(add(a,b))
      elif n==2:
          print(subtract(a,b))
      elif n==3:
          print(multiply(a,b))
      elif n==4:
          print(devide(a,b))
      else:
          print("please enter a valid number")
    except ValueError:
       print("Please enter a number")
       


