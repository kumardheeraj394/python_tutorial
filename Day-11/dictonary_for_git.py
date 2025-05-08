import requests

repo = "kubernetes/kubernetes"
url = f'https://api.github.com/repos/{repo}/pulls'
response = requests.get(url)
raw_data = response.json()
#print(raw_data)

for i in range(len(raw_data)):
    print(type(raw_data))
    
