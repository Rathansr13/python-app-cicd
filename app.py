import requests
print("Hello from Jenkins Python job!")
response = requests.get("https://httpbin.org/get")
print("Status Code:", response.status_code)
