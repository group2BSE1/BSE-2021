max1=None
min1=None
while True:
    try:
        num=input("Enter a number:")
        if num=="done":
            break
        num1=int(num)
        if (max1 and min1) is None:
            max1=num1
            min1=num1
        if num1>max1:
            max1=num1
        if num1<min1:
            min1=num1
    except:
        print("Invalid input")
        continue

print(f"The maximum value is {max1} \nThe minimum value is {min1}")
    
