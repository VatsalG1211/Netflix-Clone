from locust import HttpUser, task, between

class APIUser(HttpUser):
    wait_time = between(1, 5)  # Simulates a wait time between requests

   
    # def login(self):
    #     """
    #     Simulates user login to get an authentication token or session cookie.
    #     """
    #     response = self.client.post("/account/login/", json={
    #         "username": "radharaman@gmail.com",
    #         "password": "radharani"
    #     })

    #     # response = self.client.get('/account/profile/28bd24c4-940b-4b20-a754-c4531b2039be/')
        
    #     # Assuming the response contains a token (JWT or session-based)
    #     if response.status_code == 200:
    #         self.token = response.json()["token"]  # Adjust according to your API's token format
    #         self.client.headers.update({
    #             "Authorization": f"Bearer {self.token}"
    #         })
    #     else:
    #         print(f"Login failed: {response.status_code}")

    # @task
    # def test_protected_api(self):
    #     """
    #     This method makes authenticated requests to the API after login.
    #     """
    #     response = self.client.get("/api/protected-endpoint/")
    #     if response.status_code == 200:
    #         print("Successfully accessed protected API!")
    #     else:
    #         print(f"Failed to access protected API: {response.status_code}")

    @task
    def get_content(self):
        self.client.get('/content/get_content/0ae469af2b5b465184124d13042616e9')

    @task
    def get_content2(self):
        self.client.get('/content/get_content/0ae468af2b5b465684123d13042616f3')

    @task
    def get_content3(self):
        self.client.get('/content/get_content/17657ae9-6c10-43ea-8c74-6a495ee665fc')