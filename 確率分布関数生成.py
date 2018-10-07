# -*- coding: utf-8 -*-

import sympy as sym

oo = sym.oo
x = sym.Symbol("x")

print("任意の連続関数f(x)を確率分布関数 c*f(x) に変形するための定数cを算出し、その後その関数の特徴を評価します。無限大対応（無限大=oo）")
fun_x = input("連続型関数f(x)を入力してください。f(x)=")
up = input("積分の上限：")
down = input("積分の下限：")


fun_x, up, down = [sym.sympify(a) for a in [fun_x, up, down]]

inte_fun_x = sym.integrate(fun_x, (x, down, up))
vul_c = 1/inte_fun_x if inte_fun_x-inte_fun_x == 0 else "（解なし）"

print(f"求めるcの値は、{vul_c}です。")
fun_x = fun_x*vul_c

escape = exit if vul_c == "（解なし）" else print
escape()


e_x = sym.integrate(x*fun_x, (x, down, up))
e_x = sym.simplify(e_x)
v_x = sym.integrate(((x-e_x)**2)*fun_x, (x, down, up))
v_x = sym.simplify(v_x)

fun_z = (fun_x-e_x)/v_x
skew, kurto = [sym.integrate((fun_z**j)*fun_x, (x, down, up)) for j in [3, 4]]
flo = [float(m) for m in [e_x, v_x, skew, kurto]]
print(
    f"平均：{e_x}  {flo[0]}\n分散：{v_x}  {flo[1]}\n歪度：{skew}  {flo[2]}\n尖度：{kurto}  {flo[3]}\n") 