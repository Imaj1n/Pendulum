import streamlit as st
import numpy as np
from scipy.integrate import solve_ivp
from VisualGraph import create_graph,create_simulation
from Formula import Damped_Osci 

def teks1():
    
    st.subheader("Model Persamaan 📚")
    st.markdown("""
    Osilasi bandul yang teredam dapat dimodelkan dengan persamaan diferensial berikut:
    """)

    st.latex(r'''
    - bv_{\theta} - mgL \sin(\theta) = I \frac{d^2 \theta}{dt^2} 
    ''')
    st.latex(r'''
    I \frac{d^2 \theta}{dt^2} + bL \frac{d \theta}{dt} + mgL \sin(\theta) = 0
    ''')

    st.markdown("""
    Untuk bandul sederhana, kita dapat mendekati sin(θ) ≈ θ, sehingga persamaan geraknya menjadi:
    """)

    st.latex(r'''
    mL^2 \frac{d^2 \theta}{dt^2} + bL \frac{d \theta}{dt} + mgL \theta = 0
    ''')

    st.markdown("""
    Setelah disederhanakan, persamaan ini menjadi:
    """)

    st.latex(r'''
    \frac{d^2 \theta}{dt^2} + \frac{b}{mL} \frac{d \theta}{dt} + \frac{g}{L} \theta = 0
    ''')
    st.text('bentuk persamaan ini menjadi bentuk sistem persamaan diferensial')    
    st.latex(r'''
    \frac{d\theta}{dt}=v_{\theta}\\
    \frac{dv_{\theta}}{dt} = - \frac{b}{mL} v_{\theta} - \frac{g}{L} \theta = 0
    ''')
    st.text("dan Kode python untuk solusi dari persamaan ini adalah")
    st.code(
        '''
    def damped_oscillator(t, y):
        theta, omega = y
        dthetadt = omega
        domegadt = -(g/l)*theta - b/(m*l) * omega #Pers Newton
        return [dthetadt,domegadt]
    #Kondisi awal
    y0 = [1.0, 0.0]

    # Waktu yang akan dihitung
    t_span = (0, 30)  # dari t = 0 hingga t = 30
    t_eval = np.linspace(0, 30, 500)

    # Menyelesaikan persamaan diferensial
    solution = solve_ivp(damped_oscillator, t_span, y0, t_eval=t_eval)
    sol_theta = solutin.y[0]
    sol_t = solutin.t
    '''
    )
    # st.markdown("""
    # Solusi umum untuk persamaan ini adalah:
    # """)

    # st.latex(r'''
    # \theta(t) = \theta_0 e^{-\gamma t} \cos(\omega_d t + \phi)
    # ''')

    # st.markdown("""
    # Dengan:
    # - γ = b / (2mL) adalah laju redaman,
    # - ωₗ = √(g / L - γ²) adalah frekuensi osilasi teredam,
    # - θ₀ adalah amplitudo awal,
    # - φ adalah fase awal.
    # """)

def app():
    
    st.title("Gerak Osilasi Teredam💡")
    teks1()
    st.subheader("Solusi dan Visualisasi 🔬")
    g = st.slider("Percepatan Gravitasi ", 0.0, 100.0, 9.81)
    l = st.slider("Panjang tali", 0.0, 5.0, 1.0)
    m = st.slider("Massa beban", 0.00, 5.00, 0.50)
    b = st.slider("Koefisien gesek", 0.00, 1.00, 0.55)
    oscillator = Damped_Osci(g,l,m,b)
    
    # Kondisi awal: posisi theta(0) = 1, kecepatan v(0) = 0
    y0 = [1.0, 0.0]

    # Waktu yang akan dihitung
    t_span = (0, 10)  # dari t = 0 hingga t = 10
    t_eval = np.linspace(0, 10, 500)

    # Menyelesaikan persamaan diferensial
    solution2 = solve_ivp(oscillator, t_span, y0, t_eval=t_eval)

    theta2 = solution2.y[0]
    t2 = solution2.t
    # Plot hasilnya
    create_graph(t2,theta2)

    X = [l*np.sin(i) for i in theta2]
    Y = [-l*np.cos(i) for i in theta2]
    
    create_simulation(t2,X,Y,"Osilasi Pendulum sederhana")
    
