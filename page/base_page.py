import requests


def get_status_code(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Failed to reach {url}. Error: {e}")
        return None
