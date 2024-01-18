import os, time

title = "\033[31m=\033[0m=\033[34m=\033[33m To Do List Manager \033[31m=\033[0m=\033[34m="

print(f"{title:^80}")
print()

ToDoList = []

def printList():
  menu = input("ToDoList Manager\n\n What do you want to do?\n view\n add\n remove\n\n:> ")
  if menu == "view" or menu == "View" or menu == "VIEW":
    for item in ToDoList:
      counter = 0
      counter += 1
      print(f"{counter}:{item}")
      time.sleep(5)
  elif menu == "add" or menu == "Add" or menu == "ADD":
    item = input("What's next on the Agenda?: ")
    ToDoList.append(item)
  elif menu == "remove" or menu == "Remove" or menu == "REMOVE":
    item = ("What do you want to remove?: ")
    if item in ToDoList:
      ToDoList.remove(item)
    else:
      print(f"{item} was not in the list")

while True:
  printList()
  print()
  os.system("clear")

