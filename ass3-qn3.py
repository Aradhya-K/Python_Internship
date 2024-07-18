start = int(input("Start: "))
end = int(input("End: "))

for num in range(start, end+1):
     if num % 4 == 0:
          print(f"{num} is a leap year ")
     else:
          print(f"{num} is not a leap year ")