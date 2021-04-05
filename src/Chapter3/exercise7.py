try:
    location=input("Enter job offer location:")
    pay=float(input("Enter pay:"))
except:
    print("Invalid input!!.")
    exit()


if  location=="Kampala":
    if pay>=10000000:
        print("Sure I can work with this.")
    else:
        print("No way!")    
elif location=="Mbarara":
    if pay>4000000:
        print("Sure I can work with this.")
    else:
        print("No Thanks, I can find something better.")
elif location=="Space":
    print("Without a doubt, I'll take it.")
else:
    if pay>=6000000:
        print("Sure I can work with this.")
    else:
        print("No Thanks, I can find something better.")
    
    