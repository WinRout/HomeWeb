import requests
from bs4 import BeautifulSoup
from typing import List, Dict
from config import SPITOGATOS_FILTERS, XE_FILTERS, QUERY_URL_SPITOGATOS, QUERY_URL_XE

# Headers for HTTP requests
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
}

def fetch_data(url: str, params: dict = None, parser: callable = None) -> List[Dict]:
    """Fetch data from a URL and parse it using the provided parser function."""
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        return parser(response) if parser else []
    except Exception as e:
        print(f"Error fetching or parsing data from {url}: {e}")
        return []

def parse_spitogatos(response: requests.Response) -> List[Dict]:
    """Parse Spitogatos API response into a list of property dictionaries."""
    data = response.json()
    return [{'id': str(prop['id']), 'modified': prop['modified'], 'url': f"https://www.spitogatos.gr/aggelia/11{prop['id']}"} for prop in data.get('data', [])]

def parse_xe(response: requests.Response) -> List[Dict]:
    """Parse XE HTML response into a list of property dictionaries."""
    soup = BeautifulSoup(response.text, 'html.parser')
    property_divs = soup.find_all('div', class_='common-ad')
    return [{
        'id': div.get('id'),
        'url': div.find('a', href=True)['href'],
        'modified': div.find('span', class_='common-ad-label').text.strip()
    } for div in property_divs if div.get('id') and div.find('a', href=True) and div.find('span', class_='common-ad-label')]