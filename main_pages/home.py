
import streamlit  as st
from config import styleSettings
from streamlit.components.v1 import html
# from pathlib import Path
from PIL import Image


def homepages():
    
    
    social = {"Linkedin":"https://www.linkedin.com/in/ezequiel-mussambe-089b51127/","Github":"https://github.com/EzequielMussambe37?tab=repositories","Facebook":"https://www.facebook.com/ezequielchipilica.ezequiel/","Instagram":"https://www.instagram.com/ezequielchipilica/"}
    column1, column2 = st.columns(2,gap="large")
    with open("./css/EzequielMussambe'sResume.pdf","rb") as pdf_file:
        pdfbyte = pdf_file.read()

    with column1:

        st.title("My name is Ezequiel Mussambe,GIS Analysis/Developer")
        st.write("""I design, develop and maintain Geographic Information Systems(GIS) applications and solutions.
            """)
        
        
        #  I leverage my expertise in spatial data analysis and programming to create a maps,application 
        #     and custom tools for solving real-world problems ,optimizing decisions for business,governments, 
        #     and organizations.
        
        
        
        

        # st.markdown(f"""
        #     <h2 {styleSettings.titles()}> Hello,<br> My name is Ezequiel,<br> GIS Analyst and Developer
        #     </h2>
        # """,unsafe_allow_html=True)
        
        
        # st.markdown(f"""
        #     <p {styleSettings.titles()}> I design, develop and maintain Geographic Information Systems(GIS) applications and solutions.
        #     I leverage my expertise in spatial data analysis and programming to create a maps,application 
        #     and custom tools for solving real-world problems ,optimizing decisions for business,governments, 
        #     and organizations.</p>""",unsafe_allow_html=True)
        column3, column4 = st.columns([2,2],gap="small")
        with column4:
            st.download_button(
                label="DOWNLOAD CV",
                data=pdfbyte,
                file_name="EzequielCV.pdf",
                mime="application/octet-stream",
            )
            st.markdown(""":email:  [Email Address](ezequielmussambe37@gmail.com)""",unsafe_allow_html=True)
            st.markdown("""	:telephone_receiver: +1517 455-3585""",unsafe_allow_html=True)
        
        # with column4:
        #     st.button('SEE MY PROJECTS', on_click=projects,args=('https://github.com/EzequielMussambe37?tab=repositories',))
    with column2:
        st.image("./images/ezequiel.png")
        
    st.markdown("""___""")   
    #st.write("##")
    cols = st.columns(len(social))
    for index, (media, link) in enumerate(social.items()):
        cols[index].write(f"[{media}]({link})")
def projects(url):
    open_script= f"""
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)