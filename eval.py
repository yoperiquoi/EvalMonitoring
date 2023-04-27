import requests
import concurrent.futures
import time
import matplotlib.pyplot as plt

def make_request():
    url = 'http://172.16.193.38:8080/fibo/5'
    response = requests.get(url)
    data = response.json()
    return data


urls = ['https://example.com/api/endpoint'] * 1000
with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
    futures = [executor.submit(make_request) for url in urls]
    responses = [future.result() for future in futures]

plt.plot(responses)
plt.xlabel('Request Number')
plt.ylabel('Response Value')
plt.title('API Response Plot')
plt.show()