def investment(C,r,n,t):
    p=C*((1+((r)/n))**(t*n))
    return p

C=float(input("Enter initial amount:"))
r=float(input("Enter the yearly rate:"))
t=float(input("Enter years till maturation:"))
n=float(input("Enter compound interest:"))

print(f"The final value is {investment(C,r,t,n):,.2f}")

