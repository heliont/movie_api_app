import streamlit as st
from movies.repository import MovieRepository


class MovieService:

    def __init__(self):
        self.movie_repository = MovieRepository()

    def get_movies(self):
        # Verifica se existe uma variavel em cache de sessão
        if 'movies' in st.session_state:
            return st.session_state.movies
        # caso não tenha variavel em cache faz nova busca
        movies = self.movie_repository.get_movies()
        # Salva na sessão para evitar busca novamente na próxima vez que a página for carregada
        st.session_state.movies = movies
        return movies

    def create_movie(self, title, genre, release_date, actors, resume):
        movie = dict(
            title=title,
            genre=genre,
            release_date=release_date,
            actors=actors,
            resume=resume,
        )
        new_movie = self.movie_repository.create_movie(movie)
        st.session_state.movies.append(new_movie)
        return new_movie

    def get_movie_stats(self):
        return self.movie_repository.get_movie_stats()