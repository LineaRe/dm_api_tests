import requests


class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers

    def post_v1_account(self, json_data):
        """
        Register new user
        :param json_data:
        :return:
        """
        response = requests.post(url=f'{self.host}/v1/account', json=json_data)
        return response


    def put_v1_account_token(self, token):
        headers = {
            'accept': 'text/plain'}
        """
        Activate registred user
        :param json_data:
        :return:
        """
        response = requests.put(url=f'{self.host}/v1/account/{token}', headers=headers)
        return response


    def put_v1_account_email(self, login, email, password):
        headers = {
            'accept': 'text/plain'
        }

        """
        Change registered user email
        :param json_data:
        :return:
        """

        json_data = {
            'login': login,
            'email': email,
            'password': password,
        }

        response = requests.put(url=f'{self.host}/v1/account/email', headers=headers, json=json_data)
        return response

