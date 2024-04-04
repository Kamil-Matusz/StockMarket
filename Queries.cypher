// Import CryptoCurrency from csv

LOAD CSV FROM 'file:///cryptocurrency_data.csv' AS row
CREATE (:Crypto_Asset {name: row[0],symbol: row[1], price: row[2]});

// Import NFT from csv

LOAD CSV FROM 'file:///ntf_data.csv' AS row
CREATE (:NFT_Asset {name: row[0],symbol: row[1], asset_platform: row[2]});

// Import ETF form csv

LOAD CSV FROM 'file:///etf_data.csv' AS row
CREATE (:ETF_Asset {name: row[1],symbol: row[0], price: row[2], exchangeName: row[4]});

// Import Metals from csv

LOAD CSV FROM 'file:///metals_data.csv' AS row
CREATE (:Metal_Asset {name: row[0],symbol: row[1], grammage: row[2]});

// Import CryptoCurrency Markets from csv

LOAD CSV FROM 'file:///cryptostockmarket_data.csv' AS row
CREATE (:StockMarket {name: row[0],yearEstablished: row[1], country: row[2]});

// Added AssetType

CREATE (:AssetType {type: 'ETF'}),
       (:AssetType {type: 'NFT'}),
       (:AssetType {type: 'Crypto'}),
       (:AssetType {type: "Metal"})

// Added StockMarketType

CREATE (:StockMarketType {type: 'Stock Exchange'}),
       (:StockMarketType {type: 'Cryptocurrency Exchange'}),
       (:StockMarketType {type: 'Raw Materials Exchange'})

// Added StockMarket

CREATE (:StockMarket {name: 'XETRA', yearEstablished: 1997, country: 'Germany'}),
       (:StockMarket {name: 'NASDAQ', yearEstablished: 1971, country: 'United States'}),
       (:StockMarket {name: 'LSE', yearEstablished: 1801, country: 'United Kingdom'}),
       (:StockMarket {name: 'AMEX', yearEstablished: 1850, country: 'United States'}),
       (:StockMarket {name: 'TSX', yearEstablished: 1852, country: 'Canada'}),
       (:StockMarket {name: 'SIX', yearEstablished: 1850, country: 'Swiss'}),
       (:StockMarket {name: 'NYSE', yearEstablished: 1817, country: 'United States'}),
       (:StockMarket {name: 'NYMEX', yearEstablished: 1882, country: 'United States'}),
       (:StockMarket {name: 'LME', yearEstablished: 1887, country: 'United Kingdom'}),
       (:StockMarket {name: 'SHFE', yearEstablished: 1999, country: 'China'})

// IS_CryptoCurrency

MATCH (asset:Crypto_Asset)
WHERE asset.price IS NOT NULL
MATCH (type:AssetType)
WHERE type.type = 'Crypto'
CREATE (asset)-[:IS_CRYPTOCURRENCY]->(type)

// IS_NFT

MATCH (asset:NFT_Asset)
WHERE asset.name IS NOT NULL
MATCH (type:AssetType)
WHERE type.type = 'NFT'
CREATE (asset)-[:IS_NFT]->(type)

// IS_ETF

MATCH (asset:ETF_Asset)
WHERE asset.name IS NOT NULL
MATCH (type:AssetType)
WHERE type.type = 'ETF'
CREATE (asset)-[:IS_ETF]->(type)

// IS_METAL

MATCH (asset:Metal_Asset)
WHERE asset.name IS NOT NULL
MATCH (type:AssetType)
WHERE type.type = 'Metal'
CREATE (asset)-[:IS_METAL]->(type)

// IS_CRYPTOCURRENCY_EXCHANGE

MATCH (asset:StockMarket)
WHERE asset.name IS NOT NULL
MATCH (type:StockMarketType)
WHERE type.type = 'Cryptocurrency Exchange'
CREATE (asset)-[:IS_CRYPTOCURRENCY_EXCHANGE]->(type)

// ALLOWS_TRADE_CRYPTOCURRENCIES

MATCH (asset:StockMarket)-[:IS_CRYPTOCURRENCY_EXCHANGE]->(type:StockMarketType {type: 'Cryptocurrency Exchange'})
CREATE (asset)<-[:ALLOWS_TRADE_CRYPTOCURRENCIES]-(type)

// IS STOCK_EXCHANGE

MATCH (asset:StockMarket)
WHERE asset.name IS NOT NULL
AND NOT (asset)-[:IS_CRYPTOCURRENCY_EXCHANGE]->()
MATCH (type:StockMarketType {type: 'Stock Exchange'})
CREATE (asset)-[:IS_STOCK_EXCHANGE]->(type)

// ALLOWS_TRADE_SHARES

MATCH (asset:StockMarket)-[:IS_STOCK_EXCHANGE]->(type:StockMarketType {type: 'Stock Exchange'})
CREATE (asset)<-[:ALLOWS_TRADE_SHARES]-(type)

// IS_METAL_EXCHANGE

MATCH (asset:StockMarket)
WHERE asset.name IN ['NYMEX', 'SHFE', 'LME']
MATCH (type:StockMarketType {type: 'Raw Materials Exchange'})
CREATE (asset)-[:IS_METAL_EXCHANGE]->(type)

// SPECIALIZES_IN

MATCH (a:AssetType {type: 'NFT'}), (t:StockMarketType {type: 'Cryptocurrency Exchange'})
CREATE (t)-[:SPECIALIZES_IN]->(a)

MATCH (a:AssetType {type: 'Crypto'}), (t:StockMarketType {type: 'Cryptocurrency Exchange'})
CREATE (t)-[:SPECIALIZES_IN]->(a)

MATCH (a:AssetType {type: 'Metal'}), (t:StockMarketType {type: 'Raw Materials Exchange'})
CREATE (t)-[:SPECIALIZES_IN]->(a)

MATCH (a:AssetType {type: 'ETF'}), (t:StockMarketType {type: 'Stock Exchange'})
CREATE (t)-[:SPECIALIZES_IN]->(a)

// ALLOWS_TRADE_METALS

MATCH (asset:StockMarket)-[:IS_METAL_EXCHANGE]->(type:StockMarketType {type: 'Raw Materials Exchange'})
CREATE (asset)<-[:ALLOWS_TRADE_METALS]-(type)

// 1:1 ALLOWS_TRADE_METALS

MATCH (asset:StockMarket)-[:ALLOWS_TRADE_METALS]-(type:StockMarketType)
RETURN asset, type
LIMIT 1 

// 1:1 ALLOWS_TRADE_CRYPTOCURRENCIES

MATCH (asset:StockMarket)-[:ALLOWS_TRADE_CRYPTOCURRENCIES]-(type:StockMarketType)
RETURN asset, type
LIMIT 1

// 1:1 ALLOWS_TRADE_SHARES

MATCH (asset:StockMarket)-[:ALLOWS_TRADE_SHARES]-(type:StockMarketType)
RETURN asset, type
LIMIT 1

// Count of Assets

MATCH ()-[r:IS_CRYPTOCURRENCY|IS_NFT|IS_ETF|IS_METALS]-()
RETURN
    type(r) AS Asset,
    COUNT(DISTINCT r) AS count

// List of Country

MATCH (market:StockMarket)
WHERE market.country IS NOT NULL
RETURN 
    DISTINCT market.country AS country,
    COUNT(*) AS count

// Metals grammage count

MATCH (metal: Metal_Asset)
WHERE metal.grammage IS NOT NULL
RETURN
    DISTINCT metal.grammage AS grammage,
    COUNT(*) AS count
