import requests
import csv

def get_exchange_data():
    url = 'https://api.coingecko.com/api/v3/exchanges'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'year_established', 'country']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for exchange in data:
            writer.writerow({
                'name': exchange['name'],
                'year_established': exchange.get('year_established', 'N/A'),
                'country': exchange.get('country', 'N/A')
            })

def main():
    exchange_data = get_exchange_data()
    if exchange_data:
        save_to_csv(exchange_data, 'scraped_data/cryptostockmarket_data.csv')
        print("Dane zapisane do pliku cryptostockmarket_data.csv")
    else:
        print("Nie udało się pobrać danych o giełdach z CoinGecko")

if __name__ == "__main__":
    main()
