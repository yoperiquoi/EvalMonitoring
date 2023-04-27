import time
import requests
import datetime
import concurrent.futures

HOST = '172.16.193.9'
API_PATH = '/fib/5/'
ENDPOINT = HOST + API_PATH
MAX_THREADS = 4
CONCURRENT_THREADS = 3

def send_api_request():
    print ('Sending API request: ', ENDPOINT)
    r = requests.get(ENDPOINT)
    print ('Received: ', r.status_code, r.text)

start_time = datetime.datetime.now()
print ('Starting:', start_time)

with concurrent.futures.ThreadPoolExecutor(MAX_THREADS) as executor:
    futures = [ executor.submit(send_api_request) for x in range (CONCURRENT_THREADS) ]
time.sleep(5)
end_time = datetime.datetime.now()
print ('Finished start time:', start_time, 'duration: ', end_time-start_time)