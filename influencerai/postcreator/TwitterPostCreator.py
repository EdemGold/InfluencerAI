import random
import string
from PIL import Image
from typing import Dict
import streamlit as st


####################################################
# Globals
####################################################

####################################################
# Functions
####################################################

def _build_layout():
    pass
    

@st.cache(allow_output_mutation=True)
def _get_static_store() -> Dict:
    """This dictionary is initialized once and can be used to store the files uploaded"""
    return {}


def twitter_char_limit(post):
    emojis = list(filter(lambda p: p.startswith(':') & p.endswith(':'), post.split()))
    for emoji in emojis:
        post = post.replace(emoji, ' ')
    # print(emojis, len(post))
    if len(post) <= 280:
        return True, len(post)
    else:
        return False, len(post)


def _preview_tweet(stColumn: st, tweet: string, static_store):
    for i, post in enumerate(tweet.split('\n\n\n')):
        charLimit, charLen = twitter_char_limit(post)
        if charLimit:
            stColumn.info("Post "+str(i+1)+" --- Char Length: "+str(charLen))
        else:
            stColumn.error("Post "+str(i+1)+" --- Char Length: "+str(charLen))
        for line in post.split('\n'):
            stColumn.markdown(line, unsafe_allow_html=True)
        selectedImgs = stColumn.multiselect("Select Images", static_store.keys(), key=str(i))
        for i in selectedImgs:
            stColumn.image(_load_image(static_store[i]), width=250)


def _load_image(image_file):
   img = Image.open(image_file)
   return img      


def clicked(postBtn, section):
    if postBtn:
        section.title("Hello")

####################################################
# Main function
####################################################


def twitter_postcreator_view():

    # Variables
    twitterPost = [] 
    static_store = _get_static_store()

    #####################################################################
    # Create sidebar
    st.sidebar.write("Sidbar this is",)

    #####################################################################
    # Create Title and Subtitle
    st.header("Twitter")

    subheaderRightCol, postToTwitterLeftCol = st.columns(2)
    subheaderRightCol.subheader("Twitter Post Creator")
    postBtn = postToTwitterLeftCol.button('Post to Twitter')

    #####################################################################
    # Create right column for writing post and left column for previewing post
    writePostTextAreaRightColumn, previewPostTextAreaLeftColumn = st.columns(2)
    tweet = writePostTextAreaRightColumn.text_area("Post", height=250)
    previewPostTextAreaLeftColumn.text("Preview")
    _preview_tweet(previewPostTextAreaLeftColumn, tweet, static_store)

    #####################################################################
    # Bottom section for uploading and previewing images
    st.subheader("Upload Images")

    con1 = st.container()
    narrowRightCol, wideLeftCol = con1.columns([1, 5])

    # Create photos uploader
    uploadedFile = wideLeftCol.file_uploader("Upload")

    # Extra spaces to center below buttons
    narrowRightCol.write(" ")
    narrowRightCol.write(" ")

    # Create buttons for clearing and showing uploaded photos
    clearUploadsBtn = narrowRightCol.button("Clear file list")
    showUploadsBtn = narrowRightCol.checkbox("Show content of files?")

    # Center column for diplaying the uploaded photos
    _, photoCenter, _ = st.columns(3)

    if uploadedFile:
        # Process you file here
        value = uploadedFile.getvalue()

        # And add it to the static_store if not already in
        if not uploadedFile in static_store.values():
            static_store[uploadedFile.name] = uploadedFile

    if clearUploadsBtn:
        static_store.clear()
    if showUploadsBtn:
        for img in static_store.values():
            photoCenter.image(_load_image(img), width=450)

   







