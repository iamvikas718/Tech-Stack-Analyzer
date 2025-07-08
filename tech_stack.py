import requests

def get_tech_stack(domain, api_key):
    url = "https://api.wappalyzer.com/v2/lookup/"
    headers = {"x-api-key": api_key}
    params = {"urls": domain}

    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return []
    except Exception as e:
        return []
