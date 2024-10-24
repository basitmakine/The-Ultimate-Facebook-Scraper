# marketplace_item.py

from facebook_scraper import FacebookScraper

def main():
    rapidapi_key = "YOUR_RAPIDAPI_KEY"  # Replace with your RapidAPI key
    scraper = FacebookScraper(rapidapi_key)

    facebook_url = "https://www.facebook.com/marketplace/item/1030745568732697"
    data = scraper.get_marketplace_item(facebook_url)

    print(data)

if __name__ == "__main__":
    main()
