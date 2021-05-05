# Function for Bill
def bill(gallons,code,begin,end):
    if code=="r" or code=="R":
        amt=5+(gallons*0.0005)
    elif code=="c" or code=="C":
        if gallons>4_000_000:
            extra_gallons=gallons-4_000_000
            extra_bill=extra_gallons*0.00025
            amt=extra_bill+1000
        else:
            amt=1000
    elif code=="i" or code=="I":
        if gallons>10_000_000:
            amt=((gallons-10_000_000)*0.00025)+2000
        elif 4_000_000<gallons<=10_000_000:
            amt=2000
        else:
            amt=1000
    print()
    print("Customer code:",code)
    print("Beginning water reading:",begin)
    print("Ending water reading:",end)
    print(f"Gallons of water used:{gallons:.1f}")
    print(f"Amount billed: ${amt:.2f}")

# Function for water used
def water(begin,end,code):
    if begin>end:#complete iteration
        gallons=((1_000_000_000-begin)+end)*0.1
        bill(gallons, code, begin, end)
    elif begin<end:
        gallons=(end-begin)*0.1
        bill(gallons, code, begin, end)
    else:
        gallons=end-begin
        bill(gallons, code, begin, end)
    #print("Gallons of water used:",gallons*0.1)


def next(code):
    code=code
    while True:
        try:
            begin=int(input("Enter beginning meter number:"))
            end=int(input("Enter ending meter number:"))
            if (0<=begin) and (end<=999_999_999):
                water(begin, end, code)
                break
            else:
                print("Number exceeds meter number, Try Again!!!")
                continue
        except:
            print("\tInvalid number!!")


#Main program
print("Welcome!!!!")
while True:
    try:
        code=input("Enter customer code:")
        if code=="r" or code=="R":
            next(code)
        elif code=="c" or code=="C":
            next(code)
        elif code=="i" or code=="I":
            next(code)
        else:
            print("Invalid code")
            continue
    except:
        print("\nError!!! Enter valid code.")
        continue
