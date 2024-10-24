# profile_photos.py

from facebook_scraper import FacebookScraper

def main():
    rapidapi_key = "YOUR_RAPIDAPI_KEY"  # Replace with your RapidAPI key
    scraper = FacebookScraper(rapidapi_key)

    facebook_url = "https://www.facebook.com/zuck"
    data = scraper.retrieve_profile_photos(facebook_url)

    print(data)

if __name__ == "__main__":
    main()
