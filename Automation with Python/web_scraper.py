import requests
from bs4 import BeautifulSoup

def scrape_hacker_news():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    stories = soup.find_all('tr', class_='athing')
    
    for story in stories[:5]:  # Get top 5 stories
        title = story.find('a', class_='storylink').text
        link = story.find('a', class_='storylink')['href']
        print(f"Title: {title}")
        print(f"Link: {link}")
        print("---")

scrape_hacker_news()
