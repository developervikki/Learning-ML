import sympy as sp

#define a function

x=sp.symbols('x')
f=sp.exp(-x)


#compute indefinite integral

indefinite_integral=sp.integrate(f,x)
print("indefinite interagl: ",indefinite_integral)



#compute definite integral
definite_integral=sp.integrate(f,(x,0,sp.oo))
print("definite interagl: ",definite_integral)