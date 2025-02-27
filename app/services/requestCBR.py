import requests
from requests.exceptions import ConnectionError
from datetime import datetime

def requestCBR(date: datetime) -> str:
    """Fetches exchange rate data from the Central Bank of Russia."""
    date_req = date.strftime("%d/%m/%Y")
    url = f"https://www.cbr.ru/scripts/XML_daily.asp?date_req={date_req}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.HTTPError as e:
        raise ConnectionError(f"HTTP error occurred while fetching data: {e}")
    except requests.RequestException as e:
        raise ConnectionError(f"Network error occurred while fetching data: {e}")