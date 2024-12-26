from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def capture_screenshot(url, filename):
    # Set up Chrome options for headless mode
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    
    # Initialize the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    try:
        # Navigate to the URL
        driver.get(url)
        
        # Wait for the page to load (you might need to adjust this)
        time.sleep(5)
        
        # Capture the screenshot
        driver.save_screenshot(filename)
        print(f"Screenshot saved as {filename}")
    
    finally:
        # Close the browser
        driver.quit()

# Example usage
capture_screenshot("https://www.example.com", "example_screenshot.png")
