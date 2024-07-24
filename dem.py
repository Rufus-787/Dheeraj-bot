import streamlit as st
st.set_page_config(page_icon="🎮")
st.title("Rufus Raj",anchor=False)
st.subheader("Gen AI Developer | Gamer")
with st.container(border=2):
    st.warning("I am a Student...........")
    st.info("I am a Gamer")
    col1, col2, col3=st.columns(3)
    with col1:
        with st.expander(label="know me more",expanded=False):
            st.info("hi............")
    with col2:
        st.image("formulaone.jpg")
    with col3:
        with st.expander(label="know me more",expanded=False):
            st.warning("Heloooooo......")