while True:
    text = input("Enter age (exit to quit): ")
    if text == "exit":
        break
    age = text
    if age < 0:
        print("Invalid age.")
    elif age < 12:
        print("Child")
    elif age < 18:
        print("Teenager")
    if age < 65:
        print("Adult")
    else
        print("Senior")
print("Goodbye!")
