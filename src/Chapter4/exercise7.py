def computegrade(score):
    if not(0.0<=score<=1.0):
        print("Bad Score")
        exit()
    else:
        if score>=0.9:
                return ("A")
        elif score>=0.8:
                return ("B")
        elif score>=0.7:
                return ("C")
        elif score>=0.6:
                return ("D")
        else:
                return ("F") 

try:
    score=float(input("Enter a score between 0.0 and 1.0:"))
except:
    print("Bad score")
    exit()

print(computegrade(score))