import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    api_key = "TU_API_KEY_AQUI"
    url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey=5d5bda486154c3ef4d274f554fd0e9dd80dc2f55e88252e8c8355bbd639fffb6"
    response = requests.get(url)
    data = response.json()
    precio = float(data["data"]["priceUsd"])
    total = n * precio
    print(f"${total:,.4f}")
except requests.RequestException:
    sys.exit("Error accessing API")
