p = int(input("Enter the principle : "))
r = int(input("Enter the return percentage : "))
n = int(input("Enter the number of years : "))
A = p*((1+(r/100))**n)
print(f"Final amount is:  {A}")
# Answer is option b- 162.89