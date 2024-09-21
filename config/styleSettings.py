import streamlit as st
from streamlit_option_menu import option_menu

def hideConfigOption():

    st.set_page_config(
        page_title = "Ezequiel",
        
        layout="centered", 
    )
    
    with open("./assets/styles/shared.css") as f:
        st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)
    hide_style= """
    <style>
    #MainMenu {visibility:hidden;}
    header {visibility:hidden;}
    footer {visibility:hidden !important;}
    nav {visibility:hidden;}
    [data-testid="stToolbar"] {visibility:hidden !important;}
     .block-container {
                    padding-top: 2rem;
                    padding-bottom: 0rem;
                }
    </style>
    """
    st.markdown(hide_style, unsafe_allow_html=True)
    
def menuStyle():
    style = [
        {"container":{"padding":"4!import","background-color":"white","border-radius":'0'},
            "icon":{"color":'black',"font-size":'23px'},
            "nav-link":{"color":'black',"font-size":'20px',"text-align":'left',"margin":'0px',"--hover-color":'lightgrey'},
            "nav-link-selected":{"background-color":'#F2890C'},},
        


        ]  
    return style
#  title = """ style= "padding:10px; color:black;" """
    
def titles():
    
    title = """ style= "padding:0px; color:black;" """
    
    return title
def background_image():
    page_bg_img = """
        <style>
            [data-testid="stAppViewContainer"] {
                background-image: url("https://github.com/EzequielMussambe37/backgroundImage/blob/main/background.jpg?raw=true");
                background-size: cover;
                }
        </style>
        """
    element_container ="""
      
         <style>
            [data-testid="stVerticalBlock"] {
                # background-color:rgba(255,255,255);

                
                
                }
                
             button[title="View fullscreen"] {
        display: none;
    }

            [data-testid="stHorizontalBlock"] {
                padding:0px;
                margin:0px;
            }
           [data-testid="stImage"]  {
               
               object-fit: contain;
               border: 3px solid black;
               border-bottom-right-radius: 30%;
               border-top-left-radius: 30%;
               background-color: #F2890C;
           }
           
           
           
        [data-testid="stHorizontalBlock"]:has(span.meu-container){
            border: 1px solid grey;
        }
             [data-testid="element_container"] {
                 
             }
             
             .menu {
            
             }
        </style>
    """
    st.markdown(element_container, unsafe_allow_html=True)
    # st.markdown(page_bg_img, unsafe_allow_html=True)
    #  '''
    #     <style>
    #         body {
    #         background-image: url("../images/background.jpg");
    #         background-size: cover;
    #         }
    #     </style>
    #     '''