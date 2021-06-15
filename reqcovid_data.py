import requests

url = "https://covid-19-data.p.rapidapi.com/report/country/name"

querystring = {"date":"2020-04-01","name":"Norway"}

headers = {
    'x-rapidapi-key': "7ad42b455bmshbe3207e3af9e693p13dd03jsnec374f2e8201",
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)