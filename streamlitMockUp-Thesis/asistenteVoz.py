from streamlit_mic_recorder import speech_to_text
from langchain_openai import ChatOpenAI
import streamlit as st


openai_api_key="EstoEsUnaKeyFalsa usaUnaVerdadera"


llm= ChatOpenAI(model="gpt-4o", openai_api_key= openai_api_key)
st.title("tu asistente de Voz todo en uno")
st.write("Aplicacion de chat habilitada por voz")

text = speech_to_text(language="es", use_container_width= True, just_once=False, key="STT")

if text:
    st.write("Tu: ", text)
    response =llm.invoke(text)
    st.write("Respuesta del modelo: ", response.content)
