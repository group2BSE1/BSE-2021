C=float(input("Enter initial amount:"))
r=float(input("Enter the yearly rate:"))
t=float(input("Enter years till maturation:"))
n=float(input("Enter compound interest:"))
final_value=C*((1+((r/100)/n))**(t*n))
print("The final value is ",round(final_value,2))
