#Jitender Rajpoot
#Lab 6

#list 5 strings
names = ["Andrew", "Natalia", "Eddie", "Ethan", "Carlos"]
print("The original list is: ")
print(names)

print("Enter a number 1, 2, or 3")
menu = input("1. Add student, 2. Modify student name, 3. Remove student ")
#print(menu)


if menu == "1":
    newName = input("What's the new student name? ")
    names.append(newName)
    print("List after adding a new name: ")
    for i in names:
        print(i)

elif menu == "2":
    print("0", names[0])
    print("1", names[1])
    print("2", names[2])
    print("3", names[3])
    print("4", names[4])
        
    changeNum = int(input("Enter the number [0-4] you want to change: "))
    #names.pop(changeNum)
    changeName = input("Enter a new student name: ")
    #names.insert(changeNum, changeName)
    names[changeNum] = changeName
    print("List after exchanging a name")
    for i in names:
        print(i)

elif menu == "3":
    print("0", names[0])
    print("1", names[1])
    print("2", names[2])
    print("3", names[3])
    print("4", names[4])

    removeNum = int(input("Enter a number [0-4] you want to remove: "))
    names.pop(removeNum)
    print("List after removing a name: ")
    for i in names:
        print(i)
