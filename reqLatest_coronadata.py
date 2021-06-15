import requests

url = "https://covid-19-data.p.rapidapi.com/totals"

headers = {
    'x-rapidapi-key': "7ad42b455bmshbe3207e3af9e693p13dd03jsnec374f2e8201",
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)