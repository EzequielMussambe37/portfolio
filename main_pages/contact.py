import streamlit  as st
from config import styleSettings



def contactpages():

    st.markdown(f"""
                <h2 {styleSettings.titles()}>
                Contact
                </h2>
                <span {styleSettings.titles()}>
                <ul style="list-style: none;">
                    <li><b>EMAIL:</b> Ezequielmussambe37@gmail.com</li>
                    <li><b>ROLE:</b> GIS Analysis/Developer</li>
                    <li><b>PHONE:</b> +1517 455-3585</li>
                </ul>
                </span>
                """,unsafe_allow_html=True)

