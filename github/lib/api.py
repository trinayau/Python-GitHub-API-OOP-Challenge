import requests
from .repository import Repository

URL = 'https://api.github.com/users/'

def fetch_repos(username):
    ''' Call to GitHub API '''
    req = requests.get(URL + username + '/repos')
    for data in req.json():
        Repository(data)
    return data
