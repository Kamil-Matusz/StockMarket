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
