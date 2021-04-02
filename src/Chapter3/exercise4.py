try:
    age = int(input("Wat is ur age:"))
except:
    print("Please enter a valid age!!!.")
    exit()

if age>=18:
    print("You can vote.")
elif 0<age<=17:
    print("Too young to vote.")
else:
    print("You are a time traveller.")
