import json

data = {'people': []}
data['people'].append({
    'name': 'kyle',
    'username': '547113e07fe001c3366023bfdd091303a1f28aefa6e982ad2681a4a9548dd0cc',
    'password': '5527af79dba11bbe883d47586fb453cf6291e442dae011a40e410369f0958401',
    'accountNumber': '294495'
})

with open('accounts.txt', 'w') as outfile:
    json.dump(data, outfile)
