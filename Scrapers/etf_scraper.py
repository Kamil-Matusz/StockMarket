import requests
import csv

def get_etf_data(api_key):
    url = f"https://financialmodelingprep.com/api/v3/etf/list?apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Nie udało się pobrać danych.")
        return None

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['symbol', 'name', 'price', 'exchange', 'exchangeShortName', 'type']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for etf in data:
            writer.writerow({
                'symbol': etf['symbol'],
                'name': etf['name'],
                'price': etf['price'],
                'exchange': etf['exchange'],
                'exchangeShortName': etf['exchangeShortName'],
                'type': etf['type'],
            })

def main():
    api_key = "FPJTLjXAkKmijy2lwzPJ6ZOo8ur6Kgwp"
    etf_data = get_etf_data(api_key)
    if etf_data:
        save_to_csv(etf_data, 'scraped_data/etf_data.csv')
        print("Dane zapisane do pliku etf_data.csv")
    else:
        print("Nie udało się pobrać danych ETF.")

if __name__ == "__main__":
    main()
