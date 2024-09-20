
import streamlit  as st
from config import styleSettings
from streamlit.components.v1 import html
# from pathlib import Path
from PIL import Image
# gap="small"
def homepages():
    social = {"Linkedin":"https://www.linkedin.com/in/ezequiel-mussambe-089b51127/","Github":"https://github.com/EzequielMussambe37"}
    column1, column2 = st.columns(2)
    with open("./assets/docs/EzequielCV.pdf","rb") as pdf_file:
        pdfbyte = pdf_file.read()

    with column1:

        st.title("Ezequiel Mussambe")
        st.write("""I am a data scientist with extensive experience in GIS analysis and GIS web development, gained through my education and work. 
                 I have worked on several data-driven and web application projects, 
                 developing APIs and responsive web applications that meet client requirements.
            """)
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
    with column2:
        st.image("./assets/images/ezequiel.png",width=250)

    st.markdown("""___""")
    st.markdown(f"""<h4 style="text-align:center;">Most Recent Work Experiences</h4>""",unsafe_allow_html=True)

    # st.markdown(f"""<span class="meu-container"></span>""",unsafe_allow_html=True)
    st.markdown(f"""
        ##### GIS Analyst and GIS Developer
        Hydrosimulatics, 2020-2023

        Web Mapping Service Development
        * ✅ Led the development of a cutting-edge web mapping environment platform designed to provide environmental
        georeferenced data on a global scale. Utilized modern web technologies and GIS platforms and created an
        intuitive and user-friendly interface for accessing worldwide environmental geospatial data and enhanced user
        mapping and data visualization experience.
        * ✅ Manipulated and extracted data from various web mapping services (WMS), web features services (WFS), and
        web coverage services (WCS), and Web mapping tile services (WMTS) to support environmental and
        hydrological internal projects.
        
        """)
    st.markdown("""___""")
    # st.markdown(f"""<spans class="meu-container"></spans>""",unsafe_allow_html=True) # trick and tips to make the boarder...
    st.markdown(f"""
        ##### Undergraduate GIS Research Assistant
        Landscape Ecology & Ecosystem Science Lab, Summer 2019
    
        Data Processing and Classification
        * ✅ Utilized Pix4D and ArcGIS software for processing and orthorectification of sub-watershed historical imagery to
        use them for land use and land cover classification.
        * ✅ Employed eCognition software for advanced land cover and land use classification, contributing valuable insights
        to ecological research within the LEES Lab.
        * ✅ Developed efficient workflow for image processing, ensuring consistent and reliable data transformation.
        
        Field Work
        * ✅ Assisted in the maintenance and operation of over seven radiation towers in crop fields, measuring albedo and
        monitoring crop health to gather critical data for ecological studies.
        * ✅ Used GPS devices to conduct field surveys, identifying and collecting data from more than 30 plots within crop
        fields
        * ✅ Measured key parameters such as vegetation height, leaf area index, soil moisture, and nitrogen concentration
        levels to understand the photosynthetic activity and soil moisture and properties. Collaborated with researchers
        to interpret data and integrate findings into broader ecologic
        """)
    
    

    
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