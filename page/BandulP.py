import streamlit as st
import numpy as np
from scipy.integrate import solve_ivp
from VisualGraph import create_graph,create_simulation
from Formula import Spring_Osci

def teks1():
    st.subheader("Model Persamaan📚")
    st.text('Persamaan pada Pendulum yang dihubungkan dg pegas diproyeksi pada dua sumbu yakni sumbu x dan sumbu y. Pada sumbu x diberika dalam bentuk ')
    st.latex(r'''
    \sum F_x=ma_x 
    ''')
    st.latex(r'''
    m \frac{d^2 x}{dt^2}=-k(x-L)\sin{\theta}=-\frac{k(x-L)x}{\sqrt{x^2+y^2}} 
    ''')
    st.text("dan untuk pada arah sumbu y")
    st.latex(r'''
    \sum F_y=ma_y 
    ''')
    st.latex(r'''
    m \frac{d^2 y}{dt^2}=mg-k(x-L)\cos{\theta}=mg-\frac{k(x-L)y}{\sqrt{x^2+y^2}} 
    ''')
    st.text("dengan 2 persamaan diatas dapat dicari solusi untuk nilai x dan y dengan memodifikasi persamaannya menjadi")
    st.latex(r'''
    \frac{dx}{dt}=v_x \\ m \frac{dv_x}{dt}=-\frac{-k(x-L)x}{\sqrt{x^2+y^2}} 
    ''')
    st.divider()
    st.latex(r'''
    \frac{dy}{dt}=v_y \\ m \frac{dv_y}{dt^2}=mg-\frac{k(x-L)y}{\sqrt{x^2+y^2}}
    ''')
    st.markdown("Dengan menggunakan Library Scipy untuk menyelesaikan Model Persamaan diferensial diatas, Model persamaan diferensial disusun dalam kode Python sebagai berikut")
    st.code(
        '''
        def pendulum_spring(t, z):
        x, vx, y, vy = z # Kondisi awal
        r = (x**2 + y**2)**(0.5)  # Panjang pegas
        F_spring = k * (r - L)  # Gaya pegas
        ax = -F_spring * (x / r) / m  # Percepatan di arah x
        ay = g-F_spring * (y / r) / m   # Percepatan di arah y
        return [vx, ax, vy, ay]

        # Kondisi awal
        x0 = 1.0  
        y0 = -1.0  
        vx0 = 0.0  
        vy0 = 0.0  
        z0 = [x0, vx0, y0, vy0]

        # Waktu simulasi
        t_span = (0, 10) 
        t_eval = np.linspace(t_span[0], t_span[1], 1000)

        # Simulasi dengan solve_ivp
        sol = solve_ivp(pendulum_spring, t_span, z0, t_eval=t_eval, method='RK45')

        # Ekstraksi hasil
        x, y = sol.y[0], sol.y[2]
        '''
        )
        

def app():
    
    st.title("Gerak Pendulum dengan Pegas💡")
    teks1()
    st.subheader("Solusi dan Visualisasi 🔬")
    g = st.slider("Percepatan Gravitasi ", 0.0, 100.0, 9.81)
    l = st.slider("Panjang tali", 0.0, 5.0, 1.0)
    m = st.slider("Massa beban", 0.00, 5.00, 1.0)
    k = st.slider("Konstanta Pegas", 0.0, 50.0, 50.0)
    oscillator = Spring_Osci(g,l,m,k)
    
    # Kondisi awal
    y0 = [1.0, -1.0, 0.0, 0.0]
    # Waktu yang akan dihitung
    t_span = (0, 10)  # dari t = 0 hingga t = 10
    t_eval = np.linspace(0, 10, 1000)

    # Menyelesaikan persamaan diferensial
    solution = solve_ivp(oscillator, t_span, y0, t_eval=t_eval)

    # theta = solution.y[0]
    t = solution.t
    # Plot hasilnya
    X, Y = solution.y[0], solution.y[2]

    option = st.selectbox(
    "Visualisasi:",
    ("x terhadap t", "y terhadap x"),
    )

    if option == "x terhadap t":
        create_graph(t,X,Nama="Osilasi dg Pegas")
    if option == "y terhadap x":
        create_graph(X,Y,Nama="Osilasi dg Pegas",Position=True)


    create_simulation(t,X,Y,"Osilasi Pendulum sederhana")
    
