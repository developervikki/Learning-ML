import sympy as sp

x=sp.symbols('x')
f=x**2
derivative=sp.diff(f,x)


print("Derivative: ",derivative)


x,y=sp.symbols('x y')
f=x**2 + y**2
grad_x=sp.diff(f,x)
grad_y=sp.diff(f,y)


print("Partial derivatives: \n", grad_x, grad_y)