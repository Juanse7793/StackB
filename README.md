# Hacker News Web Crawler

This project is a web crawler that extracts the first 30 entries from [Hacker News](https://news.ycombinator.com/). It retrieves the number, title, points, and comments for each entry and supports filtering operations based on the number of words in the title.

## Author

👤 **Juan Sebastian Sotomayor**

- GitHub: [@Juanse7793](https://github.com/Juanse7793)
- LinkedIn: [Juan Sebastian Sotomayor](https://linkedin.com/in/juansebastiansotomayor)

## Features

- Fetch the first 30 news stories from Hacker News
- Filter stories with more than five words in the title, ordered by the number of comments
- Filter stories with five or fewer words in the title, ordered by points
- Log usage data including the request timestamp and applied filter to both an SQLite database and a text file

## Requirements

- Python 3.6 or higher
- `requests`
- `beautifulsoup4`
- `sqlite3` (part of the Python standard library)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/hacker-news-crawler.git
cd hacker-news-crawler
```

### 2. Set Up the Virtual Environment

Create a virtual environment to manage dependencies.

```bash
python -m venv env
```

Activate the virtual environment:

- On Windows:

```bash
.\env\Scripts\Activate.ps1
```

- On macOS/Linux:

```bash
source env/bin/activate
```

### 3. Install Dependencies

Install the required Python packages.

```bash
pip install requests beautifulsoup4
```

### 4. Run the Main Crawler

Run the web crawler script to fetch news, apply filters, and log the usage data.

```bash
python mainCrawler.py
```

## Project Structure

- `mainCrawler.py`: Main script that fetches news, applies filters, and logs usage data.
- `requirements.txt`: List of dependencies (if needed).
- `usage_log.txt`: Log file that records the usage data.
- `usage_data.db`: SQLite database that stores the usage data (automatically created by the script).
- `env/`: Virtual environment directory (ignored in the repository).

## How It Works

1. Setup Database: Creates an SQLite database to store usage data if it doesn't already exist.
2. Fetch News: Fetches the first 30 news stories from Hacker News.
3. Filter News:

   - `filter_by_comments`: Filters stories with more than five words in the title and sorts them by the number of comments.
   - `filter_by_points`: Filters stories with five or fewer words in the title and sorts them by points.

4. Log Requests: Logs the request timestamp and applied filter to both the SQLite database and a text file.3
5. Print Results: Prints the filtered results to the console.

## Example Output

```bash
Added story 1: Polyfill supply chain attack hits 100K+ sites
Added story 2: Show HN: Glasskube – Open Source Kubernetes Package Manager, alternative to Helm
...
Total stories fetched: 30
Filtered by comments: 10 entries
Filtered by points: 20 entries
Filtered by comments:
{'number': '1', 'title': 'Polyfill supply chain attack hits 100K+ sites', 'points': 280, 'comments': 113}
...

Filtered by points:
{'number': '2', 'title': 'Show HN: Glasskube – Open Source Kubernetes Package Manager, alternative to Helm', 'points': 79, 'comments': 26}
...
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

## Show your support

Give a ⭐️ if you like this project!

## Acknowledgments

- Hat tip to anyone whose code was used
- Stack Builders
- Camila Vasquez

## 📝 License

This project is [MIT](./MIT.md) licensed.
