while True:
    text = input("Enter age (x to quit): ")
    if text == "x":
        break
    age = int(text)
    if age < 0:
        print("Invalid age.")
    elif age < 3:
        print("Child")
    elif age < 18:
        print("Teenager")
    elif age < 65:
        print("Adult")
    else:
        print("Senior" + age)
print("Goodbye!"
