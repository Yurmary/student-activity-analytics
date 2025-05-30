import requests

def fetch_data_from_api():
    url = "https://b2b.itresume.ru/api/statistics"
    params = {
        "client": "Skillfactory",
        "client_key": "M2MGWS",
        "start": "2023-05-31 00:00:00.000000",
        "end": "2023-06-01 00:00:00.000000"
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Ошибка запроса: {response.status_code}")
        return 
