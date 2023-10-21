
import streamlit  as st
from config import styleSettings
from streamlit.components.v1 import html


def homepages():

    column1, column2 = st.columns([.6,.4],gap="large")
    with open("./css/EzequielMussambe'sResume.pdf","rb") as pdf_file:
        pdfbyte = pdf_file.read()
    with column1:

        st.markdown(f"""
            <h2 {styleSettings.titles()}> Hello,<br> My name is Ezequiel,<br> GIS Analyst and Developer
            </h2>
        """,unsafe_allow_html=True)
        
        
        st.markdown(f"""
            <p {styleSettings.titles()}> I design, develop and maintain Geographic Information Systems(GIS) applications and solutions.
            I leverage my expertise in spatial data analysis and programming to create a maps,application 
            and custom tools for solving real-world problems ,optimizing decisions for business,governments, 
            and organizations.</p>""",unsafe_allow_html=True)
        
        column3, column4 = st.columns([.4,.6],gap="small")
        
        with column3:
            # st.markdown(""" div.stButton > button:first-child {
            #     background-color: #00cc00;color:white;}""", unsafe_allow_html=True)
            st.download_button(
                label="DOWNLOAD CV",
                data=pdfbyte,
                file_name="EzequielCV.pdf",
                mime="application/octet-stream",
            )
        with column4:
            st.button('SEE MY PROJECTS', on_click=projects,args=('https://github.com/EzequielMussambe37?tab=repositories',))
    with column2:
        st.image("./images/ezequiel.png")

def projects(url):
    open_script= f"""
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)