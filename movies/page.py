import streamlit as st
import pandas as pd
from st_aggrid import AgGrid



movies = [
    {
        'id': 1,
        'name': 'Interestelar'
    },
    {
        'id': 2,
        'name': 'Origem'
    },
    {
        'id': 3,
        'name': 'Sem Limites'
    },
]


def show_movies():
    st.write('Lista de Filmes')

    AgGrid(
        data=pd.DataFrame(movies),
        reload_data=True,
        key='movies_grid',

    )
