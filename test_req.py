import requests
import json
from config import *
from pprint import pprint

print ('********************** Регистрация пользователя в системе Метод GET ********************************')

res = requests.get(f'{base_url}/user/login?username={username}&password={password}', headers=headers2)

print('Code = ', res.status_code)
print('Response body: ')
pprint(res.json(), width=40, indent=10)
print('Response headers: ')
pprint(dict(res.headers), indent=10)

print ('********************** Создание нового пользователя Метод POST ********************************')

info_js = json.dumps(new_user, ensure_ascii=False)

res = requests.post(f'{base_url}/user', headers=headers1, data=info_js)

print('Code  = ', res.status_code)
print('Response body: ')
pprint(res.json(), width=40, indent=10)
print('Response headers: ')
pprint(dict(res.headers), indent=10)

print ('********************** Измененение данных пользователя. Метод PUT ********************************')

username = new_user["username"]
info_js = json.dumps(updated_user, ensure_ascii=False)

res = requests.put(f'{base_url}/user/{username}', headers=headers1, data=info_js)

print('Code = ', res.status_code)
print('Response body: ')
pprint(res.json(), width=40, indent=10)
print('Response headers: ')
pprint(dict(res.headers), indent=10)

print ('********************** Удаление пользователя. Метод DELETE ********************************')


username = updated_user["username"]
res = requests.delete(f'{base_url}/user/{username}', headers=headers2)

print('Code = ', res.status_code)
print('Response body: ')
pprint(res.json(), width=40, indent=10)
print('Response headers: ')
pprint(dict(res.headers), indent=10)

print ('********************** Выход пользователя из системы. Метод GET ********************************')

res = requests.get(f'{base_url}/user/logout', headers=headers2)

print('Code = ', res.status_code)
print('Response body: ')
pprint(res.json(), width=40, indent=10)
print('Response headers: ')
pprint(dict(res.headers), indent=10)
