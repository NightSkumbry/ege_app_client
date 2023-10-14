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
    with open('data.json', 'wb') as f:
        f.write(response.content)

task()