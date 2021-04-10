import spacy
import streamlit as st
from spacy import displacy
import wikipedia

st.header("Backend Task Assigned by Board Infinity") #defining Header

nlp = spacy.load('en_core_web_sm') #Loading Trained english pipeline

query = st.text_input("Search") #Making Search Bar using Streamlit

if st.button('Search'): #user clicks button
    if query == "":
        st.write("# Please Enter Something")  #user does'nt enter something   
    else:
        try:  #Loading content using Wikipedia API
            content = wikipedia.page(str(query)).content
        except wikipedia.DisambiguationError as e:
            randPage = random.choice(e.options)
            content  = wikipedia.page(randPage).content
        content = nlp(content) #Loading Content in Pipeline 
        annotatedText = displacy.render(content, style='ent')  #Performing NER
        st.write("# " + str(query)) 
        st.markdown(annotatedText, unsafe_allow_html=True) #Writing Annotated Text using streamlit