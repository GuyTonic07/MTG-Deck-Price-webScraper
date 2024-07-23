from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time


def get_deck_price_moxfield(decklink):
    driver = None  # Initialize driver variable
    try:
        # Set up Selenium WebDriver options
        options = Options()
        options.add_argument("--headless")  # Run in headless mode
        options.add_argument("--disable-gpu")  # Disable GPU acceleration
        options.add_argument("--window-size=1920,1080")  # Set window size for headless mode
        options.add_argument("--no-sandbox")  # Bypass OS security model
        options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
        
        # Automatically manage ChromeDriver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        
        # Navigate to the deck link
        driver.get(decklink)
        
        # Wait for the span element with id 'shoppingcart' to be present
        price_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'shoppingcart'))
        )
        
        if price_element:
            price_text = price_element.text.strip()
            
            # Remove the dollar sign
            price = price_text[1:] if price_text.startswith('$') else price_text
            
            return price
        else:
            return None  # No price element found
    except Exception as e:
        print(f"An error occurred: {e}")
        return None  # An error occurred
    finally:
        if driver:
            driver.quit()
            
            
def get_deck_price_deckstats(decklink):
    driver = None  # Initialize driver variable
    try:
        # Set up Selenium WebDriver options
        options = Options()
        options.add_argument("--headless")  # Run in headless mode
        options.add_argument("--disable-gpu")  # Disable GPU acceleration
        options.add_argument("--window-size=1920,1080")  # Set window size for headless mode
        options.add_argument("--no-sandbox")  # Bypass OS security model
        options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
        
        # Automatically manage ChromeDriver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        
        # Navigate to the deck link
        driver.get(decklink)
        
        # Wait for the span element with id 'shoppingcart' to be present
        price_element = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'deck_buy'))
        )
        
        
        price = None
        if price_element:
            for element in price_element:
                price_text = element.text.strip()
                if price_text.startswith('$'):
                    # Remove the dollar sign
                    price = price_text[1:]
                    break
                return price
        else:
            return None  # No price element found
    except Exception as e:
        print(f"An error occurred: {e}")
        return None  # An error occurred
    finally:
        if driver:
            driver.quit()
            


