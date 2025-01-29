import streamlit as st
from streamlit_option_menu import option_menu
import BandulT,BandulS,BandulP,BandulG
import streamlit as st
# Set konfigurasi halaman Streamlit
st.set_page_config(
    page_title="Simulasi Bandul",
)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='Pendulum Problem',
                options=["Pendulum teredam","Pendulum sederhana","Pendulum dg Pegas","Pendulum Ganda"],
                menu_icon='chat-text-fill',
                icons=['chat-fill','house-fill','person-circle','info-circle-fill'],#,'trophy-fill','info-circle-fill'

                default_index=1,
        #         styles={
        #             "container": {"padding": "5!important","background-color":'black'},
        # "icon": {"color": "white", "font-size": "23px"}, 
        # "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        # "nav-link-selected": {"background-color": "#02ab21"},}      
                )
        if app=="Pendulum sederhana":
            BandulS.app()
        if app=="Pendulum teredam":
            BandulT.app()
        if app=="Pendulum dg Pegas":
            BandulP.app()
        if app=="Pendulum Ganda":
            BandulG.app()
    run()            
         