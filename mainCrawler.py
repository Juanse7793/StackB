import requests
from bs4 import BeautifulSoup
from datetime import datetime
import sqlite3

# Set up SQLite database
def setup_database():
    """Create an SQLite database to store usage data if it does not exist."""
    conn = sqlite3.connect('usage_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usage (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            filter_type TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Log usage data to the database and text file
def log_request(filter_type):
    """Log the request in the database and a text file."""
    conn = sqlite3.connect('usage_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO usage (timestamp, filter_type) 
        VALUES (?, ?)
    ''', (datetime.now().isoformat(), filter_type))
    conn.commit()
    conn.close()
    
    with open('usage_log.txt', 'a') as log_file:
        log_file.write(f"{datetime.now().isoformat()} - Filter: {filter_type}\n")
    
    print(f"Logged request: {datetime.now().isoformat()} - Filter: {filter_type}")

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

# Filter news by number of comments
def filter_by_comments(news):
    """Filter news with more than 5 words in the title and sort by number of comments."""
    filtered = sorted([entry for entry in news if len(entry['title'].split()) > 5], key=lambda x: x['comments'], reverse=True)
    print(f"Filtered by comments: {len(filtered)} entries")
    return filtered

# Filter news by number of points
def filter_by_points(news):
    """Filter news with 5 or fewer words in the title and sort by number of points."""
    filtered = sorted([entry for entry in news if len(entry['title'].split()) <= 5], key=lambda x: x['points'], reverse=True)
    print(f"Filtered by points: {len(filtered)} entries")
    return filtered

if __name__ == "__main__":
    # Set up the database
    setup_database()
    
    # Fetch news
    news = fetch_news()
    if not news:
        print("No news fetched.")
    
    # Filter news by comments and log the request
    comments_filtered = filter_by_comments(news)
    log_request('comments')
    
    # Filter news by points and log the request
    points_filtered = filter_by_points(news)
    log_request('points')
    
    # Print filtered results
    print("Filtered by comments:")
    for entry in comments_filtered:
        print(entry)
    
    print("\nFiltered by points:")
    for entry in points_filtered:
        print(entry)
