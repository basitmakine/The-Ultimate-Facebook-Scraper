# marketplace_by_keyword.py

from facebook_scraper import FacebookScraper

def main():
    rapidapi_key = "YOUR_RAPIDAPI_KEY"  # Replace with your RapidAPI key
    scraper = FacebookScraper(rapidapi_key)

    facebook_url = "https://www.facebook.com/marketplace/austin/search/?query=helmet"
    data = scraper.search_marketplace_by_keyword(facebook_url)

    print(data)

if __name__ == "__main__":
    main()
