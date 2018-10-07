# -*- coding: utf-8 -*-

import sympy as sym
import matplotlib.pyplot as plt
from sympy.plotting import plot

oo = sym.oo

n = sym.Symbol("n")
x = sym.Symbol("x")
formula_p = input("n回目のゲームに勝つ確率は？ ※サンクトペテルブルクのパラドックスなら　(1/2)**n：")
formula_x = input("n回目のゲームに勝ったときの賞金Xは？ ※サンクトペテルブルクのパラドックスなら 2**n：")

formula_p = sym.sympify(formula_p)
formula_x = sym.sympify(formula_x)
formula_n = sym.solve(formula_x-x, n)
formula_n = sym.sympify(formula_n[0])
formula = formula_p.subs(n, formula_n)


def temp(x1):
    return formula_x.subs(n, x1)


print(f"求める確率分布の式は：{formula}\nただし、X=({temp(1)},{temp(2)},{temp(3)},...,{formula_x},...)")

dis_x=[temp(i) for i in range(1,11,1)]
dis_y=[formula.subs(x,j) for j in dis_x]

plt.scatter(dis_x,dis_y)
# plot(formula,(x,1,10),title="Expected value distribution")
plt.show()

formula_cul=formula_p*formula_x
result=sym.summation(formula_cul, (n, 1, oo))

print(f"期待値は、一般項{formula_cul}の無限級数の総和を求めて、{result}")