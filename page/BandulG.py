import streamlit as st
import numpy as np
from scipy.integrate import solve_ivp
from VisualGraph import create_graph,create_simulation
from Formula import Double_pendulum

def teks1():
    st.subheader("Model Persamaan 📚")
    st.text('Persamaan pada Double Pendulum diberikan dalam bentuk fungsi Lagrangian')
    st.latex(r'''
    L = \frac{1}{2} m_1 \left( L_1^2 \dot{\theta_1}^2 \right) + \frac{1}{2} m_2 \left( L_1^2 \dot{\theta_1}^2 + L_2^2 \dot{\theta_2}^2 + 2 L_1 L_2 \dot{\theta_1} \dot{\theta_2} \cos(\theta_1 - \theta_2) \right) \\
    - m_1 g L_1 \cos(\theta_1) - m_2 g \left( L_1 \cos(\theta_1) + L_2 \cos(\theta_2) \right)
    ''')
    st.text("Mengguanakan persamaan lagrangian euler pada fungsi diatas didapatkan solusi analitik ")
    st.latex(r'''
        \ddot{\theta}_1 = \frac{L_1 \left( 2m_1 + m_2 - m_2 \cos(2\theta_1 - 2\theta_2) \right)}{-\left(g(2m_1 + m_2) \sin(\theta_1) - m_2 g \sin(\theta_1 - 2\theta_2) \right)} \\
        - \frac{2 \sin(\theta_1 - \theta_2) m_2 \left( \dot{\theta}_2^2 L_2 + \dot{\theta}_1^2 L_1 \cos(\theta_1 - \theta_2) \right)}{-\left(g(2m_1 + m_2) \sin(\theta_1) - m_2 g \sin(\theta_1 - 2\theta_2) \right)}
        ''')

    st.latex(r'''
        \ddot{\theta}_2 = \frac{2 \sin(\theta_1 - \theta_2) \left( \dot{\theta}_1^2 L_1 (m_1 + m_2) + g (m_1 + m_2) \cos(\theta_1) + \dot{\theta}_2^2 L_2 m_2 \cos(\theta_1 - \theta_2) \right)}{L_2 \left( 2m_1 + m_2 - m_2 \cos(2\theta_1 - 2\theta_2) \right)}
        ''')
    st.text("bentuk persamaan diferensial ini ke dalam sistem persamaan")
    st.latex(r'''
        \frac{d\theta_1}{dt}= \omega_1 , \frac{d\theta_2}{dt}= \omega_2 \\
        \ddot{\theta}_1 = \frac{L_1 \left( 2m_1 + m_2 - m_2 \cos(2\theta_1 - 2\theta_2) \right)}{-\left(g(2m_1 + m_2) \sin(\theta_1) - m_2 g \sin(\theta_1 - 2\theta_2) \right)} \\
        - \frac{2 \sin(\theta_1 - \theta_2) m_2 \left( \omega_2^2 L_2 + \omega_1^2 L_1 \cos(\theta_1 - \theta_2) \right)}{-\left(g(2m_1 + m_2) \sin(\theta_1) - m_2 g \sin(\theta_1 - 2\theta_2) \right)}
        ''')

    st.latex(r'''
        \ddot{\theta}_2 = \frac{2 \sin(\theta_1 - \theta_2) \left( \omega_1^2 L_1 (m_1 + m_2) + g (m_1 + m_2) \cos(\theta_1) + \omega_2^2 L_2 m_2 \cos(\theta_1 - \theta_2) \right)}{L_2 \left( 2m_1 + m_2 - m_2 \cos(2\theta_1 - 2\theta_2) \right)}
        ''')
    st.text("dan bentuk kode nya sebagai berikut")
    st.code(
        '''
    def double_pendulum(t, z):
        theta1, omega1, theta2, omega2 = z
        delta = theta2 - theta1

        denom1 = (2*m1 + m2 - m2 * np.cos(2*delta))
        denom2 = (L2 / L1) * denom1

        d_omega1 = (-g * (2*m1 + m2) * np.sin(theta1) - m2 * g * np.sin(theta1 - 2*theta2) - 
                    2 * np.sin(delta) * m2 * (omega2**2 * L2 + omega1**2 * L1 * np.cos(delta))) / (L1 * denom1)

        d_omega2 = (2 * np.sin(delta) * (omega1**2 * L1 * (m1 + m2) + g * (m1 + m2) * np.cos(theta1) + 
                    omega2**2 * L2 * m2 * np.cos(delta))) / (L2 * denom2)

        return [omega1, d_omega1, omega2, d_omega2]    
    # Kondisi awal
    theta1_0 = np.pi / 4  # Sudut awal batang 1 (rad)
    theta2_0 = np.pi / 2  # Sudut awal batang 2 (rad)
    omega1_0 = 0.0        # Kecepatan sudut awal batang 1 (rad/s)
    omega2_0 = 0.0        # Kecepatan sudut awal batang 2 (rad/s)
    z0 = [theta1_0, omega1_0, theta2_0, omega2_0]

    # Waktu simulasi
    t_span = (0, 10)  # Dari 0 hingga 10 detik
    t_eval = np.linspace(t_span[0], t_span[1], 1000)  # Titik evaluasi

    # Simulasi dengan solve_ivp
    sol = solve_ivp(double_pendulum, t_span, z0, t_eval=t_eval, method='RK45')

    # Ekstraksi hasil
    theta1, theta2 = sol.y[0], sol.y[2]

    # Konversi ke koordinat kartesian
    x1 = L1 * np.sin(theta1)
    y1 = -L1 * np.cos(theta1)
    x2 = x1 + L2 * np.sin(theta2)
    y2 = y1 + L2 * np.cos(theta2)

    '''
    )
