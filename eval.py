from locust import HttpUser, task
class WebsiteUser(HttpUser): 
    
    @task 
    def fibonacci(self): 
        self.client.get(url='/fibo/5') 