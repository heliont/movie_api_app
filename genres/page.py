import streamlit as st
import pandas as pd
from st_aggrid import AgGrid



genres = [
    {
        'id': 1,
        'name': 'Ação'
    },
    {
        'id': 2,
        'name': 'Comédia'
    },
    {
        'id': 3,
        'name': 'Terror'
    },
]


def show_genres():
    st.write('Lista de Gêneros')

    AgGrid(
        data=pd.DataFrame(genres),
        reload_data=True,
        key='genres_grid',

    )

    st.title('Cadastrar Gênero')
    name = st.text_input('Nome do Gênero')
    if st.button('Salvar'):
        # genres.append({'id': len(genres) + 1, 'name': name})
        st.success(f'Gênero "{name}" cadastrado com sucesso!')
