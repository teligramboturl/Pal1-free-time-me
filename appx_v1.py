import requests

def download_appx(url, token):
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        return resp.content
    else:
        raise Exception(f"Failed to fetch: {resp.status_code}")
