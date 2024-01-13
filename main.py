title = "\033[31m=\033[0m=\033[34m=\033[33m To Do List Manager \033[31m=\033[0m=\033[34m="

print(f"{title:^80}")
print()

ToDoList = []

def printList():
  menu = input("ToDoList Manager\n\nDo you want to view, add or edit the todo list?\n:> ")
  if menu == "view":
    for item in ToDoList:
      print(item)
  elif menu == "add":
    item = input("What's next on the Agenda?: ")
    ToDoList.append(item)
  elif menu == "remove":
    item = ("What do you want to remove?: ")
    if item in ToDoList:
      ToDoList.remove(item)
    else:
      print(f"{item} was not in the list")

while True:
  printList()
  print()

