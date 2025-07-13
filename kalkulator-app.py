import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def main():
    print("=== Kalkulator Turunan dan Integral ===")
    expr_str = input("Masukkan fungsi (misal: x**2 + 3*x - 5): ")

    x = sp.symbols('x')
    try:
        expr = sp.sympify(expr_str)

        # Turunan dan Integral
        deriv = sp.diff(expr, x)
        integ = sp.integrate(expr, x)

        print(f"\nFungsi asli     : {expr}")
        print(f"Turunan simbolik: {deriv}")
        print(f"Integral simbolik: {integ} + C")

        # Evaluasi numerik (opsional)
        val = float(input("\nMasukkan nilai x untuk evaluasi numerik: "))
        f_val = expr.subs(x, val)
        d_val = deriv.subs(x, val)
        i_val = integ.subs(x, val)

        print(f"f({val}) = {f_val}")
        print(f"f'({val}) = {d_val}")
        print(f"Integral hingga x={val} = {i_val}")

        # Bonus: Grafik
        plot_graph(expr, deriv)

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def plot_graph(expr, deriv):
    x = sp.symbols('x')
    f_lambd = sp.lambdify(x, expr, 'numpy')
    d_lambd = sp.lambdify(x, deriv, 'numpy')

    x_vals = np.linspace(-10, 10, 400)
    y_vals = f_lambd(x_vals)
    dy_vals = d_lambd(x_vals)

    plt.figure(figsize=(10, 5))
    plt.plot(x_vals, y_vals, label='Fungsi Asli f(x)')
    plt.plot(x_vals, dy_vals, label="Turunan f'(x)", linestyle='--')
    plt.title("Grafik Fungsi dan Turunan")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()
