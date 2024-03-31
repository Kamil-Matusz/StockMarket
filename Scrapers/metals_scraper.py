import requests
from bs4 import BeautifulSoup
import csv

def get_metals_data():
    url = 'https://www.metals-api.com/symbols'
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        return None

def parse_metals_data(html_content):
    metals_data = []
    excluded_phrases = ['ask', 'am', 'pm', 'bid']
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
        table = soup.find("table", id="myTableMetals")
        if table:
            rows = table.find_all("tr")
            for row in rows[1:]:
                cells = row.find_all("td")
                if cells:
                    name = cells[0].text.strip()
                    symbol = cells[1].text.strip()
                    price = cells[2].text.strip()
                    if not any(phrase in name.lower() for phrase in excluded_phrases):
                        metals_data.append({'metal name': name, 'symbol': symbol, 'grammage': price})
    return metals_data

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['metal name', 'symbol', 'grammage']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def main():
    metals_content = get_metals_data()
    if metals_content:
        metals_data = parse_metals_data(metals_content)
        save_to_csv(metals_data, 'scraped_data/metals_data.csv')
        print("Dane zapisane do pliku metals_data.csv")
    else:
        print("Nie udało się pobrać danych z Metals API")

if __name__ == "__main__":
    main()
