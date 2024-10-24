# post_data.py

from facebook_scraper import FacebookScraper

def main():
    rapidapi_key = "YOUR_RAPIDAPI_KEY"  # Replace with your RapidAPI key
    scraper = FacebookScraper(rapidapi_key)

    facebook_url = "https://www.facebook.com/melbournecarspotters/posts/pfbid0JGU22toEbeEevfmj4q1UJ1DWYs7NX2EPSBJiUNmbaTPUhDQiLLwegN7MxTBUoUKXl"
    data = scraper.retrieve_post_data(facebook_url)

    print(data)

if __name__ == "__main__":
    main()
