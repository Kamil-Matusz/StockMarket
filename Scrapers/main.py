import subprocess
import csv
from neo4j import GraphDatabase


def run_scripts(script_paths):
    for script_path in script_paths:
        print(f"Running script: {script_path}")
        try:
            subprocess.run(['python', script_path], check=True)
            print(f"Script {script_path} executed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while running script: {script_path}")
            print(e)


def import_crypto_data_to_neo4j(file_path):
    uri = "bolt://localhost:7687"
    username = "neo4j"
    password = "Qwerty123!"
    driver = GraphDatabase.driver(uri, auth=(username, password))

    with driver.session() as session:
        print(f"Importing cryptocurrency data from file: {file_path}")
        label = 'Crypto_Asset'
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                query = f'''
                    LOAD CSV WITH HEADERS FROM 'file:///{file_path}' AS row
                    CREATE (:{label} {{name: $name, symbol: $symbol, price: $price}})
                '''
                session.run(query, name=row['name'], symbol=row['symbol'], price=row['price'])
        print(f"Cryptocurrency data from file {file_path} imported to Neo4j.")


def import_stock_market_data_to_neo4j(file_path):
    uri = "bolt://localhost:7687"
    username = "neo4j"
    password = "Qwerty123!"
    driver = GraphDatabase.driver(uri, auth=(username, password))

    with driver.session() as session:
        print(f"Importing stock market data from file: {file_path}")
        label = 'StockMarket'
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                query = f'''
                    LOAD CSV WITH HEADERS FROM 'file:///{file_path}' AS row
                    CREATE (:{label} {{name: $name, yearEstablished: $yearEstablished, country: $country}})
                '''
                session.run(query, name=row['name'], yearEstablished=row['yearEstablished'], country=row['country'])
        print(f"Stock market data from file {file_path} imported to Neo4j.")


def import_metals_data_to_neo4j(file_path):
    uri = "bolt://localhost:7687"
    username = "neo4j"
    password = "Qwerty123!"
    driver = GraphDatabase.driver(uri, auth=(username, password))

    with driver.session() as session:
        print(f"Importing metals data from file: {file_path}")
        label = 'Metal_Asset'
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                query = f'''
                    LOAD CSV WITH HEADERS FROM 'file:///{file_path}' AS row
                    CREATE (:{label} {{name: $name, symbol: $symbol, grammage: $grammage}})
                '''
                session.run(query, name=row['name'], symbol=row['symbol'], grammage=row['grammage'])
        print(f"Metals data from file {file_path} imported to Neo4j.")


def import_nft_data_to_neo4j(file_path):
    uri = "bolt://localhost:7687"
    username = "neo4j"
    password = "Qwerty123!"
    driver = GraphDatabase.driver(uri, auth=(username, password))

    with driver.session() as session:
        print(f"Importing NFT data from file: {file_path}")
        label = 'NFT_Asset'
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                query = f'''
                    LOAD CSV WITH HEADERS FROM 'file:///{file_path}' AS row
                    CREATE (:{label} {{name: $name, symbol: $symbol, asset_platform: $asset_platform}})
                '''
                session.run(query, name=row['name'], symbol=row['symbol'], asset_platform=row['asset_platform'])
        print(f"NFT data from file {file_path} imported to Neo4j.")


def import_etf_data_to_neo4j(file_path):
    uri = "bolt://localhost:7687"
    username = "neo4j"
    password = "Qwerty123!"
    driver = GraphDatabase.driver(uri, auth=(username, password))

    with driver.session() as session:
        print(f"Importing ETF data from file: {file_path}")
        label = 'ETF_Asset'
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                query = f'''
                    LOAD CSV WITH HEADERS FROM 'file:///{file_path}' AS row
                    CREATE (:{label} {{name: $name, symbol: $symbol, price: $price, exchangeName: $exchangeName}})
                '''
                session.run(query, name=row['name'], symbol=row['symbol'], price=row['price'],
                            exchangeName=row['exchangeName'])
        print(f"ETF data from file {file_path} imported to Neo4j.")


def add_stock_market_types_to_neo4j():
    uri = "bolt://localhost:7687"
    username = "neo4j"
    password = "Qwerty123!"
    driver = GraphDatabase.driver(uri, auth=(username, password))

    with driver.session() as session:
        print("Adding StockMarketType nodes to Neo4j.")
        queries = [
            "CREATE (:StockMarketType {type: 'Stock Exchange'})",
            "CREATE (:StockMarketType {type: 'Cryptocurrency Exchange'})",
            "CREATE (:StockMarketType {type: 'Raw Materials Exchange'})"
        ]
        for query in queries:
            session.run(query)
        print("StockMarketType nodes added to Neo4j.")


def add_stock_markets_to_neo4j():
    uri = "bolt://localhost:7687"
    username = "neo4j"
    password = "Qwerty123!"
    driver = GraphDatabase.driver(uri, auth=(username, password))

    with driver.session() as session:
        print("Adding StockMarket nodes to Neo4j.")
        queries = [
            "CREATE (:StockMarket {name: 'XETRA', yearEstablished: '1997', country: 'Germany'})",
            "CREATE (:StockMarket {name: 'NASDAQ', yearEstablished: '1971', country: 'United States'})",
            "CREATE (:StockMarket {name: 'LSE', yearEstablished: '1801', country: 'United Kingdom'})",
            "CREATE (:StockMarket {name: 'AMEX', yearEstablished: '1850', country: 'United States'})",
            "CREATE (:StockMarket {name: 'TSX', yearEstablished: '1852', country: 'Canada'})",
            "CREATE (:StockMarket {name: 'SIX', yearEstablished: '1850', country: 'Swiss'})",
            "CREATE (:StockMarket {name: 'NYSE', yearEstablished: '1817', country: 'United States'})",
            "CREATE (:StockMarket {name: 'NYMEX', yearEstablished: '1882', country: 'United States'})",
            "CREATE (:StockMarket {name: 'LME', yearEstablished: '1887', country: 'United Kingdom'})",
            "CREATE (:StockMarket {name: 'SHFE', yearEstablished: '1999', country: 'China'})"
        ]
        for query in queries:
            session.run(query)
        print("StockMarket nodes added to Neo4j.")


def main():
    scripts_to_run = ['cryptocurrency_scraper.py', 'cryptostockmarket_scraper.py', 'metals_scraper.py',
                      'nft_scraper.py', 'etf_scraper.py']
    run_scripts(scripts_to_run)

    # Import data to Neo4j
    files_to_import = ['scraped_data/cryptocurrency_data.csv', 'scraped_data/cryptostockmarket_data.csv',
                       'scraped_data/metals_data.csv', 'scraped_data/nft_data.csv', 'scraped_data/etf_data.csv']
    for file_path in files_to_import:
        if 'cryptocurrency' in file_path:
            import_crypto_data_to_neo4j(file_path)
        elif 'cryptostockmarket' in file_path:
            import_stock_market_data_to_neo4j(file_path)
        elif 'metals' in file_path:
            import_metals_data_to_neo4j(file_path)
        elif 'nft' in file_path:
            import_nft_data_to_neo4j(file_path)
        elif 'etf' in file_path:
            import_etf_data_to_neo4j(file_path)

    add_stock_market_types_to_neo4j()

    add_stock_markets_to_neo4j()


if __name__ == "__main__":
    main()
