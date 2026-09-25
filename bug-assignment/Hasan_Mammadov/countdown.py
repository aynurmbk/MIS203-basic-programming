start = int(input("Countdown from: "))
total = 0
while start > 0:
    print(start)
    total = start
    start = start - 1
print("Go!)
print("Sum of numbers: " + total)
