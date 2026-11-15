import httpx

print("Project B: My Website Checker")

response = httpx.get("https://example.com")

print(response.status_code)