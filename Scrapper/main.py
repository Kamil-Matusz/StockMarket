import requests
import csv

def get_cryptocurrency_data():
    url = 'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=100&sortBy=market_cap&sortType=desc&convert=USD&cryptoType=all&tagType=all&audited=false'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['data']['cryptoCurrencyList']
    else:
        return None

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['name', 'symbol', 'price in USD']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in data:
            quotes = row.get('quotes', [])
            if quotes:
                quote = quotes[0]
                price = round(quote.get('price', 'N/A'), 2)
            else:
                price = 'N/A'
            writer.writerow({
                'name': row['name'],
                'symbol': row['symbol'],
                'price in USD': price
            })

def main():
    cryptocurrency_data = get_cryptocurrency_data()
    if cryptocurrency_data:
        save_to_csv(cryptocurrency_data, 'scraped_data/cryptocurrency_data.csv')
        print("Dane zapisane do pliku cryptocurrency_data.csv")
    else:
        print("Nie udało się pobrać danych z CoinMarketCap")

if __name__ == "__main__":
    main()
