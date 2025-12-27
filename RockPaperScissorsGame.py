per1 = input("Enter S or P or R: ")
per2 = input("Choose again but not same: ")

if per1 == "S" and per2 == "P":
    print("Person1 wins")

elif per1 == "P" and per2 == "S":
    print("Person2 wins")

elif per1 == "R" and per2 == "P":
    print("Person1 wins")

elif per1 == "P" and per2 == "R":
    print("Person2 wins")

elif per1 == "R" and per2 == "S":
    print("Person1 wins")

elif per1 == "S" and per2 == "R":
    print("Person2 wins")

elif per1 == per2 and per1 in ["S", "P", "R"]:
    print("Tie")

else:
    print("Invalid Input")
