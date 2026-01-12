def quad_solv(a, b, c):
   """ This function solve the quadratic equation """
   term = b**2 - 4*a*c
   if term < 0:
      print("Error: No real soltions")
   else:
      sol_1 = (-b + term**0.5)/(2*a)
      sol_2 = (-b - term**0.5)/(2*a)
   return sol_1, sol_2

a = float(input("Enter the parameter of x^2: "))
b = float(input("Enter the parameter of x: "))
c = float(input("Enter the constant term: "))

x1, x2 = quad_solv(a, b, c)
print("The soltions are: ", x1, x2)

