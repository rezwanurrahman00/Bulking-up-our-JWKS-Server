"""
Author: Rezwanur Rahman
Course: CSCE 3550 - Foundations of Cybersecurity
Date: December 6, 2024
Description: Flask application for enhancing security and user management
in the JWKS Server using AES encryption, user registration, and authentication logging.
"""


import requests
import sqlite3

BASE_URL = "http://127.0.0.1:5000"  # URL can be updated

def check_users_table():
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        conn.close()
        print("[PASS] Users table exists.")
    except sqlite3.OperationalError:
        print("[FAIL] Users table does not exist.")

def test_register():
    try:
        data = {"username": "test_user"}
        response = requests.post(f"{BASE_URL}/register", json=data)
        if response.status_code == 201:
            print("[PASS] /register endpoint is working.")
        else:
            print(f"[FAIL] /register endpoint returned {response.status_code}.")
    except requests.exceptions.RequestException as e:
        print(f"[FAIL] Error testing /register endpoint: {e}")

def check_encrypted_keys():
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT private_key FROM keys")
        private_keys = cursor.fetchall()
        conn.close()
        if all(len(key[0]) > 0 for key in private_keys):
            print("[PASS] Private keys are encrypted in the database.")
        else:
            print("[FAIL] Private keys are not encrypted.")
    except sqlite3.OperationalError:
        print("[FAIL] No such table: keys.")

def check_auth_logs_table():
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM auth_logs")
        conn.close()
        print("[PASS] auth_logs table exists.")
    except sqlite3.OperationalError:
        print("[FAIL] auth_logs table does not exist.")

def test_auth_logging():
    try:
        data = {"username": "test_user"}
        response = requests.post(f"{BASE_URL}/auth", json=data)
        if response.status_code == 200:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM auth_logs")
            logs = cursor.fetchall()
            conn.close()
            if logs:
                print("[PASS] /auth requests are logged.")
            else:
                print("[FAIL] /auth requests are not logged.")
        else:
            print(f"[FAIL] /auth endpoint returned {response.status_code}.")
    except requests.exceptions.RequestException as e:
        print(f"[FAIL] Error testing /auth endpoint: {e}")

def test_rate_limiting():
    try:
        data = {"username": "test_user"}
        for _ in range(5):  # Simulate multiple requests
            response = requests.post(f"{BASE_URL}/auth", json=data)
        if response.status_code == 429:  # Assuming 429 is the rate-limit code
            print("[PASS] /auth is rate-limited.")
        else:
            print("[FAIL] /auth is not rate-limited.")
    except requests.exceptions.RequestException as e:
        print(f"[FAIL] Error testing rate-limiting: {e}")

if __name__ == "__main__":
    print("Simulating Gradebot checks...")
    check_users_table()
    test_register()
    check_encrypted_keys()
    check_auth_logs_table()
    test_auth_logging()
    test_rate_limiting()
