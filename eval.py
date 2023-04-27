import requests
import concurrent.futures
import time
import matplotlib.pyplot as plt

def make_request():
    url = 'http://172.16.193.38:8080/fibo/5'
    response = requests.get(url)
    return response.status_code


urls = ['https://example.com/api/endpoint'] * 1000
with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
    futures = [executor.submit(make_request) for url in urls]
    responses = [future.result() for future in futures]
    concurrent.futures.wait(futures)

plt.hist(responses)
plt.show()
plt.savefig('histogram.png')