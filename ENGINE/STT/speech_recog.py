import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep

voice_html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'ASSETS', 'voice.html')

if not os.path.isfile(voice_html_path):
    raise FileNotFoundError("voice.html file not found at: " + voice_html_path)

chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--use-fake-device-for-media-stream")
chrome_options.add_argument("--headless=new")

driver = webdriver.Chrome(options=chrome_options)
driver.get(voice_html_path)

def speech_recognition_model():
    try:
        start_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "start")))
        start_button.click()
        print("Listening...")
        
        output_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "output")))
        text = output_element.text.strip()
        
        if text:
            end_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "end")))
            end_button.click()
            return text
    except TimeoutException:
        print("Timeout occurred while waiting for elements")
    except Exception as e:
        print("An error occurred:", e)

def close_driver():
    driver.quit()

if __name__ == "__main__":
    try:
        while True:
            speech = speech_recognition_model()
            if speech:
                print(speech)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        close_driver()