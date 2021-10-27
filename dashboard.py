import streamlit as st
import requests
import urllib
from requests_html import HTMLSession
import pyperclip


def get_source(url):
    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except:
        pass


def get_results(query):

    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.com/search?q=" + query)

    return response


def scrape_google(query):

    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.com/search?q=" + query)

    links = list(response.html.absolute_links)
    google_domains = (
        "https://www.google.",
        "https://google.",
        "https://webcache.googleusercontent.",
        "http://webcache.googleusercontent.",
        "https://policies.google.",
        "https://support.google.",
        "https://maps.google.",
    )

    for url in links[:]:
        if url.startswith(google_domains):
            links.remove(url)

    return links


def parse_results(response):

    css_identifier_result = ".tF2Cxc"
    css_identifier_title = "h3"
    css_identifier_link = ".yuRUbf a"
    css_identifier_text = ".IsZvec"

    results = response.html.find(css_identifier_result)

    output = []

    for result in results:

        item = {
            "title": result.find(css_identifier_title, first=True).text,
            "link": result.find(css_identifier_link, first=True).attrs["href"],
            "text": result.find(css_identifier_text, first=True).text,
        }

        output.append(item)

    return output


def google_search(query):
    response = get_results(query)
    return parse_results(response)

def copyText(title_, link_, text_):
    pyperclip.copy("{}\n\n{}\n\n{}".format(title_, link_, text_))


st.sidebar.write("Sidabr this is",)
option = st.sidebar.selectbox("Which Dashboard?", ('Google Search', 'Twitter', 'Instagram', 'Facebook'))

if option == "Google Search":
    st.header("Google Search")
    st.subheader("Google Search for your content")

    search = st.text_input("Input search term here:",)
    output = google_search(search)
    for i, o in enumerate(output):
        st.write(o['title'])
        st.write(o['link'])
        st.write(o['text'])
        st.button('Copy Text', key=i, on_click=copyText(o['title'], o['link'], o['text']))
        st.write('--------------------------------')
        

if option == "Twitter":
    st.header("Twitter")
    st.subheader("Twitter Logic Dashboard")
    
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

    st.image('https://wie.ieee.org/wp-content/uploads/2019/06/twitter-logo-transparent-15.png',)

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