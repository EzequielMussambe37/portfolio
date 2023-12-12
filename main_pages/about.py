
import streamlit  as st
from config import styleSettings

def aboutpages():
    
    st.markdown(f"""
            <h2>  About me
            </h2>
        """,unsafe_allow_html=True)
    
    column1, column2 = st.columns([.6,.4])
    
    with column1:
        st.markdown(f"""
                <p> I'm passionate and skilled Geographic Information Systems (GIS) Developer with a strong 
                dedication to leveraging cutting-edge technology and programming language to solve real-world spatial data challenges.
                Over the years, I have honed my skills in GIS development, and today, I consider myself a professional in the field.
                I have a strong background in geospatial analysis, data manipulation, and custom application development..</p>"""
                ,unsafe_allow_html=True)

        # st.markdown(f"""
        #     <p>My expertise includes: <b>Geospatial Data Management, GIS Software Development,
        #     Spatial Data Analysis, Data Visualization, GIS integration, 
        #     and Geospatial Problem Solving.</b></p>"""
        #         ,unsafe_allow_html=True)
    with column2:
        st.markdown(f"""
                    <div style="background-color: hsl(23, 100%, 65%);">
                    <h3>HELLO, I'M EZEQUIEL</h3>
                    <p>I am a versatile GIS Developer who can approach web 
                    mapping projects from a development to production.</p>
                    </div>
                    """,unsafe_allow_html=True)
        
    st.markdown("___")
    st.markdown(f"""<h4 style="text-align:center;">Most Recent Work Experience</h4>""",unsafe_allow_html=True)
    st.markdown(f"#")
    
    with st.container():
        
        column1, column2 = st.columns(2)
        
        with column1:
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
        with column2:
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
            
        
    st.markdown("___")
    st.markdown(f"""<h4 style="text-align:center;">My expertise includes</h4>""",unsafe_allow_html=True)
    # st.markdown(f"""<p class="meu-container"></p>""",unsafe_allow_html=True)
    st.write("""
                - ✔️ Geospatial Data Management
                - ✔️ GIS Software Development
                - ✔️ Spatial Data Analysis, 
                - ✔️ Data Visualization, GIS integration, 
                - ✔️ Geospatial Problem Solving
                 """)