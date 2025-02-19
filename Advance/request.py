# Requests
''' It is one of the most downloaded package in python. This module is 
required to perform HTTP requests. '''

import requests

## Get Request
print('\n-------------------------------Get Request---------------------------\n')
response = requests.get('https://httpbin.org/get')
print('Status Code - ', response.status_code)
print(response.text)

## Get Request with Params
print('\n-------------------------------Get Request with params---------------------------\n')
param = {
    'name': 'Tanishqua',
    'job': 'Python Developer'
}

get_response = requests.get('https://httpbin.org/get', params=param)
print(get_response.url)

## Post Request
print('\n-------------------------------Post Request with payload---------------------------\n')
payload = {
    'name': 'Tanishqua',
    'job': 'Python Developer',
    'age': '21',
    'company': 'Simform'
}

post_response = requests.post('https://httpbin.org/post', data=payload)
print(post_response.json()['form'])

## Status Code
print('\n-------------------------------Status Code Handling---------------------------\n')
status_response = requests.get('https://httpbin.org/status/404')

if status_response.status_code == requests.codes.not_found:
    print('Not Found')
else:
    print('Status Code - ', response.status_code)

## User Agent
print('\n-------------------------------User Agent---------------------------\n')
header = {
    'User-Agent': 'TanishquaHello/1.43.0'
}
agent_response = requests.get('https://httpbin.org/user-agent', headers=header)

print(agent_response.text)

## Delayed Response
print('\n-------------------------------Delayed Response---------------------------\n')

delay_response = requests.get('https://httpbin.org/delay/3')
print(delay_response)

## Timeout - Throws exception when response takes longer time
print('\n-------------------------------Timeout---------------------------\n')

# timeout_response = requests.get('https://httpbin.org/delay/3', timeout=2) # Gives error
timeout_response = requests.get('https://httpbin.org/delay/1', timeout=2)
print(timeout_response)

## Proxy Servers
print('\n-------------------------------Proxy Servers---------------------------\n')

proxies = {
    'http': '47.250.51.110:8080',
    # 'https': '139.99.237.62:80'
    # 'http': '139.99.237.62:80'
}
proxy_response = requests.get('http://httpbin.org/get', proxies=proxies)
print(proxy_response.json())

## Get Img Request
print('\n-------------------------------Get Img Request---------------------------\n')
img_response = requests.get('https://imgs.xkcd.com/comics/compiler_complaint.png')
img_bytes = img_response.content

with open('images/comic.png', 'wb') as img:
    img.write(img_bytes)
    print('Comic image downloaded successfully')

## HTTP Auth
print('\n-------------------------------HTTP Auth---------------------------\n')
auth_response = requests.get('https://httpbin.org/basic-auth/tani/12345678', auth=('tani', '12345678'))
print(auth_response.text)