from streamlit_option_menu import option_menu
from config import styleSettings
from main_pages import home,about,contact

def menu():
    menu_default = option_menu(
        menu_title = None,
        options=["Home","About", "Contact","Project"],
        icons=[" ","📊","📉","💻"],
        menu_icon = None,
        default_index=0,
        orientation="horizontal",
        styles= styleSettings.menuStyle()[0]
                )
    return menu_default



def menu_optionFuc():
    
    menu_options = {"Home":home.homepages,"About":about.aboutpages,"Contact":contact.contactpages}
    
    return menu_options