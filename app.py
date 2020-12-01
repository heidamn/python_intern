import requests


def is_alive_host(hostname):
    response = requests.get(hostname)
    return response.ok
