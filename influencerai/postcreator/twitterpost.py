import random
import string
from PIL import Image
from typing import Dict
import streamlit as st

@st.cache(allow_output_mutation=True)
def get_static_store() -> Dict:
    """This dictionary is initialized once and can be used to store the files uploaded"""
    return {}

def previewTweet(element_, tweet, static_store):
    #element_.text(tweet)
    for i, post in enumerate(tweet.split('\n\n\n')):
        element_.info("Post "+str(i+1))
        for line in post.split('\n'):
            element_.markdown(line, unsafe_allow_html=True)
        selectedImgs = element_.multiselect("Select Images", static_store.keys(), key=str(i))
        for i in selectedImgs:
            element_.image(load_image(static_store[i]), width=250)

def main_view():

    twitterPost = [] 

    st.sidebar.write("Sidabr this is",)

    st.header("Twitter")
    #c02.image('https://wie.ieee.org/wp-content/uploads/2019/06/twitter-logo-transparent-15.png', width=150)
    st.subheader("Twitter Post Creator")
    
    c1, c2 = st.columns(2)

    #postToTwitter = c2.button('Post to Twitter')

    #c2.subheader("Post Preview")
    
    tweet = c1.text_area("Post", max_chars=280, height=2)

    c2.text("Preview")

    st.subheader("Upload Images")
    static_store = get_static_store()

    con1 = st.container()
    c11, c12 = con1.columns([1,5])

    _, photoCenter, _ = st.columns(3)

    result = c12.file_uploader("Upload")
    c11.write(" ")
    c11.write(" ")
    if c11.button("Clear file list"):
        static_store.clear()
    if c11.checkbox("Show content of files?"):
        for img in static_store.values():
            photoCenter.image(load_image(img), width=450)

    if result:
        # Process you file here
        value = result.getvalue()

        # And add it to the static_store if not already in
        if not result in static_store.values():
            static_store[result.name] = result
    # else:
    #     static_store.clear()  # Hack to clear list if the user clears the cache and reloads the page
    #     st.info("Upload one or more `.py` files.")
    
    
    if tweet:
        previewTweet(c2, tweet, static_store)


