# marketplace_by_location.py

from facebook_scraper import FacebookScraper

def main():
    rapidapi_key = "YOUR_RAPIDAPI_KEY"  # Replace with your RapidAPI key
    scraper = FacebookScraper(rapidapi_key)

    facebook_url = "https://www.facebook.com/marketplace/austin/"
    data = scraper.search_marketplace_by_location(facebook_url)

    print(data)

if __name__ == "__main__":
    main()
