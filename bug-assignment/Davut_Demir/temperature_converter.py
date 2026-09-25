count = 0
while True
    text = input("Enter temperature in Celsius (x to quit): ")
    if text == "x":
        break
    celsius = float(text)
    fahrenheit = celsius * 5 / 9 + 32
    count = count + 1
    print(f"{celsius} C = {farenheit} F")
print(f"You converted {count} temperatures.")
