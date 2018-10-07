# -*- coding: utf-8 -*-

import sympy as sym

a = sym.Symbol("a", real=True)
x = sym.Symbol("x")
f = sym.Function("f")

oo = sym.oo

# E(x-a)^2を最小にするaの値を求める。


func_1 = sym.integrate((x-a)**2*f(x), (x, -oo, oo)).expand()
func_1 = func_1.doit()

func_2 = sym.diff(func_1, a)
func_2 = func_2.expand()

func_3 = (sym.solve(func_2, a)[0]
          .subs(sym.integrate(f(x), (x, -oo, oo)), 1)
          )

print(f"a={func_3}")
