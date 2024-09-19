
import streamlit  as st
from config import styleSettings
from streamlit.components.v1 import html
# from pathlib import Path
from PIL import Image


def homepages():

    social = {"Linkedin":"https://www.linkedin.com/in/ezequiel-mussambe-089b51127/","Github":"https://github.com/EzequielMussambe37"}
    column1, column2 = st.columns(2,gap="large")
    with open("./assets/docs/EzequielMussambe'sResume.pdf","rb") as pdf_file:
        pdfbyte = pdf_file.read()

    with column1:

        st.title("Ezequiel Mussambe")
        st.write("""I am a data scientist with extensive experience in GIS analysis and GIS web development, gained through my education and work. 
                 I have worked on several data-driven and web application projects, 
                 developing APIs and responsive web applications that meet client requirements.
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
        with column3:
            st.download_button(
                label="DOWNLOAD CV",
                data=pdfbyte,
                file_name="EzequielCV.pdf",
                mime="application/octet-stream",
            )
            st.markdown(""":email:  [Email Address](ezequielmussambe37@gmail.com)""",unsafe_allow_html=True)
            st.markdown("""	:telephone_receiver: +1517 455-3585""",unsafe_allow_html=True)
        cols = st.columns(len(social))
        for index, (media, link) in enumerate(social.items()):
            cols[index].write(f"[{media}]({link})")
        # st.markdown("___")
        # with column4:
        #     st.button('SEE MY PROJECTS', on_click=projects,args=('https://github.com/EzequielMussambe37?tab=repositories',))
    with column2:
        st.image("./assets/images/ezequiel.png")

    st.markdown("""___""")
    st.markdown(f"""<h4 style="text-align:center;">Most Recent Work Experiences</h4>""",unsafe_allow_html=True)

    st.markdown(f"""<span class="meu-container"></span>""",unsafe_allow_html=True)
    st.markdown(f"""

        ##### GIS Analyst and GIS Developer
        Hydrosimulatics, Inc
        2020-2023
        * ✔️Process water wells data and classify lithologic materials (Boreholes lithology) using QGIS and Python 
        * ✔️Calculate borehole thickness of lithologic materials using Python scripts\QGIS  
        * ✔️Build a web mapping services web application to provide environmental georeferenced data around the world 
        * ✔️Manipulate and extract web mapping service data (web map services, web feature services and web coverage 
        services)
                """)
    
    st.markdown("""___""")
    st.markdown(f"""<spans class="meu-container"></spans>""",unsafe_allow_html=True) # trick and tips to make the boarder...
    st.markdown(f"""
        ##### Undergraduate GIS Research Assistant
        Landscape Ecology & Ecosystem Science Lab
        Summer 2019
        * ✔️Processed and orthorectified Ortho mosaic sub-watershed historical imagery for Landuse/Landcover classification.
        * ✔️Classified Landuse Landcover of  Kalamazoo Watershed by using eCognition
        * ✔️Georeferenced and Converted historical images into grayscale( python, Irfan view and Geo Setter)
        * ✔️Assisted in the maintenance of more than seven radiation towers in crops field to measure albedo and monitor crop health
        * ✔️Collected data on the height of vegetation, leaf area index, soil moisture, and nitrogen of biofuel crops and measured soil moisture """)
    
    

    
    # ======================================== end =====================
    # cols = st.columns(len(social))
    # for index, (media, link) in enumerate(social.items()):
    #     cols[index].write(f"[{media}]({link})")

    # st.markdown("___")
    # HtmlFile = open("./assets/cv.html", 'r', encoding='utf-8')
    # source_code = HtmlFile.read()
    # html(source_code)

    # columns1, columns2 = st.columns(2)
    
    # with columns1:
    #     st.subheader("Experience")
        

def projects(url):
    open_script= f"""
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)