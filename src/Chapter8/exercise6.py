numbers=[]
while True:
    number=input("Enter a number:")
    if number=="done":
        break
    else:
        number=float(number)
        numbers.append(number)
        continue
print("Maximum:",max(numbers))
print("Minimum:",min(numbers))