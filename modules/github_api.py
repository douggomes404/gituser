import requests

class GithubAPI:
    def __init__(self):
        pass
    
    def get_user_data(self, username):
        url = f"https://api.github.com/users/{username}"
        response = requests.get(url)
        if response.status_code != 200:
            return None
        return response.json()
    
    def get_user_repositories(self, username):
        url = f"https://api.github.com/users/{username}/repos"
        response = requests.get(url)
        if response.status_code != 200:
            return []
        return response.json()