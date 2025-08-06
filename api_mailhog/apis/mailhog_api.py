import requests


class MailhogApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers



    def get_api_v2_messages(self, limit=50, **kwargs):
        params = {
            'limit': limit,
        }
        """
        Get Users emails
        """
        response = requests.get(url=f'{self.host}/api/v2/messages', params=params, verify=False, **kwargs)
        return response