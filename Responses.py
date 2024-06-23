import random
import requests
from bs4 import BeautifulSoup

##################################################### WebScrapper ###############################################
# URL of the Archidekt deck


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








##################################################### Quotes ###############################################
def get_response():
    quote_list = [
        'I think a lot about meteors...the purity of them. BOOM! The end. Start again. The world made clean for the new man to rebuild. I was meant to be new. I was meant to be beautiful. The world would have looked to the sky and seen hope...seen mercy. Instead, they will look up in horror because of you.',
        'There is a difference between you and me. We both looked into the abyss. But when it looked back at us… you blinked.',
        'and the universe said I love you',
        'You look like a calm and reasonable person',
        'incrediblis'
    ]
    return random.choice(quote_list)
