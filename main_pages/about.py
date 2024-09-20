
import streamlit  as st
from config import styleSettings

def aboutpages():
    # style="text-align:center;"
    st.markdown(f"""
            <h2> About Me
            </h2>
        """,unsafe_allow_html=True)
    st.markdown("___")
    column1, column2 = st.columns([.6,.4])
    
    with column1:
        st.markdown(f"""
                    <p style="text-align:center;">
                I earned my undergraduate degree in Geographic Information Science and Cartography, with a minor in Economics and Mathematics, from Michigan State University in December 2019. 
                Since then, I’ve gained over 3 years of industry experience. 
                In August 2023, I began my master’s program in Data Science at Michigan State University.
                My expertise includes GIS data analysis and development, with a strong background in geospatial analysis,
                data manipulation, and custom application development.
                </p>"""
                ,unsafe_allow_html=True)
    with column2:
        st.markdown(f"""
                    <div style="text-align:center;margin:10px;background-color: hsl(23, 100%, 65%); border-radius:5%;border: 2px solid black;">
                    <h3>My Expertise Includes</h3>
                    <p style="text-align:center">
                     Geospatial Data Management,
                     GIS Web Development,
                     Spatial Data Analysis, 
                     Data Visualization, GIS integration, 
                     Geospatial Problem Solving,
                    Data Modeling.
                    </p>
                    </div>
                    """,unsafe_allow_html=True)