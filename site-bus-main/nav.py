import requests
urlOAuth = 'https://as.api.iledefrance-mobilites.fr/api/oauth/token'
client_id='bus'
client_secret='pvIWslEjYJEeVTiUA6k6LT6mqHSBn4fH'

data =dict(
grant_type='client_credentials',
scope='read-data',
client_id=client_id,
client_secret=client_secret
)

response = requests.post(urlOAuth,data=data)
print(response.json)

if response.status_code != 200:
    print('Status:', response.status_code,
    'Erreur sur la requête; fin de programme')
exit()
    
jsonData = response.json()
token = jsonData['access_token']