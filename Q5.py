import sympy as sym
import control as ctrl
import matplotlib.pyplot as plt
import numpy as np
m, ell, x3, x4, M, g, F = sym.symbols('m, ell ,x3, x4, M, g, F')

phi = 4*M*ell*x4**2*sym.sin(x3) + 4*F - 3*m*g*sym.sin(x3)*sym.cos(x3)
phi /= 4*(M+m) - 3*m*sym.cos(x3)**2

dphi_x3 = phi.diff(x3)
dphi_x4 = phi.diff(x4)
dphi_F = phi.diff(F)

# Equilibrium point
Feq = 0
x3eq = 0
x4eq = 0

dphi_F_eq = dphi_F.subs([(F, Feq), (x3, x3eq), (x4, x4eq)])
dphi_x3_eq = dphi_x3.subs([(F, Feq), (x3, x3eq), (x4, x4eq)])
dphi_x4_eq = dphi_x4.subs([(F, Feq), (x3, x3eq), (x4, x4eq)])

a = dphi_F_eq
b = -dphi_x3_eq
c = 3/(ell*(4*M + m))
d = 3*(M+m)*g/(ell*(4*M + m))

M_value = 0.3
m_value = 0.1
g_value = 9.81
ell_value = 0.35

def evaluate_at_given_parameters(z):
        return float(z.subs([(M, M_value), (m, m_value), (ell, ell_value), (g, g_value)]))

a_value = evaluate_at_given_parameters(a)
b_value = evaluate_at_given_parameters(b)
c_value = evaluate_at_given_parameters(c)
d_value = evaluate_at_given_parameters(d)
# ---------------------------------------------
# Control library of Python
# ---------------------------------------------
transfer_function_F2x3 = ctrl.TransferFunction([-c_value], [1, 0, -d_value])
# Define a PID controller (using function `pid` introduced above)
def pid(Kp, Ki, Kd):
        Gc = ctrl.TransferFunction([Kp], [1])
        Gc += ctrl.TransferFunction([Kd, 0], [1])
        Gc -= ctrl.TransferFunction([Ki], [1, 0])
        return Gc

transfer_function_pid = -pid(Kp=100, Ki=0.5, Kd=10)
# Plot the impulse response of the c/l system
overall_tf = ctrl.feedback(transfer_function_F2x3, transfer_function_pid)
t_final = 1
num_points = 500
t_imp, x3_imp = ctrl.impulse_response(overall_tf, T=np.linspace(0, t_final, num_points))
degree = (180/np.pi)*x3_imp
import matplotlib.pyplot as plt
plt.plot(t_imp, x3_imp)
plt.xlabel('Time (s)')
plt.ylabel('Degree(°)')
plt.show()
