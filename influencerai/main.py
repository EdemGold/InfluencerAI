# from core.Core import Core
import streamlit as st
from postcreator.TwitterPostCreator import twitter_postcreator_view

# """
#     Main class. Responsible for running the application.
# """


        


if __name__ == '__main__':
    # Main.run()
    st.set_page_config(layout="wide")
    st.sidebar.write("Sidabr this is",)
    pages = ['Google Search', 'Twitter', 'Instagram', 'Facebook']
    option = st.sidebar.selectbox("Which Dashboard?", (pages))

    if option == 'Google Search':
        st.title("G")

    elif option == 'Twitter':
        twitter_postcreator_view()
