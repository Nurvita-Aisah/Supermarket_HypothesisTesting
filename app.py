import streamlit as st 
from collectiveapp import CollectiveApp
import visualization, hypothesis

st.set_page_config(
    page_title="Supermarket Sales Dashboard",
    page_icon="🧊",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/Nurvita-Aisah',
        'Report a bug': "https://github.com/Nurvita-Aisah",
        'About': "Supermarket Sales Dashboard"
    }
)

st.title("SUPERMARKET SALES DASHBOARD")
st.write("The main objective of this project is comparing the gross income of supermarket's branches")

app = CollectiveApp()

# Dashboard pages
app.add_app("Visualization Dashboard", visualization.App)
app.add_app("Hypothesis Testing Dashboard", hypothesis.App)

app.run()