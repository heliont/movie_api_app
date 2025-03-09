import streamlit as st
from login.service import login


# Carrega a tela  de login
def show_login():
    st.title('Login')

    # Cria input para autenticação
    username = st.text_input('Usuário')
    password = st.text_input(
        label='Senha',
        type='password'
    )

    # Cria botão de login
    if st.button('Login'):
        login(
            username=username,
            password=password
        )