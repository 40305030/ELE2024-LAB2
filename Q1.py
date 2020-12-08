import sympy as sym
import control as ctrl

m, ell, x3, x4, M, g, F = sym.symbols('m, ell ,x3, x4, M, g, F')
#-------------------------------------------------------------------------
# φ(F, x3, x4)
phi = (4*M*ell*x4**2*sym.sin(x3) + 4*F - 3*m*g*sym.sin(x3)*sym.cos(x3)) / (4*(M+m) - 3*m*sym.cos(x3)**2)

def evaluate_at_equilibrium (f):
    return f.subs([(F, 0), (x3, 0), (x4, 0)])

dphi_F_eq = evaluate_at_equilibrium (phi.diff (F))
dphi_x3_eq = evaluate_at_equilibrium (phi.diff (x3))
dphi_x4_eq = evaluate_at_equilibrium (phi.diff (x4))

sym.pprint(dphi_F_eq)
sym.pprint(dphi_x3_eq)
sym.pprint(dphi_x4_eq)
#--------------------------------------------------------------------
#ψ(F, x3, x4)
psi = (-3)*(m*ell*(x4**2)*sym.sin(x3)*sym.cos(x3) + F*sym.cos(x3) - (M + m)*g*sym.sin(x3)) / ((4*(M + m) - 3*m*(sym.cos(x3)**2))*ell)

dpsi_F_eq = evaluate_at_equilibrium (psi.diff (F))
dpsi_x3_eq = evaluate_at_equilibrium (psi.diff (x3))
dpsi_x4_eq = evaluate_at_equilibrium (psi.diff (x4))

sym.pprint(dpsi_F_eq)
sym.pprint(dpsi_x3_eq)
sym.pprint(dpsi_x4_eq)
