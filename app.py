import streamlit as st
from login.page import show_login
from genres.page import show_genres
from home.page import show_home
from actors.page import show_actors
from movies.page import show_movies
from reviews.page import show_reviews


def main():

    if 'token' not in st.session_state:
        show_login()
    else:
        st.title('Movie APP')

        menu_option = st.sidebar.selectbox(
            'Selecione uma opção',
            ['Início', 'Gêneros', 'Atores/Atrizes', 'Filmes', 'Avaliações']
        )

        if menu_option == 'Início':
            show_home()

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
