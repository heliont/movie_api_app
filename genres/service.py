import streamlit as st
from genres.repository import GenreRepository


class GenreService:

    def __init__(self):
        self.genre_repository = GenreRepository()

    def get_genres(self):
        # Verifica se existe uma variavel em cache de sessão
        if 'genres' in st.session_state:
            return st.session_state.genres
        # caso não tenha variavel em cache faz nova busca
        genres = self.genre_repository.get_genres()
        # Salva na sessão para evitar busca novamente na próxima vez que a página for carregada
        st.session_state.genres = genres
        return genres

    def create_genre(self, name):
        genre = dict(
            name=name,
        )
        new_genre = self.genre_repository.create_genre(genre)
        st.session_state.genres.append(new_genre)
        return new_genre
