import streamlit  as st
from config import styleSettings
import streamlit.components.v1 as components
from streamlit_card import card
import base64

def hello():
    st.write("thiss is the file assssss")
def projectpages():
    column1,column2 = st.columns(2,gap="small")
    
    
    with column1:
        project_1() 
        project_3()  
    with column2:
        project_2() 
        project_4()

def project_1():
    
    with open("./images/earthquake_nepal.jpg", "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data)
        data = "data:image/png;base64," + encoded.decode("utf-8")
    nepal_project = card(
    title="Earthquake in Nepal",
    text="GIS Project",
    image=data
    )
    
def project_2():
    
    with open("./images/super.jpg", "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data)
        data = "data:image/png;base64," + encoded.decode("utf-8")
    luanda_project = card(
    title="Supermarket Accessibility in Luanda Capitol",
    text="Year of 2018",
    image=data
    )
    
def project_3():
    admission = card(
    title="Graduate Admission Prediction",
    text="School Project (2023)",
    image="",

    )
        
    # with open("./images/ezequiel.png", "rb") as f:
    #     data = f.read()
    #     encoded = base64.b64encode(data)
    #     data = "data:image/png;base64," + encoded.decode("utf-8")
    # hasClicked = card(
    # title="Graduate Admission Prediction",
    # text="School Project (2023)",
    # image=data
    # )
    
def project_4():
    
    crime = card(
    title="Crime in Chicago",
    text="Spatial Data Analysis",
    image="h",

    )
        
    # with open("./images/ezequiel.png", "rb") as f:
    #     data = f.read()
    #     encoded = base64.b64encode(data)
    #     data = "data:image/png;base64," + encoded.decode("utf-8")
    # hasClicked = card(
    # title="Crime in Chicago",
    # text="Spatial Data Analysis",
    # image=data)