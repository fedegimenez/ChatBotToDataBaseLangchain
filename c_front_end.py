#To run the code you will need to install all the dependencies of the project and write streamlit run c_front_end.py in a terminal

import b_backend
import streamlit as st
from streamlit_chat import message

st.title("App Experto en tus Datos")
st.write("Preguntame lo que quieras sobre tus propios datos. Los analizaré y te contestaré")

if 'preguntas' not in st.session_state:
    st.session_state.preguntas = []
if 'respuestas' not in st.session_state:
    st.session_state.respuestas = []

def click():
    if st.session_state.user != '':
        pregunta = st.session_state.user
        respuesta = b_backend.consulta(pregunta)

        st.session_state.preguntas.append(pregunta)
        st.session_state.respuestas.append(respuesta)

        # Clean the user input
        st.session_state.user = ''


with st.form('my-form'):
   query = st.text_area('¿En qué te puedo ayudar?:', key='user', help='Pulsa Enviar para hacer la pregunta')
   submit_button = st.form_submit_button('Enviar',on_click=click)

if st.session_state.preguntas:
    for i in range(len(st.session_state.respuestas)-1, -1, -1):
        message(st.session_state.respuestas[i], key=str(i))

    # Option to continue the conversation
    continuar_conversacion = st.checkbox('Quieres hacer otra pregunta?')
    if not continuar_conversacion:
        st.session_state.preguntas = []
        st.session_state.respuestas = []









