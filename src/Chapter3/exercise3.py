try:
    grade=float(input("Enter a score between 0.0 and 1.0:"))
except:
    print("Bad score")
    exit()

if not(0.0<=grade<=1.0):
        print("Bad Score")
else:
    if grade>=0.9:
            print("A")
    elif grade>=0.8:
            print("B")
    elif grade>=0.7:
            print("C")
    elif grade>=0.6:
            print("D")
    else:
            print("F") 

    
    