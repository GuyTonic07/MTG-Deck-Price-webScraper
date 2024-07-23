
import random
import requests
from bs4 import BeautifulSoup

##################################################### WebScrapper ###############################################


def get_deck_priceArch(decklink): #Archidekt Code
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
    
#################################################Tapped out################################################
    
def get_deck_price_tapped(decklink): # Tappedout Code
    try:
        # Send a request to fetch the content of the page
        response = requests.get(decklink)
        
        if response.status_code == 200:
            # Parse the content of the page
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all span elements with class 'pull-right'
            price_elements = soup.find_all('span', class_='pull-right')
            
            prices = []
            
            for element in price_elements:
                price_text = element.text.strip()
                
                # Split the price range if present
                price_range = price_text.split(' - ')
                
                if len(price_range) == 2:
                    min_price = price_range[0][1:]  # Remove the dollar sign
                    max_price = price_range[1][0:]  # Remove the dollar sign
                    prices.append((min_price, max_price))
                else:
                    base_price = price_range[0][1:]  # Remove the dollar sign
                    prices.append((base_price,))
            
            return prices
        else:
            return None  # Failed to fetch the webpage
    except Exception as e:
        print(f"An error occurred: {e}")
        return None  


##################################################### Quotes ###############################################
def get_response():
    quote_list = [
        'I think a lot about meteors...the purity of them. BOOM! The end. Start again. The world made clean for the new man to rebuild. I was meant to be new. I was meant to be beautiful. The world would have looked to the sky and seen hope...seen mercy. Instead, they will look up in horror because of you.',
        'There is a difference between you and me. We both looked into the abyss. But when it looked back at us… you blinked.',
        'and the universe said I love you',
        'You look like a calm and reasonable person',
        'incrediblis',
        'Do you know what type of animal waits for its own slaughter? sheep',
        "I want to buy you something, but I don't have any money",
        '4 pixels',
        'one second of eterity has passed',
        "Do not be sorry, be better",
        "What counts is not necessarily the size of the dog in the fight - it's the size of the fight in the dog",
        'you offer to the shrine but gain nothing',
        'Dude, sucking is the first step to being sorta good at something'
    ]
    return random.choice(quote_list)
