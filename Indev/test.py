import json
import pyperclip
import re

def var():
    import requests

    response = requests.get('https://kompege.ru/api/v1/variant/kim/25028749')

    print(response, type(response.content))
    with open('data.json', 'wb') as f:
        f.write(response.content)


def task(n=100870):
    import requests

    response = requests.get(f'https://kompege.ru/api/v1/task/{n}')

    print(response, type(response.content), response.content.decode())
    j = json.loads(response.content)
    with open('./Indev/data12473.json', 'w') as f:
        f.write(json.dumps(j, ensure_ascii=False, indent=4))
    h = j['text']
    pyperclip.copy(h)
    ha = re.findall(r'<a[^>]*?>[^<]*?</a>', h)
    for i in ha:
        h = h.replace(i, '')
    h = re.sub(r'<td [^>]*?(padding:[ ]*0px;)[^>]*?>', lambda m: m.group().replace(m.groups()[0], ''), h)
    h = re.sub(r'(\\\([ ]*?)', '<b><i>', h)
    h = re.sub(r'([ ]*?\\\))', '</i></b>', h)
    h = re.sub(r'\\to', '→', h)
    h = re.sub(r'\\lor', '∨', h)
    h = re.sub(r'\\neg', '¬', h)
    h = re.sub(r'\\land', '∧', h)
    h = re.sub(r'\\equiv', '≡', h)
    h = re.sub(r'_([^ ]+)', lambda m: f'<sub>{m.groups()[0].replace("}", "").replace("{", "")}</sub>', h)
    h = re.sub(r'\^([^ ]+)', lambda m: f'<sup>{m.groups()[0].replace("}", "").replace("{", "")}</sup>', h)
    h = re.sub(r'\\cdot', '⋅', h)
    h = re.sub(r'\\leq', '≤', h)
    h = re.sub(r'\\times', '×', h)
    h = re.sub(r'\\geq', '≥', h)
    
    
    with open('./Indev/data.html', "w") as f:
        f.write(h)
    
    

task(12473)