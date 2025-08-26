# Kaldata Scraper 🕷️
<br />
This project is a Scrapy-based web scraping application that extracts news articles from Kaldata.<br />
The collected data is stored in a SQLite database (kaldata.db) and automatically updated every hour via GitHub Actions.<br />
<br />
# Features 🚀
<br />
Extracts article title, publication date, author, and body using Scrapy<br />
Stores all scraped data into a SQLite database (kaldata.db)<br />
Automated crawling with GitHub Actions (runs every hour)<br />
Database updates are version-controlled via Git commits<br />
<br />
# Project Structure 📂
**kaldata-scraper**
│<br />
├── **.github/workflows/**             # GitHub Actions workflows<br />
│ &nbsp; &nbsp;  └── **scrapy-crawl.yml**<br />
├── **kaldata**/                      # Scrapy project package<br />
│  &nbsp; &nbsp; ├── **content-schema.json**        # Item definitions<br />
│  &nbsp; &nbsp; ├── **content.json**               # Item definitions<br />
│  &nbsp; &nbsp;  ├── **items.py**                   # Item definitions<br />
│  &nbsp; &nbsp;  ├── **kaldata.db**                 # SQLite database (auto-created/updated)<br />
│  &nbsp; &nbsp;  ├── **main.py**                    # <br />
│  &nbsp; &nbsp;  ├── **middlewares.py**             # <br />
│  &nbsp; &nbsp;  ├── **pipelines.py**               # SQLite pipeline<br />
│  &nbsp; &nbsp;  ├── **settings.py**                # Scrapy settings<br />
│  &nbsp; &nbsp;  └── **spiders/**<br />
│  &nbsp; &nbsp; &nbsp; &nbsp;      └── **kaldata_spider.py**      # Main spider<br />
│<br />
├── **flowchart_kaldata_spider.jpg**   # Workflow<br />
├── **scrapy.cfg**                     # Scrapy configuration file<br />
├── **requirements.txt**               # Requirements<br />
└── **README.md**<br />
<br />

Local Setup ⚙️ <br />
<br />
Clone the repository:<br />
git clone https://github.com/<your-user_name>/kaldata-scraper.git<br />
cd kaldata-scraper<br />
Install dependencies:<br />
pip install scrapy<br />
Run the spider:<br />
scrapy crawl kaldata_spider<br />
After execution, a kaldata.db SQLite database will be created/updated with the scraped articles.<br />
<br />
# GitHub Actions (Automated Runs) ⏰ <br />
<br />
This project includes a workflow at .github/workflows/scrapy-crawl.yml.<br />
The workflow:<br />
<br />
Runs every hour (via cron job)<br />
Executes the spider<br />
Updates kaldata.db with new data<br />
Commits changes back to the repository<br />
You can view run logs under the Actions tab in the repository.<br />
<br />
# Database Schema 📝 <br />
<br />
The SQLite database contains a single table: articles<br />
<br />
Field	Type	Description<br />
id	int	Auto-increment PK<br />
title	text	Article title<br />
pubdate	text	Publication datetime<br />
author	text	Article author<br />
body	text	Article content<br />
# Contributing🔧 <br />
<br />
Issues and pull requests are welcome.<br />
Future improvements could include exporting to JSON/CSV or adding more categories.<br />
