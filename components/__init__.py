
import streamlit.components.v1 as components

_component_func = components.declare_component(
    "components",
    path="./components"
)

def projects(data):
    try:
        component_value = _component_func(spec = data, default = None)
        return component_value
    except:
        pass