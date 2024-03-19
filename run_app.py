from db import connectToMongo, closeConnection
from app import scrapeData

def InsertData(data: list):
    db = connectToMongo()
    collection = db["CoinMarketCapData"]
    collection.insert_many(data)
    closeConnection()
    
def main():
    data = scrapeData()
    InsertData(data)
    print("Data Scraped and Inserted to MongoDB")
    
if __name__ == "__main__":
    main()