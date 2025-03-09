import streamlit as st
from genres.page import show_genres
from actors.page import show_actors
from movies.page import show_movies
from reviews.page import show_reviews


def main():
    st.title('Movie APP')

    menu_option = st.sidebar.selectbox(
        'Selecione uma opção',
        ['Início', 'Gêneros', 'Atores/Atrizes', 'Filmes', 'Avaliações']
    )

    if menu_option == 'Início':
        st.subheader('Bem-vindo ao Movie App!')
        st.text('Este é um app de visualização de filmes, gêneros, atores/atrizes e avaliações.')

    elif menu_option == 'Gêneros':
        show_genres()

    elif menu_option == 'Atores/Atrizes':
        show_actors()

    elif menu_option == 'Filmes':
        show_movies()

    else:
        show_reviews()


if __name__ == '__main__':
    main()
