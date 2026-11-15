import httpx

print("Project A: My Website Checker")

response = httpx.get(
    "https://example.com",
    proxies="http://localhost:8080"
)

print(response.status_code)