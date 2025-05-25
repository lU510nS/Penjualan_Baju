import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Judul
st.title("Aplikasi Turunan Parsial dan Visualisasi Bidang Singgung")

# Simbol
x, y = sp.symbols('x y')

# Input fungsi
func_input = st.text_input("Masukkan fungsi f(x, y):", "x**2 + y**2")

try:
    # Konversi input ke ekspresi
    f_expr = sp.sympify(func_input)
    fx = sp.diff(f_expr, x)
    fy = sp.diff(f_expr, y)

    # Input titik evaluasi
    px = st.number_input("Masukkan nilai x =", value=1.0)
    py = st.number_input("Masukkan nilai y =", value=2.0)

    # Evaluasi nilai turunan dan fungsi
    fx_val = fx.subs({x: px, y: py})
    fy_val = fy.subs({x: px, y: py})
    f_val = f_expr.subs({x: px, y: py})

    st.write(f"Turunan parsial terhadap x: {fx}, nilai di titik ({px}, {py}) = {fx_val}")
    st.write(f"Turunan parsial terhadap y: {fy}, nilai di titik ({px}, {py}) = {fy_val}")

    # Bidang singgung
    tangent_plane = fx_val * (x - px) + fy_val * (y - py) + f_val

    # Meshgrid untuk plot
    X, Y = np.meshgrid(np.linspace(px-3, px+3, 30), np.linspace(py-3, py+3, 30))
    f_lambd = sp.lambdify((x, y), f_expr, "numpy")
    Z = f_lambd(X, Y)

    tp_lambd = sp.lambdify((x, y), tangent_plane, "numpy")
    Zt = tp_lambd(X, Y)

    # Plotting
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)
    ax.plot_surface(X, Y, Zt, color='red', alpha=0.5)
    ax.scatter(px, py, f_val, color='black', s=50)
    ax.set_title("Grafik f(x, y) dan Bidang Singgung")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("f(x, y)")
    st.pyplot(fig)

except Exception as e:
    st.error(f"Terjadi kesalahan saat memproses fungsi: {e}")
