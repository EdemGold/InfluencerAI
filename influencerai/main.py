# from core.Core import Core
import streamlit as st
from postcreator import twitterpost

# """
#     Main class. Responsible for running the application.
# """


        


if __name__ == '__main__':
    # Main.run()
    st.sidebar.write("Sidabr this is",)
    pages = ['Google Search', 'Twitter', 'Instagram', 'Facebook']
    option = st.sidebar.selectbox("Which Dashboard?", (pages))

    if option == 'Google Search':
        st.title("G")

    elif option == 'Twitter':
        twitterpost.main_view()
