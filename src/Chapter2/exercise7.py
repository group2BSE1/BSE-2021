amount=float((input("Enter an amount to make change for:")))
print("Your change is...")
print(amount//20,"twenties")
amount=amount%20
print(amount//10,"tens")
amount=amount%10
print(amount//5,"fives")
#
amount=amount%5
print(amount//1,"ones")
amount=amount%1
print(amount//0.25,"quarters")
amount=amount%0.25
print(amount//0.1,"dimes")
amount=amount%0.1
print(amount//0.05,"nickel")
amount=amount%0.05
print(amount//0.01,"pennies")





