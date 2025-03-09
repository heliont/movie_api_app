import requests


# Cria uma classe que pode ser referenciado sempre que precisar de autenticação de token da API
class Auth:

    def __init__(self):
        self.__base_url = 'https://nt.pythonanywhere.com/api/v1/'
        self.__auth_url = f'{self.__base_url}authentication/token/'

    # Cria uma função para receber login e status code
    def get_token(self, username, password):
        auth_payload = {
            'username': username,
            'password': password
        }

        auth_response = requests.post(
            self.__auth_url,
            data=auth_payload
        )

        if auth_response.status_code == 200:
            return auth_response.json()
        return {'error': f'Erro ao autenticar. Status code: {auth_response.status_code}'}
