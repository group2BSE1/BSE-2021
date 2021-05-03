#Main program
print("Welcome!!!!")
while True:
    try:
        code=input("Enter customer code:")
        if code=="r" or code=="R":
            print("Valid R")
        elif code=="c" or code=="C":
            print("Valid C")
        elif code=="i" or code=="I":
            print("Valid I")
        else:
            print("Invalid code")
            continue
    except:
        print("\nError!!! Enter valid code.")
        break