

import json


with open('therapists_data.json', 'r') as f:
    content = json.load(f)

new_content = []

for entry in content:
    name, surname = entry['fields']["name"].split(',')
    new_content.append({
        'id': entry['pk'],
        "activity": entry['fields']["activity"],
        "inami_nb": entry['fields']["inami_nb"],
        "name": f'{surname.strip()} {name.strip()}',
        "address": entry['fields']["address"],
        "contracted": entry['fields']["contracted"],
    })

with open('therapists.json', 'w') as g:
    json.dump(new_content, g)