def app():
    
    st.title("Gerak Double Pendulum💡")
    teks1()
    st.subheader("Solusi dan Visualisasi 🔬")
    # Kondisi awal
    theta1_0 = np.pi / 4  # Sudut awal batang 1 (rad)
    theta2_0 = np.pi / 2  # Sudut awal batang 2 (rad)
    omega1_0 = 0.0        # Kecepatan sudut awal batang 1 (rad/s)
    omega2_0 = 0.0        # Kecepatan sudut awal batang 2 (rad/s)
    z0 = [theta1_0, omega1_0, theta2_0, omega2_0]

    # Waktu simulasi
    t_span = (0, 10)  # Dari 0 hingga 10 detik
    t_eval = np.linspace(t_span[0], t_span[1], 1000)  # Titik evaluasi
    g = st.slider("Percepatan Gravitasi ", 0.0, 100.0, 9.81)
    m1 = st.slider("Massa m1", 0.0, 50.0, 50.0)
    m2 = st.slider("Massa m2", 0.0, 50.0, 50.0)
    L1 = st.slider("Panjang tali 1", 0.0, 5.0, 1.0)
    L2 = st.slider("Panjang tali 2", 0.0, 5.0, 1.0)
    double_pendulum=Double_pendulum(g,m1,m2,L1,L2)
    # Simulasi dengan solve_ivp
    sol = solve_ivp(double_pendulum, t_span, z0, t_eval=t_eval, method='RK45')

    # Ekstraksi hasil
    theta1, theta2 = sol.y[0], sol.y[2]

    # Konversi ke koordinat kartesian
    x1 = L1 * np.sin(theta1)
    y1 = -L1 * np.cos(theta1)
    x2 = x1 + L2 * np.sin(theta2)
    y2 = y1 + L2 * np.cos(theta2)
    t = sol.t
    st.warning("Untuk kurva double pendulum masih dalam tahap pembuatan")
    # check_box = st.checkbox("Karena proses running visualisasi cukup lama, tekan tombol checkbox ini agar grafik dapat muncul dan tunggu beberapa saat")
    # if check_box :
    #     option = st.selectbox(
    #     "Visualisasi:",
    #     ("x terhadap t", "y terhadap x"),
    #     )
        
    #     if option == "x terhadap t":
    #         # create_graph(t,X,Nama="Osilasi dg Pegas")
    #         create_graph([t,x2],[t,x1],Nama="Double Pendulum",Double=True)
    #     if option == "y terhadap x":
    #         # create_graph(X,Y,Nama="Osilasi dg Pegas",Position=True)
    #         create_graph([x1,x2],[y1,y2],Nama="Double Pendulum",Double=True,Position=True)
    # else :
    #     pass
    create_simulation(t,[x1,x2],[y1,y2],"Osilasi Pendulum sederhana",Double=True)
    

