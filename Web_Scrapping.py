import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = "https://example.com"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract data from the webpage (for example, scraping all the links)
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))

    # Print the scraped data (in this case, the links)
    for link in links:
        print(link)
else:
    print("Failed to fetch the webpage. Status code:", response.status_code)