import requests

request_url = 'https://www.instagram.com/p/Cy5rM0-L89t/'

result = requests.get(request_url).text

print(result)
