import sympy as sp

x=sp.symbols('x')
f=x**3 -5*x+7



#compute derivative
derivative=sp.diff(f,x)

print("Function: ",f)
print("Derivetive: ",derivative)