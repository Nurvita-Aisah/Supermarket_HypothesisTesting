import streamlit as st

class CollectiveApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({"title": title, "function":function})

    def run(self):
        app = st.selectbox(
            "Select a page",
            self.apps,
            format_func= lambda app: app['title']
        )

        app['function']()