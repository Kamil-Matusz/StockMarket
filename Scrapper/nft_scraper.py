import requests
import csv

def get_nft_data():
    url = 'https://api.coingecko.com/api/v3/nfts/list?per_page=100&page=1'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'symbol', 'asset_platform']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for nft in data:
            writer.writerow({
                'name': nft['name'],
                'symbol': nft['symbol'],
                'asset_platform': nft['asset_platform_id']
            })

def main():
    nft_data = get_nft_data()
    if nft_data:
        save_to_csv(nft_data, 'scraped_data/ntf_data.csv')
        print("Dane zapisane do pliku ntf_data.csv")
    else:
        print("Nie udało się pobrać danych o NFT z CoinGecko")

if __name__ == "__main__":
    main()
