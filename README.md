# StockMarket
Using the Neo4j graph database to represent elements and dependencies on stock exchanges and investment elements

## Stored data
- Investment funds
- NFT
- Cryptocurrencies
- Raw Materials
- Stock exchanges
- Types of exchanges
- Wallets

### Where was the data downloaded from?
Data was downloaded using scrapers written in Python. All available scrapers are available in the Scrapers directory. However, the downloaded data is stored in the scraped_data folder in csv files

### Project Launch
To run it, download it locally to your computer and run the main.py file. This will download data from the Internet and then import it into the Neo4j database. For everything to work properly, you must first create the Neo4j database and configure its settings.

## Importing a Database Dump into Neo4j

This guide outlines the steps to import a database dump file into Neo4j.

### Prerequisites

- Neo4j Server installed and running.
- Database dump file prepared in the appropriate format.

### Steps

1. **Prepare Dump File**: Ensure that your dump file is in the correct format and contains all necessary data.

2. **Start Neo4j Server**: Make sure the Neo4j server is running.

3. **Use neo4j-admin Tool**: Utilize the `neo4j-admin` tool available in Neo4j to import the data.

    Example command:
    ```
    neo4j-admin load --from=<path_to_dump_file> --database=<database_name> --force
    ```
    Where:
    - `<path_to_dump_file>` is the path to your dump file.
    - `<database_name>` is the name you want to give to the new database.
    - `--force` is an optional parameter that forces overwriting an existing database with the same name.

4. **Start the Database**: After importing the database, start it to apply all changes.

### Additional Notes

- Exact steps may vary depending on your Neo4j version and the format of your dump file.
- It's recommended to refer to the Neo4j documentation tailored to your version before performing the import.

## Nodes
![](/assets/ETFAsset.png)
![](/assets/CryptoAsset.png)
![](/assets/MetalAsset.png)
![](/assets/NFTAsset.png)
![](/assets/AssetType.png)
![](/assets/StockMarket.png)
![](/assets/StockMarketType.png)
![](/assets/Category.png)
![](/assets/Wallet.png)

## Relations
![](/assets/IS_CRYPTOCURRENCY.png)
![](/assets/IS_CRYPTOCURRENCY_EXCHANGE.png)
![](/assets/IS_METAL.png)
![](/assets/IS_METAL_EXCHANGE.png)
![](/assets/IS_ETF.png)
![](/assets/IS_STOCK_EXCHANGE.png)
![](/assets/IS_NFT.png)
![](/assets/IS_NFT.png)
![](/assets/SPECIALIZES_IN.png)
![](/assets/HAS_CATEGORY.png)
![](/assets/HIGH_RISK_WALLET.png)
![](/assets/LOW_RISK_WALLET.png)

## Database
![](/assets/Full-database.png)
