# imports
import requests

response = requests.get("https://api.github.com") # consuming the API endpoint, making a GET request to the web server

print(response) # printing response

# printing success if the status code is okay
if response.status_code == 200:
    print("API connected successfully!")
    print(f"Response status code is:", response.status_code)
    print("Text:", response.text[:100])
    print("Actual data:", response.json())
else:
    print("Failed to connect API, try again later!")


# making another GET request
jsonplaceholder_response = requests.get("https://jsonplaceholder.typicode.com/posts")
print(jsonplaceholder_response.json()[:10])

