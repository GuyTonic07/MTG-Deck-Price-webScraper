import random
import requests
from bs4 import BeautifulSoup




def get_deck_price(decklink):
    try:
        # Send a request to fetch the content of the page
        response = requests.get(decklink)
        
        if response.status_code == 200:
            # Parse the content of the page
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find the price element with the specific class
            price_element = soup.find('span', class_='deckPrice_orange__dSAUq')

            if price_element:
                price_text = price_element.text.strip()
                price = float(price_text[1:])  # Convert price text to float
                if price > 0:
                    return price  # Return the price if it's greater than zero
                else:
                    return None  # Return None for non-positive prices
            else:
                return None  # Price element not found
        else:
            return None  # Failed to fetch the webpage
    except Exception as e:
        return None  # An error occurred