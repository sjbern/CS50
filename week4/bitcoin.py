import requests, sys, json

if len(sys.argv) == int(2):
    try:
        value = float(sys.argv[1])
    except:
        sys.exit("Command-line argument is not a number")
else:
    sys.exit("Wrong input")


try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    answer = response.json()
    btc = answer['bpi']['USD']['rate_float']
    adjPrice = btc * value
    print(f"${adjPrice:,.4f}") 
except requests.RequestException:
    sys.exit('Request Exception')

