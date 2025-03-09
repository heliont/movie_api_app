import streamlit as st
from api.services import Auth


# Função de login para logar e verificar sessão
def login(username, password):
    auth_service = Auth()

    # Pega resposta do get_token de Auth
    response = auth_service.get_token(
        username=username,
        password=password
    )

    # Verifica se o login foi bem sucedido
    if response.get('error'):
        st.error(f'Falha ao realizar o login: {response.get('error')}')
    else:
        # Login com sucesso grava o token na session_state
        st.session_state.token = response.get('access')
        st.rerun()

