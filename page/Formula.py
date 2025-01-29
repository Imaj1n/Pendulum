import numpy as np

def Harmonic_osci(g,l):
    #################################
    def harmonic_oscillator(t, y):
        theta, omega = y
        dthetadt = omega #theta
        domegadt = - (g/l)* theta #Pers Newton
        return [dthetadt, domegadt]
    #################################
    return harmonic_oscillator

def Damped_Osci(g,l,m,b):
    #################################
    def damped_oscillator(t, y):
        theta, omega = y
        dthetadt = omega
        domegadt = -(g/l)*theta - b/(m*l) * omega #Pers Newton
        return [dthetadt,domegadt]
    #################################
    return damped_oscillator

def Spring_Osci(g,L,m,k):
    #################################
    def pendulum_spring(t, z):
        x, vx, y, vy = z
        r = (x**2 + y**2)**(0.5)  # Panjang pegas saat ini
        F_spring = k * (r - L)  # Gaya pegas
        ax = -F_spring * (x / r) / m  # Percepatan di arah x
        ay = -F_spring * (y / r) / m - g  # Percepatan di arah y
        return [vx, ax, vy, ay]
    #################################
    return pendulum_spring

def Double_pendulum(g,m1,m2,L1,L2):
    #################################
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
    #################################
    return double_pendulum