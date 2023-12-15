from streamlit_option_menu import option_menu
from config import styleSettings
from main_pages import home,about,project

def menu():
    menu_default = option_menu(
        menu_title = None,
        options=["Home","About","Project"],
        icons=[" ","📊","📉","💻"],
        menu_icon = None,
        default_index=0,
        orientation="horizontal",
        styles= styleSettings.menuStyle()[0]
                )
    return menu_default



def menu_optionFuc():
    
    menu_options = {"Home":home.homepages,"About":about.aboutpages,"Project":project.dataProject}
    
    return menu_options