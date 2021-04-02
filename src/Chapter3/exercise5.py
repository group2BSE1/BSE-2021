try:
    pple=int(input("Enter the number of people attending the wedding:"))
except:
    print("Invalid input!!.")
    exit()

if pple<=50:
    print("Catering will cost $4,000")
elif pple<=100:
    print("Catering will cost $10,000")
elif pple<=200:
    print("Catering will cost $15,000")
elif pple>200:
    print("Catering will cost $20,000")

    

    
    
    