# Facebook Scraper

A simple Python wrapper for the Facebook Scraper API available on [RapidAPI](https://rapidapi.com/taskagi-2-taskagi-2-default/api/facebook-scraper4/). This tool allows you to interact with Facebook Marketplace and Page data easily.

## Features

- Retrieve information of a specific Marketplace listing.
- Search Marketplace items by location.
- Search Marketplace items by keyword.
- Retrieve posts from a public Facebook page.
- Get information about a Facebook page.
- Retrieve post, engagement, and comment information from a post URL.
- Retrieve photos from a public Facebook profile.
- Retrieve information from a public Facebook profile.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Setup](#setup)
  - [Examples](#examples)
    - [Get Marketplace Item](#get-marketplace-item)
    - [Search Marketplace by Location](#search-marketplace-by-location)
    - [Search Marketplace by Keyword](#search-marketplace-by-keyword)
    - [Retrieve Page Posts](#retrieve-page-posts)
    - [Get Page About Information](#get-page-about-information)
    - [Retrieve Post Data](#retrieve-post-data)
    - [Retrieve Profile Photos](#retrieve-profile-photos)
    - [Retrieve Profile Data](#retrieve-profile-data)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/facebook-scraper.git
    cd facebook-scraper
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Setup

1. **Obtain a RapidAPI Key:**

   - Sign up or log in to [RapidAPI](https://rapidapi.com/).
   - Subscribe to the [Facebook Scraper API](https://rapidapi.com/your-api-link).
   - Get your unique `x-rapidapi-key`.

2. **Add Your RapidAPI Key:**

   - Open any of the example scripts in the `examples/` directory.
   - Replace `"YOUR_RAPIDAPI_KEY"` with your actual RapidAPI key.

### Examples

Each example script demonstrates how to use a specific endpoint. Below are instructions for each.

#### 1. Get Marketplace Item

Retrieve information of a specific Facebook Marketplace listing.

**Script:** `examples/marketplace_item.py`

```python
from facebook_scraper import FacebookScraper

def main():
    rapidapi_key = "YOUR_RAPIDAPI_KEY"  # Replace with your RapidAPI key
    scraper = FacebookScraper(rapidapi_key)

    facebook_url = "https://www.facebook.com/marketplace/item/1030745568732697"
    data = scraper.get_marketplace_item(facebook_url)

    print(data)

if __name__ == "__main__":
    main()
