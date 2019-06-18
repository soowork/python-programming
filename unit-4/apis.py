import requests
'''
response = requests.get('https://gitlab.com/dword4/nhlapi')

# this just gives <Response [200]>
print(response)
'''

# we want to get the actual data
# response = requests.get('https://xkcd.com/info.0.json')
response = requests.get('https://statsapi.web.nhl.com/api/v1/teams')

# some things about json
    # key must always be a string

# everything 
# print(response.json())

teams = response.json()['teams']
print(teams[0])