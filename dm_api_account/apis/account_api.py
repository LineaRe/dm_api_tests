import requests


class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers

    def post_v1_account(self, json_data, **kwargs):
        """
        Register new user
        :param json_data:
        :return:
        """
        response = requests.post(url=f'{self.host}/v1/account', json=json_data, **kwargs)
        return response


    def put_v1_account_token(self, token, **kwargs):

        """
        Activate registred user
        :param json_data:
        :return:
        """
        response = requests.put(url=f'{self.host}/v1/account/{token}', **kwargs)
        return response


    def put_v1_account_email(self, json_data, **kwargs):

        """
        Change registered user email
        :param json_data:
        :return:
        """
        response = requests.put(url=f'{self.host}/v1/account/email', json=json_data, **kwargs)
        return response
