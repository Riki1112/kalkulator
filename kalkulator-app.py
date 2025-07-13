import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Kalkulator Integral dan Turunan")

st.title("🧮 Kalkulator Integral dan Turunan")
st.markdown("Masukkan fungsi aljabar dalam variabel `x`. Contoh: `x**2 + 3*x - 5`")

# Input fungsi
expr_str = st.text_input("Fungsi f(x):", "x**2 + 3*x - 5")

x = sp.symbols('x')

try:
    expr = sp.sympify(expr_str)
    deriv = sp.diff(expr, x)
    integ = sp.integrate(expr, x)

    st.subheader("📘 Hasil Simbolik")
    st.latex(f"f(x) = {sp.latex(expr)}")
    st.latex(f"f'(x) = {sp.latex(deriv)}")
    st.latex(f"\\int f(x)\\,dx = {sp.latex(integ)} + C")

    # Evaluasi numerik
    st.subheader("🔢 Evaluasi Numerik")
    val = st.number_input("Masukkan nilai x:", value=1.0)
    f_val = expr.subs(x, val)
    d_val = deriv.subs(x, val)
    i_val = integ.subs(x, val)

    st.write(f"f({val}) = `{f_val}`")
    st.write(f"f'({val}) = `{d_val}`")
    st.write(f"Integral hingga x = {val} adalah `{i_val}`")

    # Grafik
    st.subheader("📈 Grafik Fungsi dan Turunan")
    f_lambd = sp.lambdify(x, expr, 'numpy')
    d_lambd = sp.lambdify(x, deriv, 'numpy')

    x_vals = np.linspace(-10, 10, 400)
    y_vals = f_lambd(x_vals)
    dy_vals = d_lambd(x_vals)

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label='f(x)')
    ax.plot(x_vals, dy_vals, label="f'(x)", linestyle='--')
    ax.set_title("Grafik Fungsi dan Turunan")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")
