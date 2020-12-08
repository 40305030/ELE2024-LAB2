import sympy as sym
# Define the symbols a, b, c, d and declare them are real positive
a, b, c, d = sym.symbols('a:d', real=True , positive=True )
t, omega = sym.symbols('t, omega')
s = sym.symbols('s')
# Define G_theta symbolically:
G_theta = -c / (s**2 - d)
# 1.1. Impulse response
x3s_imp = G_theta
x3t_imp = sym.inverse_laplace_transform(x3s_imp, s, t)
sym.pprint(x3s_imp)
# 1.2. Step Response of G_theta
x3s_step = G_theta / s
x3t_step = sym.inverse_laplace_transform(x3s_step, s, t)
sym.pprint(x3t_step)
# 1.3. Frequency response
x3s_freq = G_theta*(omega / (s**2 + omega**2))
x3t_freq = sym.inverse_laplace_transform(x3s_freq, s, t)
sym.pprint(x3s_freq)
#------------------------------------------------------------
# Define Gx symbolically:
G_x = ( a*s**2 - a*d +b*c ) / ((s**2 - d)*s**2)
# 2.1. Impulse response
x1s_imp = G_x
x1t_imp = sym.inverse_laplace_transform(x1s_imp, s, t)
sym.pprint(x1s_imp)
# 2.2. Step Response of G_x
x1s_step = G_x / s
x1t_step = sym.inverse_laplace_transform(x1s_step, s, t)
sym.pprint(x1s_step)
# 2.3. Frequency response
x1s_freq = G_x*(omega / (s**2 + omega**2))
x1t_freq = sym.inverse_laplace_transform(x1s_freq, s, t)
sym.pprint(x1s_freq)
