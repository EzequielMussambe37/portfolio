
import streamlit as st 

from config import menuSettings, styleSettings

from main_pages import home



class Profile:
    def __init__(self):
        self.name = "Ezequiel Mussambe"

    def runApp(self):
        
        # with st.sidebar:
        #     st.write("hhhhh")
       
        selected_menu = self.settings()
        print(selected_menu)
        self.pages(selected_menu)
        
       
        
    def settings(self):
        styleSettings.hideConfigOption()# need to be on the top
        column1,column2 = st.columns([.4,.69])
        with column2:
            selected= menuSettings.menu()
        styleSettings.background_image()

        return selected
    def pages(self, menu):
        menuSettings.menu_optionFuc()[menu]()

main = Profile()
main.runApp()
