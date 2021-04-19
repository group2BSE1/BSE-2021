#creating function that prints purchase price
def purchase_price(price1):
    a=price1//1
    b=price1%1
    if a==0:
        payment_due=print(f"Payment due:{b*100:.0f} cents")       
    else:
        payment_due=print(f"Payment due:{a:.0f} dollars and {b*100:.0f} cents")

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
    purchase_price(price1)

#initializing money
nickels=25
dimes=25
quarters=25
ones=0
fives=0
print("Welcome to the vending machine change maker program")
print("Change maker initialized.")
print(f"Stock contains:\n {nickels} nickels\n {dimes} dimes\n {quarters} quarters\n {ones} ones\n {fives} fives")

#main program
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
        else:
            print("Illegal price: Must be a non-negative multiple of 5 cents.")
    except:
        print("Invalid input!!")
        continue