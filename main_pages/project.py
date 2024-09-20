import base64
def dataProject():
    with open("./assets/images/earthquake_nepal.jpg", "rb") as f:
        nepal = f.read()
        encoded = base64.b64encode(nepal)
        nepal = "data:image/png;base64," + encoded.decode("utf-8")

    with open("./assets/images/super.jpg", "rb") as ff:
        luanda = ff.read()
        encoded = base64.b64encode(luanda)
        luanda = "data:image/png;base64," + encoded.decode("utf-8")
    dataP ={
    "Earthquake in Nepal": [{"title":"Nepal",
                                                     "image_url":nepal,
                                                     "url":"","description":"Map Visualization"
                                                     }],
    "Graduate Admission Prediction": [{"title":"Regression Analysis",
                                                     "image_url":"https://images.unsplash.com/photo-1590012314607-cda9d9b699ae?auto=format&fit=crop&q=80&w=1171&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                                                     "url":"https://dsappcmse830.streamlit.app/","description":"Data Science"
                                                     }],
    "Enviromental Web Mapping Application": [{"title":"Hydrosimulatic Inc",
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
 