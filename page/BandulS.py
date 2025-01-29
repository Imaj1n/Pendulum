import streamlit as st
import numpy as np
from scipy.integrate import solve_ivp
from VisualGraph import create_graph,create_simulation
from Formula import Harmonic_osci 

def teks1():
    st.subheader("Model Persamaan 📚")
    st.text('Untuk Model Persamaan pada bandul matematis sederhana dapat menggunakan Hukum Newton yaitu')
    st.latex(r'''
    \sum \tau_{\theta}=I\ddot{\theta} \\ 
    -mgl \sin{\theta}=ml^2 \frac{d^2 \theta}{dt^2} \\ 
    ''')
    st.text("menggunakan aproksimasi sin(θ) ≈ θ sehingga didapatkan hasil akhir")
    st.latex(r'''
    \frac{d^2 \theta}{dt^2}+\omega^2 \theta = 0 
    ''')
    st.text("Untuk mendapatkan solusi persamaan diferensial diatas, Transformasi bentuk persamaan menjadi")
    st.latex(r'''
    \frac{d\theta}{dt}=v_{\theta}\\ \frac{dv_{\theta}}{dt}=-\omega^2 \theta 
    ''')
    st.text("Untuk Solver persamaan ini menggunakan Library scipy dan bentuk kode python ODE diatas adalah")
    st.code(
    '''
    def harmonic_oscillator(t, y):
        theta, omega = y
        dthetadt = omega #theta
        domegadt = - (g/l)* theta #Pers Newton
        return [dthetadt, domegadt]
    # Kondisi awal: posisi theta(0) = 15, kecepatan v(0) = 0
    y0 = [15, 0.0]

    # Waktu yang akan dihitung
    t_span = (0, 10)  # dari t = 0 hingga t = 10
    t_eval = np.linspace(0, 10, 500)

    # Menyelesaikan persamaan diferensial
    solution = solve_ivp(harmonic_oscillator, t_span, y0, t_eval=t_eval)
    solution_theta = sol.y[0]
    solution_t = sol.t
    '''
    )

def app():
    
    st.title("Gerak Osilasi Pendulum💡")
    teks1()
    st.subheader("Solusi dan Visualisasi 🔬")
    g = st.slider("Percepatan Gravitasi ", 0.0, 100.0, 9.81)
    l = st.slider("Panjang tali", 0.0, 10.0, 5.0)
    harmonic_oscillator = Harmonic_osci(g,l)
    
    # Kondisi awal: posisi theta(0) = 1, kecepatan v(0) = 0
    y0 = [1.0, 0.0]

    # Waktu yang akan dihitung
    t_span = (0, 10)  # dari t = 0 hingga t = 10
    t_eval = np.linspace(0, 10, 500)

    # Menyelesaikan persamaan diferensial
    solution = solve_ivp(harmonic_oscillator, t_span, y0, t_eval=t_eval)

    theta = solution.y[0]
    t = solution.t
    # Plot hasilnya
    create_graph(t,theta)

    X = [l*np.sin(i) for i in theta]
    Y = [-l*np.cos(i) for i in theta]
    
    create_simulation(t,X,Y,"Osilasi Pendulum sederhana")
    
