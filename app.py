import requests
print("Hello from Jenkins Python job!")
response = requests.get("https://httpbin.org/get")
print("Status Code:", response.status_code)


def add(a,b):
    print(a+b)
    return a+b