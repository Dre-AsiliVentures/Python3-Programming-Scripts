a=float(input("Enter a ")) # Enter value of a as float
b=float(input("Enter b ")) # Enter value of b as float
c=float(input("Enter c ")) # Enter value of c as float
d=(b**2)-(4*a*c)
#print("Value of d is {}".format(d))
soln1=(-b+(d**0.5))/(2*a)
#print("Value of soln1 is {}".format(soln1))
soln2=(-b-(d**0.5))/(2*a)
#print("Value of soln2 is {}".format(soln2))
#print("The solutions are {} {}".format(soln1,soln2))
print("The solutions are {:.3} {:.3}".format(soln1,soln2))