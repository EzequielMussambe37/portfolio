
import streamlit  as st
from config import styleSettings

def aboutpages():
    
    st.markdown(f"""
            <h2>  About Me
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

        st.subheader("My expertise includes")
        
        st.write("""
                - ✔️ Geospatial Data Management
                - ✔️ GIS Software Development
                - ✔️ Spatial Data Analysis, 
                - ✔️ Data Visualization, GIS integration, 
                - ✔️ Geospatial Problem Solving
                 """)
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
