from locust import HttpUser, task, constant
from locust.exception import StopUser
import socket
import time
import csv
import json
import os

# node informations
node = os.getenv('USECASE_ADDRESS')
node_short = node.split('.')[0]


# csv files management 
energy_file = open('energy.csv', 'w')
response_file = open('response.csv', 'w')
energy_writer = csv.writer(energy_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
response_writer = csv.writer(response_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
energy_writer.writerow(['time', 'energy', 'node'])
response_writer.writerow(['time', 'response', 'request', 'node'])

class ChargeLoad(HttpUser):
    host = "http://" + node + ":8080"
    first = True
    wait_time = constant(1)
    limit_time = time.time() + 240

    @task
    def fibonacci(self):
        if self.first is True :
            time.sleep(120)
            self.first = False
        if self.limit_time < time.time() :
            response_file.close()
            raise StopUser()
        with self.client.get(url='/fibo/5') as response:
            response_writer.writerow([time.time(), json.loads(response.content.decode('utf-8')) , response.request.url, node_short])
        

class EnergyMonitoring(HttpUser):
    wait_time = constant(1)
    fixed_count = 1
    limit_time = time.time() + 360


    host = 'https://hub.imt-atlantique.fr/seduce/grafana/api/datasources/proxy/1/query?db=mondb&q=SELECT%20mean(%22value%22)%20FROM%20%22sensors%22%20WHERE%20(%22sensor%22%20=~%20/' + node_short + '_pdu/)%20AND%20time%20%3E=%20now()%20-%2010s%20GROUP%20BY%20time(1s),%20%22sensor%22%20fill(0)&epoch=ms'
    @task
    def get_consumption(self):
        with self.client.get(url='/') as response:
            content = json.loads(response.content)
            energy_writer.writerow([time.time(), content['results'][0]['series'][0]['values'][-3][1], content['results'][0]['series'][0]['tags']['sensor']])
        if self.limit_time < time.time() :
            energy_file.close()
            raise StopUser()

