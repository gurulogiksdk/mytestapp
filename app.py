import streamlit as st
from config import constants
from config import widget_key
from openai import OpenAI

from frontend.main_screen import main_UI
st.set_page_config(layout="wide")

st.title(constants.TITLE)
st.write(constants.WELCOME_MESSAGE)


def app():
    main_UI()



if __name__ == "__main__":
    if widget_key.OPEN_AI_CLIENT_OBJ not in st.session_state:
        with st.sidebar:
            st.write("Set OpenAI API")
            st.text_area("OpenAI API", key="API_KEY")
            
            but = st.button("Set Key")
            if but:
                st.session_state[widget_key.OPEN_AI_CLIENT_OBJ] = OpenAI(api_key=st.session_state["API_KEY"])
                st.session_state[widget_key.OPEN_AI_API_KEY_DATA] = st.session_state["API_KEY"]
                st.rerun()


    if widget_key.OPEN_AI_CLIENT_OBJ in st.session_state:
        app()
