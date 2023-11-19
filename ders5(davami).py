import requests


class GithubAccount:
    __url = 'https://api.github.com/users/'

    def __init__(self, username) -> None:
        self.username = username

    def send_requests(self):
        response = requests.get(f'{__url}{self.username}')
        if response.status_code == 200:
            response = response.json()
        elif response.status_code == 404:
            print(f'User not found with "{self.username}" username')
        else:
            return "Something went wrong"

    def get_full_name(self):
        response = self.send_requests()
        return response['name']


narmin = GithubAccount('mailovanarmin')
print(narmin.get_full_name())
