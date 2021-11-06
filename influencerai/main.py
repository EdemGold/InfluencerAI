# from core.Core import Core
import streamlit as st
from postcreator.TwitterPostCreator import twitter_postcreator_view



if __name__ == '__main__':
    # Main.run()
    st.set_page_config(layout="wide")
    st.sidebar.write("Sidabr this is",)
    pages = ['Google Search', 'Twitter', 'Instagram', 'Facebook']
    option = st.sidebar.selectbox("Which Dashboard?", (pages))

    if option == 'Google Search':
        st.title("<--- Choose Twitter from the sidebar!")

    elif option == 'Twitter':
        twitter_postcreator_view()

    if option == "Instagram":
        st.header("Instagram")
        st.subheader("Instagram Logic Dashboard")
        st.image('https://i.imgflip.com/5puwup.jpg')

        st.write("""Hey there! Thanks for checking out this project! 
        Now, this is just the beginning of what I have planned for the future. 
        I really like python and I really like machine learning. 
        So, putting these two things together, I think we can create 
        a very interesting social media monitoring/content creation platform.""")

        st.write("If you want to follow along and see how this projects unfold, be sure to follow wherever you can!")
        st.write("Twitter:   https://twitter.com/dankornas")
        st.write("Instagram: https://www.instagram.com/dankornas")
        st.write("Facebook:  https://www.facebook.com/dankornas")

        st.write("Special thanks a full credit for original content search and thread creation mechanism goes to Pratham be sure to follow him as well! (https://twitter.com/PrasoonPratham)")

        st.image('https://clipground.com/images/instagram-logo-clear-background.png')

    if option == "Facebook":
        st.header("Facebook")
        st.subheader("Facebook Logic Dashboard")
        st.image('https://i.imgflip.com/5puwup.jpg')

        st.write("""Hey there! Thanks for checking out this project! 
        Now, this is just the beginning of what I have planned for the future. 
        I really like python and I really like machine learning. 
        So, putting these two things together, I think we can create 
        a very interesting social media monitoring/content creation platform.""")

        st.write("If you want to follow along and see how this projects unfold, be sure to follow wherever you can!")
        st.write("Twitter:   https://twitter.com/dankornas")
        st.write("Instagram: https://www.instagram.com/dankornas")
        st.write("Facebook:  https://www.facebook.com/dankornas")

        st.write("Special thanks a full credit for original content search and thread creation mechanism goes to Pratham be sure to follow him as well! (https://twitter.com/PrasoonPratham)")

        st.image('http://www.amjazzy.it/wp-content/uploads/2017/08/facebook-logo-png-9.png')
