import requests

def get_tech_stack(domain, api_key):
    url = "https://api.builtwith.com/free1/api.json"
    params = {"KEY": api_key, "LOOKUP": domain}
    resp = requests.get(url, params=params)
    if resp.status_code == 200:
        data = resp.json()
        groups = data.get("groups", [])
        techs = []
        for group in groups:
            for category in group.get("categories", []):
                techs.append(category["name"])
        return techs
    return []
