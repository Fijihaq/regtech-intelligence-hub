import feedparser
from datetime import datetime, timezone

feeds = {
    "FCA (UK)": "https://www.fca.org.uk/news/rss.xml",
    "Bank of England (UK)": "https://www.bankofengland.co.uk/news/rss",
    "Reuters Business": "https://feeds.reuters.com/reuters/businessNews",
    "AP News Business": "https://apnews.com/hub/business?outputType=xml"
}

last_updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

html_content = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Live Regulatory Intelligence</title>
<style>
body {{ font-family: Arial; max-width: 900px; margin: auto; padding: 20px; }}
h1 {{ color: #1a1a1a; }}
h2 {{ margin-top: 30px; }}
ul {{ padding-left: 20px; }}
li {{ margin-bottom: 8px; }}
small {{ color: gray; }}
</style>
</head>
<body>
<h1>Live Regulatory Intelligence</h1>
<p><small>Last updated: {last_updated}</small></p>
"""

for source, url in feeds.items():
    feed = feedparser.parse(url)
    html_content += f"<h2>{source}</h2><ul>"

    if feed.entries:
        for entry in feed.entries[:5]:
            html_content += f'<li><a href="{entry.link}" target="_blank">{entry.title}</a></li>'
    else:
        html_content += "<li>No recent updates available.</li>"

    html_content += "</ul>"

html_content += "</body></html>"

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)
