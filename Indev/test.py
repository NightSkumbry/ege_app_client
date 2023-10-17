import json
import pyperclip
import re

def var():
    import requests

    response = requests.get('https://kompege.ru/api/v1/variant/kim/25028749')

    print(response, type(response.content))
    with open('data.json', 'wb') as f:
        f.write(response.content)


def task():
    import requests

    response = requests.get('https://kompege.ru/api/v1/task/10084')

    print(response, type(response.content))
    j = json.loads(response.content)
    h = j['text']
    h = re.sub(r'<td [^>]*?(padding: 0px;)[^>]*?>', lambda m: m.group().replace(m.groups()[0], ''), h)
    
    with open('./Indev/data.html', "w") as f:
        f.write(h)
    pyperclip.copy(h)
    

task()