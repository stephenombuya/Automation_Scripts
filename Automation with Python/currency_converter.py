import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    return data['rates'][target_currency]

def convert_currency(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency, to_currency)
    converted_amount = amount * rate
    return converted_amount

# Example usage
amount = 100
from_currency = "USD"
to_currency = "EUR"

result = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")
