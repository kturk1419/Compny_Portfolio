import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")


col1, cole1 = st.columns(2)
col2, cole2 = st.columns(2)
coll1, coll2 = st.columns(2)
col3, cole3, col4, cole4, col5 = st.columns([1, 0.5, 1, 0.5, 1])


with st.container():
    with col1:
        st.title("Khaled Turkestani")

    with cole1:
        st.empty()

with st.container():
    with col2:
        content = """
        Hi, I am Khaled! I am a Software Developer graduated from King Fahd University of Petroleum and Minerals. This website is didecated to show my projects developed using Python.
    I am currently working in King Fahd University of Petroleum and Minerals as a Developer, and a Banner AR Consultant.
        """
        st.write(content)

    with cole2:
        st.empty()


with st.container():
    with coll1:
        st.header("Our Team:")

    with coll2:
        st.empty()


with st.container():
    df = pd.read_csv("data.csv", sep=",")
    with col3:
        for i, row in df[:4].iterrows():
            name = row["first name"].title() + " " + row["last name"].title()
            st.subheader(name)
            st.write(row["role"])
            st.image("Images/" + row["image"])

    with cole3:
        st.empty()

    with col4:
        for i, row in df[4:8].iterrows():
            name = row["first name"].title() + " " + row["last name"].title()
            st.subheader(name)
            st.write(row["role"])
            st.image("Images/" + row["image"])

    with cole4:
        st.empty()

    with col5:
        for i, row in df[8:].iterrows():
            name = row["first name"].title() + " " + row["last name"].title()
            st.subheader(name)
            st.write(row["role"])
            st.image("Images/" + row["image"])
