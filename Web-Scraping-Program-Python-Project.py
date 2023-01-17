import requests
from bs4 import BeautifulSoup
import time

# URL to scrape
url = 'https://www.example.com'

# Send a GET request to the website
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.HTTPError as errh:
    print ("HTTP Error:",errh)
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)
except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)
except requests.exceptions.RequestException as err:
    print ("Something Else:",err)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the desired data using CSS selectors
data = soup.select('css_selector')

# Print the extracted data
if data:
    for item in data:
        print(item.text)
else:
    print("No data found")
    
# Adding delay between requests
time.sleep(5)
