import streamlit as st
import pandas as pd
from st_aggrid import AgGrid


actors = [
    {
        'id': 1,
        'name': 'Leonardo Di Caprio'
    },
    {
        'id': 2,
        'name': 'Chris Rock'
    },
    {
        'id': 3,
        'name': 'Stallone'
    },
]


def show_actors():
    st.write('Lista de Atores/Atrizes:')

    AgGrid(
        data=pd.DataFrame(actors),
        reload_data=True,
        key='actors_grid',

    )

    st.title('Cadastrar novo(a) Ator/Atriz')
    name = st.text_input('Nome do(a) Ator/Atriz')
    if st.button('Salvar'):
        # genres.append({'id': len(genres) + 1, 'name': name})
        st.success(f'Ator/Atriz "{name}" cadastrado(a) com sucesso!')
