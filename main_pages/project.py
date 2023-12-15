# import streamlit  as st
# from config import styleSettings
# import streamlit.components.v1 as components
# from streamlit_card import card
import base64

# def hello():
#     st.write("thiss is the file assssss")
# def projectpages():
#     st.markdown("""<h2 style="text-align:center">Project Conducted</h2>""",unsafe_allow_html=True)
#     column1,column2 = st.columns(2,gap="small")
   
#     with column1:
#         st.subheader("DataNet Enviromental web mapping application")
#         st.markdown("""Date: 2020-2023: <span style="color:blue">Hydrosimulatic Inc</span>""",unsafe_allow_html=True)

#     with column2:
#         st.subheader("Graduate Admission Prediction Using Linear Regression Model")
#         st.markdown("""Date:2023: <span style="color:blue">Data Science</span>""",unsafe_allow_html=True)
    
#     st.markdown("___")
    
#     with column2:
#         st.subheader("Earthquake in Nepal")
#         st.markdown("""Date: 2018: <span style="color:blue">GIS Project</span>""",unsafe_allow_html=True)
    
    
#     with column1:
#         st.subheader("Supermarket Accessibility in Luanda Capitol")
#         st.markdown("""Date:2018: <span style="color:blue">Angola, Luanda</span>""",unsafe_allow_html=True)
    
    
#     with column1:
#         project_1() 
#         project_3()  
#     with column2:
#         project_2() 
#         project_4()

# def project_1():
    
#     with open("./assets/images/earthquake_nepal.jpg", "rb") as f:
#         data = f.read()
#         encoded = base64.b64encode(data)
#         data = "data:image/png;base64," + encoded.decode("utf-8")
#     nepal_project = card(
#     title="Earthquake in Nepal",
#     text="GIS Project",
#     image=data
#     )
    
# def project_2():
    
#     with open("./assets/images/super.jpg", "rb") as f:
#         data = f.read()
#         encoded = base64.b64encode(data)
#         data = "data:image/png;base64," + encoded.decode("utf-8")
#     luanda_project = card(
#     title="Supermarket Accessibility in Luanda Capitol",
#     text="Year of 2018",
#     image=data
#     )
    
# def project_3():
#     admission = card(
#     title="Graduate Admission Prediction",
#     text="School Project (2023)",
#     image="https://dsappcmse830.streamlit.app/",

#     )
        
    
# def project_4():
    
#     crime = card(
#     title="Crime in Chicago",
#     text="Spatial Data Analysis",
#     image="h",

#     )

def dataProject():
    with open("./assets/images/earthquake_nepal.jpg", "rb") as f:
        nepal = f.read()
        encoded = base64.b64encode(nepal)
        nepal = "data:image/png;base64," + encoded.decode("utf-8")
    
    # with open("https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1172&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", "rb") as f:
    #     nepal = f.read()
    #     encoded = base64.b64encode(nepal)
    #     nepal = "data:image/png;base64," + encoded.decode("utf-8")
        
        
    with open("./assets/images/super.jpg", "rb") as ff:
        luanda = ff.read()
        encoded = base64.b64encode(luanda)
        luanda = "data:image/png;base64," + encoded.decode("utf-8")
    dataP ={
    "Earthquake in Nepal": [{"title":"Nepal",
                                                     "image_url":nepal,
                                                     "url":"","description":"Map Analysis"
                                                     }],
    "Graduate Admission Prediction Using Linear Regression Model": [{"title":"Regression Analysis",
                                                     "image_url":"https://images.unsplash.com/photo-1590012314607-cda9d9b699ae?auto=format&fit=crop&q=80&w=1171&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                                                     "url":"https://dsappcmse830.streamlit.app/","description":"Data Science"
                                                     }],
    "DataNet Enviromental web mapping": [{"title":"Hydrosimulatic Inc",
                                                     "image_url":"https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1172&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                                                     "url":"","description":"Web Development"
                                                     }],
     "Steam Game Recommender": [{"title":"Steam Game Recommender",
                                                     "image_url":"https://images.unsplash.com/10/wii.jpg?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                                                     "url":"https://steamgamecse482.streamlit.app/","description":"Big Data Analysis"
                                                     }],
      "Supermarket Accessibility in Luanda Capitol": [{"title":"Luanda",
                                                     "image_url":luanda,
                                                     "url":"https://en.wikipedia.org/wiki/Luanda","description":"Network Analysis"
                                                     }],
       "Crime in Chicago City vs Housing Price": [{"title":"Chicago",
                                                     "image_url":"https://images.unsplash.com/photo-1581373449483-37449f962b6c?q=80&w=1169&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                                                     "url":"","description":"Spatial Data Analysis"
                                                     }]
    }

    return dataP
 