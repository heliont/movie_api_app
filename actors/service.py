import streamlit as st
from actors.repository import ActorRepository


class ActorService:

    def __init__(self):
        self.actor_repository = ActorRepository()

    def get_actors(self):
        # Verifica se existe uma variavel em cache de sessão
        if 'actors' in st.session_state:
            return st.session_state.actors
        # caso não tenha variavel em cache faz nova busca
        actors = self.actor_repository.get_actors()
        # Salva na sessão para evitar busca novamente na próxima vez que a página for carregada
        st.session_state.actors = actors
        return actors

    def create_actor(self, name, birthday, nationality):
        actor = dict(
            name=name,
            birthday=birthday,
            nationality=nationality,
        )
        new_actor = self.actor_repository.create_actor(actor)
        st.session_state.actors.append(new_actor)
        return new_actor
