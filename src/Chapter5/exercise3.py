#creating function that prints purchase price
def purchase_price(price):
    a=price//1 #Gives number of dollars
    b=price%1 #Gives number of cents
    if a==0:
        payment_due=print(f"Payment due:{b*100:.0f} cents")   
    else:
        payment_due=print(f"Payment due:{a:.0f} dollars and {b*100:.0f} cents")

#creating function to accept deposit
def deposit():
    purchase_price(price1)
    total_deposit=0
    while price1>total_deposit:
        test_price=price1
        dep=input("Indicate your deposit:")
        if dep=="c":
            print("Take the change below")
            #Function change
            print(total_deposit)
            break
        elif dep=="f":
            total_deposit=total_deposit+5
            test_price=test_price-total_deposit
            #print("Money so far:",total_deposit)
            purchase_price(test_price)
            continue
        elif dep=="o":
            total_deposit=total_deposit+1
            test_price=test_price-total_deposit
            #print("Money so far:",total_deposit)
            purchase_price(test_price)
            continue
        elif dep=="q":
            total_deposit=total_deposit+0.25
            test_price=test_price-total_deposit
            #print("Money so far:",total_deposit)
            purchase_price(test_price)
            continue
        elif dep=="d":
            total_deposit=total_deposit+0.1
            test_price=test_price-total_deposit
            #print("Money so far:",total_deposit)
            purchase_price(test_price)
            continue
        elif dep=="n":
            total_deposit=total_deposit+0.05
            test_price=test_price-total_deposit
            #print("Money so far:",total_deposit)
            purchase_price(test_price)
            continue
        else:
            print("Illegal selection:",dep)
            continue
    #print(total_deposit)

    
#creating function for menu of deposit selection
def deposit_menu():
    print("\nMenu for deposits:\n")
    print("""  'n' - deposit a nickel
  'd' - deposit a dime
  'q' - deposit a quarter
  'o' - deposit a one dollar bill
  'f' - deposit a five dollar bill
  'c' - cancel the purchase
""")


#main program
#initializing money
nickels=25
dimes=25
quarters=25
ones=0
fives=0
print("Welcome to the vending machine change maker program")
print("Change maker initialized.")
print(f"Stock contains:\n {nickels} nickels\n {dimes} dimes\n {quarters} quarters\n {ones} ones\n {fives} fives")
while True:
    try:
        #requesting for price input
        price=input("Enter the purchase price (xx.xx) or `q' to quit:")
        if price=="q":
            print("Quiting....")
            break
        price1=float(price)
        if (price1>0) and ((price1*100)%5==0):
            deposit_menu()
            deposit()
        else:
            print("Illegal price: Must be a non-negative multiple of 5 cents.")
    except:
        print("Invalid input!!")
        continue


