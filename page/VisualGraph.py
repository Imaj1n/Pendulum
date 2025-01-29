import plotly.graph_objects as go
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np

def create_graph(x,y,Nama="Osilasi Harmonis",Position=False,Double=False):
    plt.figure(figsize=(5, 3))
    if Position == True and Double==True: 
        x1,x2=x
        y1,y2=y
        plt.plot(x1, y1, label='Bandul 2', color='b')
        plt.plot(x2, y2, label='Bandul 1', color='r')
        plt.xlabel('Posisi x')
        plt.ylabel('Posisi y')
    if Double == True:
        x1,x2=x
        y1,y2=y
        plt.plot(x1, y1, label='Bandul 2', color='b')
        plt.plot(x2, y2, label='Bandul 1', color='r')
        plt.xlabel('Waktu (t)')
        plt.ylabel('Posisi (x)')
    if Position == True:
        plt.plot(x, y, label='Jalur Bandul', color='b')
        plt.xlabel('Posisi x')
        plt.ylabel('Posisi y')
    else:
        plt.plot(x, y, label='Posisi (x)', color='b')
        plt.xlabel('Waktu (t)')
        plt.ylabel('Posisi (x)')
    plt.title(Nama)
    plt.legend()
    plt.grid(True)
    plt.show()
    st.pyplot(plt)
        
def create_simulation(t,x,y,Nama,Double=False):
    if Double == True: 
        x1,x2=x
        y1,y2=y
        
        # Membuat plot awal
        xmax = max(x2)
        ymax = max(y2)
        l = (xmax**2+ymax**2)**(0.5)
        fig = go.Figure(
        data=[
            go.Scatter(x=[0, x1[0], x2[0]], 
                    y=[0, y1[0], y2[0]], 
                    mode='lines+markers', 
                    line=dict(color='blue', width=2), 
                    marker=dict(size=10))
        ],
        layout=go.Layout(
            title="Pendulum pegas",
            width=600,  # Menambahkan pengaturan lebar canvas
            height=600,  # Menambahkan pengaturan tinggi canvas
            xaxis=dict(range=[-l-0.5, l+0.5]),
            yaxis=dict(range=[-l-0.5, l+0.5]),
            showlegend=False,
            updatemenus=[dict(
                type="buttons",
                showactive=False,
                buttons=[dict(label="Play",
                            method="animate",
                            args=[None, dict(frame=dict(duration=0.00001, redraw=True), fromcurrent=True)]),
                        dict(
                        label="Stop",
                        method="animate",
                        args=[[None], dict(frame=dict(duration=0, redraw=True), mode='immediate', transition=dict(duration=0))]
                    )],     
                        )]
        ),
        frames=[
                go.Frame(
                    data=[
                        go.Scatter(x=[0, x1[k], x2[k]], y=[0, y1[k], y2[k]], mode='lines+markers', marker=dict(size=10, color='red'),showlegend=False)# Vektor bergerak
                    ],
                    name=str(k),
                    layout=go.Layout(
                        annotations=[
                            dict(
                                x=0.5, y=1.1, xref='paper', yref='paper', showarrow=False,
                                text=f"waktu: {t[k]:.2f}s", font=dict(size=20, color='black')
                            ),
                            dict(
                                x=0.98, y=0.95, xref='paper', yref='paper', showarrow=False,
                                text=f"sudut1: {np.arctan2(x1[k], y1[k]):.2f}", font=dict(size=20, color='black'),
                                align='right'
                            ),
                            dict(
                                x=0.98, y=0.85, xref='paper', yref='paper', showarrow=False,
                                text=f"sudut2: {np.arctan2(x2[k], y2[k]):.2f}", font=dict(size=20, color='black'),
                                align='right'
                            )
                        ]
                    )
                ) for k in range(len(t))
            ])

    else:
        # Membuat plot awal
        xmax = max(x)
        ymax = max(y)
        l = (xmax**2+ymax**2)**(0.5)
        fig = go.Figure(
            data=[
                go.Scatter(x=[x[0]], y=[x[0]], mode='markers', marker=dict(size=10, color='red'),showlegend=False),
                go.Scatter(x=[0, x[0]], y=[0, x[0]], mode='lines', line=dict(color='blue', width=2),showlegend=False),  # Vektor awal
            ],
            layout=go.Layout(
                title=Nama,
                width=600,
                height=700,
                xaxis=dict(range=[-l-0.5, l+0.5]),
                yaxis=dict(range=[-l-0.5, l+0.5]),
                showlegend=True,  # Mengaktifkan legend
                legend=dict(x=0.02, y=0.95),  # Posisi tetap di pojok kiri atas
                updatemenus=[dict(
                    type="buttons",
                    showactive=False,
                    buttons=[
                        dict(label="Play",
                            method="animate",
                            args=[None, dict(frame=dict(duration=0.0001, redraw=True), fromcurrent=True)]),
                        dict(label="Stop",
                            method="animate",
                            args=[[None], dict(frame=dict(duration=0, redraw=True), mode='immediate')])
                    ]
                )]
            ),
            frames=[
                go.Frame(
                    data=[
                        go.Scatter(x=[x[k]], y=[y[k]], mode='markers', marker=dict(size=10, color='red'),showlegend=False),
                        go.Scatter(x=[0, x[k]], y=[0, y[k]], mode='lines', line=dict(color='blue', width=2),showlegend=False),  # Vektor bergerak
                    ],
                    name=str(k),
                    layout=go.Layout(
                        annotations=[
                            dict(
                                x=0.5, y=1.1, xref='paper', yref='paper', showarrow=False,
                                text=f"waktu: {t[k]:.2f}s", font=dict(size=20, color='black')
                            ),
                            dict(
                                x=0.98, y=0.95, xref='paper', yref='paper', showarrow=False,
                                text=f"sudut: {np.arctan2(x[k], y[k]):.2f}", font=dict(size=20, color='black'),
                                align='right'
                            )
                        ]
                    )
                ) for k in range(len(t))
            ]
        )
    st.plotly_chart(fig)
        
