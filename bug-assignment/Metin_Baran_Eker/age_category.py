while True:
    text = input("Enter age (q to quit): ")
    if text == "q":
        break
    age = int(text)
    if age < 0:
        print("Invalid age.")
    elif age < 13:
        print("Child")
    elif age < 18
        print("Teenager")
    if age < 65:
        print("Adult")
    else:
        print("Senior" + age)
print("Goodbye!")
