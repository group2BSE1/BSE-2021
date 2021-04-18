def computepay(hours,rate):
    extra=(hours-40)*rate*1.5
    if hours>40:
        pay=extra+(40*rate)
    else:
        pay=hours*rate
    print("Pay:",pay)

try:
    hours=float(input("Enter Hours:"))
    rate=float(input("Enter Rate:"))
except:
    print("Please enter numeric input:")
    exit()
    
computepay(hours,rate)