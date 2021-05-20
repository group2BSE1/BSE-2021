#Function compare income and the integers
def ref(income):
    if income==1:
        income="WB_LI"
        return income
    elif income==2:
        income="WB_LMI"
        return income
    elif income==3:
        income="WB_UMI"
        return income
    elif income==4:
        income="WB_HI"
        return income
    else:
        print("Invalid income")

while True:
    try:
        file = input('Enter input file:')
        if file.endswith(".txt"):
            pass
        else:
            print("File must end with \".txt\"")
            continue
        year = int(input('Enter year:'))
        year = str(year)
        income = int(input('Enter income level:'))
        income2=ref(income)
        measles = open(file, 'r')
        for line in measles:
            if (income2==line[51:56]) and (year==line[88:92]):
                save.write(line)
                print("Done")
        #report(year,income2)
        print("Success!!")
        break
    except:
        print("Error!! , Invalid Input!!")
        break
