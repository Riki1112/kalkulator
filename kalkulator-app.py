import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Kalkulator Integral dan Turunan")

st.title("🧮 Kalkulator Integral dan Turunan")
st.markdown("Gunakan slider untuk mengubah fungsi f(x) = a*x² + b*x + c")

# Slider untuk koefisien
a = st.slider("Koefisien a (x²)", -10.0, 10.0, 1.0)
b = st.slider("Koefisien b (x)", -10.0, 10.0, 3.0)
c = st.slider("Koefisien c (konstanta)", -10.0, 10.0, -5.0)

x = sp.symbols('x')
expr = a * x**2 + b * x + c
deriv = sp.diff(expr, x)
integ = sp.integrate(expr, x)

# Hasil simbolik
st.subheader("📘 Hasil Simbolik")
st.latex(f"f(x) = {sp.latex(expr)}")
st.latex(f"f'(x) = {sp.latex(deriv)}")
st.latex(f"\\int f(x) dx = {sp.latex(integ)} + C")

# Evaluasi nilai
val_x = st.number_input("Evaluasi pada nilai x =", value=1.0)
f_val = expr.subs(x, val_x)
d_val = deriv.subs(x, val_x)
i_val = integ.subs(x, val_x)

st.write(f"f({val_x}) = `{f_val}`")
st.write(f"f'({val_x}) = `{d_val}`")
st.write(f"Integral hingga x = {val_x} adalah `{i_val}`")

# Grafik
st.subheader("📈 Grafik Fungsi dan Turunan")

f_lambd = sp.lambdify(x, expr, 'numpy')
d_lambd = sp.lambdify(x, deriv, 'numpy')

x_vals = np.linspace(-10, 10, 400)
y_vals = f_lambd(x_vals)
dy_vals = d_lambd(x_vals)

fig, ax = plt.subplots()
ax.plot(x_vals, y_vals, label='f(x)', color='blue')
ax.plot(x_vals, dy_vals, label="f'(x)", linestyle='--', color='orange')
ax.set_title("Grafik Fungsi dan Turunan")
ax.legend()
ax.grid(True)

st.pyplot(fig)
