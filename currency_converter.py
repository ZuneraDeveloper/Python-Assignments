import requests

source_currency = input("Enter your source currency here: ").upper()
target_currency = input("Enter your desire currency here:").upper()

try:

    amount = float(input("Enter your amount to change: "))

except ValueError:

    print("Invalid amount! Please enter a number.")
    exit()

def exchange_rate(source_currency, target_currency, amount):

    url = f"https://open.er-api.com/v6/latest/{source_currency}"

    try:

        response = requests.get(url)

        response.raise_for_status()

        data = response.json()

    except requests.RequestException as e:

        print(f"Error fetching exchange rates: {e}")
        exit()

    try:

        rates = data["rates"][target_currency] # Example: Get the exchange rate for the desired currency

    except KeyError:

        print("Invalid currency. Please enter a valid currency code.")
        exit()

    converted_amount = amount * rates

    return converted_amount, rates


converted_amount, rates = exchange_rate(source_currency, target_currency, amount)

print(
    f"Your Source Currency: {source_currency}\n"
    f"Your Target Currency: {target_currency}\n"
    f"Your Amount: {amount}\n"
    f"Your Converted Amount: {converted_amount}\n"
    f"Your Exchange Rate: {rates}"
)