import requests


BASE_URL = "http://127.0.0.1:5000"  

# Test /register endpoint
try:
    print("Testing /register endpoint...")
    response = requests.post(
        f"{BASE_URL}/register",
        headers={"Content-Type": "application/json"},
        json={"username": "testuser", "email": "testuser@example.com"}
    )
    if response.ok:
        print("Register Response:", response.json())
    else:
        print("Register Response Error:", response.status_code, response.text)
except Exception as e:
    print("Error testing /register endpoint:", e)

# Test /auth endpoint
try:
    print("Testing /auth endpoint...")
    response = requests.post(
        f"{BASE_URL}/auth",
        headers={"Content-Type": "application/json"},
        json={"username": "testuser"}
    )
    if response.ok:
        print("Auth Response:", response.json())
    else:
        print("Auth Response Error:", response.status_code, response.text)
except Exception as e:
    print("Error testing /auth endpoint:", e)
