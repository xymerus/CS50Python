import sys
import requests

try:

    if float(sys.argv[1]):
        bitcoin = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        bitcoin = bitcoin.json()["bpi"]["USD"]["rate_float"]
        number = float(sys.argv[1])
        usd = number * bitcoin
        print(f"${usd:,.4f}")


    else:
        sys.exit()

except IndexError:
    print("Missing command-line argument")
    exit()

except ValueError:
    print("Command-line argument is not a number")
    exit()



    