import streamlit as st


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
        st.write('Lista de Gêneros')

    elif menu_option == 'Atores/Atrizes':
        st.write('Lista de Atores e Atrizes')
    elif menu_option == 'Filmes':
        st.write('Lista de Filmes')
    else:
        st.write('Avaliações dos Filmes')

if __name__ == '__main__':
    main()