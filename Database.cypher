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


// Added AssetType

CREATE (:AssetType {type: 'ETF'}),
       (:AssetType {type: 'NFT'}),
       (:AssetType {type: 'Crypto'}),
       (:AssetType {type: "Metal"})

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








