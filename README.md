# CryptoScrape

## A simple web-scraper for gathering the latest crypto data from the CoinMarketCap Website.

### To run:

_Windows_ :

- set up a virtual environment with "python -m venv venv"
- activate the virtual environment with "source venv/Scripts/activate"
- install the frozen dependencies using "pip install -r requirements.txt"
- provide your mongodb uri "MONGO_URI" in a .env file in the root directory
- run the run_app.py script and check your database for a new collection with information on the current top 100 cryptocurrencies.
