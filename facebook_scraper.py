# facebook_scraper.py

import requests

class FacebookScraper:
    def __init__(self, rapidapi_key):
        self.rapidapi_key = rapidapi_key
        self.base_url = "https://facebook-scraper4.p.rapidapi.com/api/social-media/facebook-scraper"

        self.headers = {
            "x-rapidapi-key": self.rapidapi_key,
            "x-rapidapi-host": "facebook-scraper4.p.rapidapi.com",
            "Content-Type": "application/json"
        }

    def get_marketplace_item(self, facebook_url):
        url = f"{self.base_url}/marketplace-item"
        payload = { "facebookUrl": facebook_url }

        response = requests.post(url, json=payload, headers=self.headers)
        return response.json()

    def search_marketplace_by_location(self, facebook_url):
        url = f"{self.base_url}/marketplace-items-by-location"
        payload = { "facebookUrl": facebook_url }

        response = requests.post(url, json=payload, headers=self.headers)
        return response.json()

    def search_marketplace_by_keyword(self, facebook_url):
        url = f"{self.base_url}/marketplace-items-by-keyword"
        payload = { "facebookUrl": facebook_url }

        response = requests.post(url, json=payload, headers=self.headers)
        return response.json()

    def retrieve_page_posts(self, facebook_url):
        url = f"{self.base_url}/page-posts"
        payload = { "facebookUrl": facebook_url }

        response = requests.post(url, json=payload, headers=self.headers)
        return response.json()

    def get_page_about_info(self, facebook_url):
        url = f"{self.base_url}/page-about"
        payload = { "facebookUrl": facebook_url }

        response = requests.post(url, json=payload, headers=self.headers)
        return response.json()

    def retrieve_post_data(self, facebook_url):
        url = f"{self.base_url}/post-data"
        payload = { "facebookUrl": facebook_url }

        response = requests.post(url, json=payload, headers=self.headers)
        return response.json()

    def retrieve_profile_photos(self, facebook_url):
        url = f"{self.base_url}/profile-photos"
        payload = { "facebookUrl": facebook_url }

        response = requests.post(url, json=payload, headers=self.headers)
        return response.json()

    def retrieve_profile_data(self, facebook_url):
        url = f"{self.base_url}/profile-data"
        payload = { "facebookUrl": facebook_url }

        response = requests.post(url, json=payload, headers=self.headers)
        return response.json()
