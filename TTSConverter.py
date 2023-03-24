import pywhatkit as kit
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random

# List of search terms
search_terms = ["subway surfers gameplay", "subway surfers world tour", "subway surfers high score"]

# Select a random search term
search_term = random.choice(search_terms)

# Search for the video on YouTube
video_url = kit.playonyt(search_term)

# Configure the web browser to play the video on mute
chrome_options = Options()
chrome_options.add_argument("--mute-audio")
driver = webdriver.Chrome(options=chrome_options)
driver.get(video_url)
driver.execute_script("document.querySelector('video').muted=true;")
