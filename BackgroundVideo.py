import pywhatkit as kit
import webbrowser
import random

# List of search terms
search_terms = ["subway surfers gameplay", "subway surfers world tour", "subway surfers high score"]

# Select a random search term
search_term = random.choice(search_terms)

# Search for the video on YouTube
video_url = kit.playonyt(search_term)

# Open the video in the web browser
webbrowser.open(video_url)
