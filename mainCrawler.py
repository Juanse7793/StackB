# Import necessary libraries
import requests
from bs4 import BeautifulSoup

# Fetch news from Hacker News
def fetch_news():
    """Fetch the first 30 news stories from Hacker News."""
    url = 'https://news.ycombinator.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    stories = soup.find_all('tr', class_='athing')
    
    news = []
    for i, story in enumerate(stories[:30], start=1):
        title_tag = story.find('span', class_='titleline').find('a')
        subtext_tag = story.find_next_sibling('tr').find('td', class_='subtext')
        
        if title_tag is None or subtext_tag is None:
            print(f"Skipping story {i} due to missing title or subtext")
            continue
        
        title = title_tag.text
        number = story.find('span', class_='rank').text.strip('.')
        points_tag = subtext_tag.find('span', class_='score')
        points = int(points_tag.text.split()[0]) if points_tag else 0
        
        comments_text = subtext_tag.find_all('a')[-1].text
        comments = int(comments_text.split()[0]) if 'comment' in comments_text else 0

        news.append({
            'number': number,
            'title': title,
            'points': points,
            'comments': comments
        })
        print(f"Added story {i}: {title}")

    print(f"Total stories fetched: {len(news)}")
    return news
