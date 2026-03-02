import feedparser
from datetime import datetime, timezone

# Define feeds
feeds = {
    "FCA (UK)": "https://www.fca.org.uk/news/rss.xml",
    "OCC (US)": "https://www.occ.gov/rss/occ-news.xml"
}

last_updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

# -------------------------------
# Build index.html (FCA only)
# -------------------------------
index_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>FCA Regulatory Intelligence</title>
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
<h1>FCA Regulatory Intelligence</h1>
<p><small>Last updated: {last_updated}</small></p>
"""

fca_feed = feedparser.parse(feeds["FCA (UK)"])
print("FCA feed status:", fca_feed.bozo)
if hasattr(fca_feed, "bozo_exception") and fca_feed.bozo_exception:
    print("FCA feed error:", fca_feed.bozo_exception)
print("Number of FCA entries:", len(fca_feed.entries))

index_html += "<h2>FCA (UK)</h2><ul>"
if fca_feed.entries:
    for entry in fca_feed.entries[:5]:
        index_html += f'<li><a href="{entry.link}" target="_blank">{entry.title}</a></li>'
else:
    index_html += "<li>No recent updates available.</li>"
index_html += "</ul>"

# Add navigation link to OCC page
index_html += '<p><a href="OCC.html">View OCC Regulatory Intelligence</a></p>'
index_html += "</body></html>"

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_html)

# -------------------------------
# Build OCC.html (OCC only)
# -------------------------------
occ_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>OCC Regulatory Intelligence</title>
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
<h1>OCC Regulatory Intelligence</h1>
<p><small>Last updated: {last_updated}</small></p>
"""

occ_feed = feedparser.parse(feeds["OCC (US)"])
print("OCC feed status:", occ_feed.bozo)
if hasattr(occ_feed, "bozo_exception") and occ_feed.bozo_exception:
    print("OCC feed error:", occ_feed.bozo_exception)
print("Number of OCC entries:", len(occ_feed.entries))

occ_html += "<h2>OCC (US)</h2><ul>"
if occ_feed.entries:
    for entry in occ_feed.entries[:5]:
        occ_html += f'<li><a href="{entry.link}" target="_blank">{entry.title}</a></li>'
else:
    occ_html += '<li>Unable to load OCC feed. <a href="https://www.occ.gov/news-events/newsroom/index.html" target="_blank">Visit OCC Newsroom</a></li>'
occ_html += "</ul>"

# Add navigation back to FCA page
occ_html += '<p><a href="index.html">Back to FCA Regulatory Intelligence</a></p>'
occ_html += "</body></html>"

with open("OCC.html", "w", encoding="utf-8") as f:
    f.write(occ_html)
