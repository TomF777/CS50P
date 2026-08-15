"""
Implement a program that:

 - Expects the user to specify as a command-line argument the number of Bitcoins, 𝑛, that they would like to buy.
   If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.

 - Queries the API for the CoinCap Bitcoin Price Index at rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey.
   You should replace YourApiKey with the actual API key you obtained from your CoinCap account dashboard,
   which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float.

 - Outputs the current cost of 𝑛 Bitcoins in USD to four decimal places, using , as a thousands separator.
"""


# requires 'pip install requests'
import requests
import sys


# get number of bitcoins from command-line argument
try:
    num_bitcoins = float(sys.argv[1])
except IndexError:
    print("Missing command-line argument")
    sys.exit(1)
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)


# query the CoinCap API
try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=38abac4eb940725209d02adab56a32aece0589ae3a442246cab6b7c82681ad40")
    content = response.json()
    current_cost = float(content["data"]["priceUsd"]) * num_bitcoins
    print(f"${current_cost:,.4f}")
except requests.RequestException:
    print("error")
