import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Kalkulator Integral dan Turunan")

st.title("🧮 Kalkulator Integral dan Turunan")
st.markdown("Masukkan fungsi aljabar dalam variabel `x`. Contoh: `x**2 + 3*x - 5`")

x = sp.symbols('x')

with st.form("form_input"):
    expr_str = st.text_input("Fungsi f(x):", "x**2 + 3*x - 5")
    nilai_x = st.number_input("Masukkan nilai x:", value=1.0)
    submitted = st.form_submit_button("Hitung")

if submitted:
    try:
        expr = sp.sympify(expr_str)
        deriv = sp.diff(expr, x)
        integ = sp.integrate(expr, x)

        st.subheader("📘 Hasil Simbolik")
        st.latex(f"f(x) = {sp.latex(expr)}")
        st.latex(f"f'(x) = {sp.latex(deriv)}")
        st.latex(f"\\int f(x)\\,dx = {sp.latex(integ)} + C")

        # Evaluasi numerik
        f_val = expr.subs(x, nilai_x)
        d_val = deriv.subs(x, nilai_x)
        i_val = integ.subs(x, nilai_x)

        st.write(f"f({nilai_x}) = `{f_val}`")
        st.write(f"f'({nilai_x}) = `{d_val}`")
        st.write(f"Integral hingga x = {nilai_x} adalah `{i_val}`")

        # Grafik
        st.subheader("📈 Grafik Fungsi dan Turunan")
        f_lambd = sp.lambdify(x, expr, 'numpy')
        d_lambd = sp.lambdify(x, deriv, 'numpy')

        x_vals = np.linspace(-10, 10, 400)
        y_vals = f_lambd(x_vals)
        dy_vals = d_lambd(x_vals)

        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label='f(x)')
        ax.plot(x_vals, dy_vals, '--', label="f'(x)", color='orange')
        ax.set_title("Grafik Fungsi dan Turunan")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")

