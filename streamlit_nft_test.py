import streamlit as st
endpoint = st.sidebar.selectbox("Endpoints", ["Assets", "Events", "Rarity"])
st.write("Some text")
st.header(f"NFT API Explorer (Stratton Oakmont) - {endpoint}")
st.sidebar.write("Some sidebar text")
owner = st.sidebar.text_input("Owner")
collection = st.sidebar.text_input("Collection")