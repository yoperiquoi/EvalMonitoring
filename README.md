# EvalMonitoring
To do the evaluation you will need 2 servers from the cluster ecotype in Nantes on G5K.

## To lanch the usecase:
On the first one we will be launching the Use Case:

```ssh
git clone https://github.com/yoperiquoi/EvalMonitoring.git
cd EvalMonitoring
g5k-setup-docker -t
docker-compose up --build
```

## To launch the evaluation:

On the second one we will be launching the locust for evaluation.
```ssh
git clone https://github.com/yoperiquoi/EvalMonitoring.git
cd EvalMonitoring
```

Activate the venv:
```ssh
source venv/bin/activate
````

Export an environnement variable corresponding to the use case adress on G5K:

```ssh
export USECASE_ADDRESS=ecotype-xx.nantes.grid5000.fr
```

Launch locust on the port 8080:

```ssh
locust -P 8080
```

You can now access the locust front from G5K proxy using your ecotype server and your credentials.
```
https://ecotype-xx.nantes.http8080.proxy.grid5000.fr/
```

You can configure your test for the load charge of the use case. (Note that 1 user is reserved to get electricty consumption from [seduce dashbord](https://hub.imt-atlantique.fr/seduce/grafana/d/TSY_RlpGz/seduce-project?orgId=1))
With current configuration in ```locustfile.py```:
- It requesting seduce dashboard to get server consumption with no trafic for 360 seconds.
- It wait for 120 seconds, then send ```Numbers of users - 1``` requests each ```seconds``` for 120 seconds then stop.
- To change the energy objective you will have to change the header in ```locustfile.py```: ```{"x-user-energy-objective": "xx"}```

This can be changed in the ```locustfile.py```.
![locust frontend](https://github.com/yoperiquoi/EvalMonitoring/blob/main/locust_front.jpg?raw=true)

You can push Start swarming to start the evaluation (be careful that your use case is ready.)

This will generate a ```response.csv``` and ```energy.csv``` file which can be used with the ```csv_eval/csv_plot.py``` script.
