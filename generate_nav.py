import yaml
import re
import os

# Load existing navigation
with open('src/_data/navigation.yml', 'r') as f:
    nav_data = yaml.safe_load(f)

# Parse parsed links
links = {}
with open('all_links.txt', 'r') as f:
    for line in f:
        # Match: src/{chapter}/index.md: ... [title](url) ...
        match = re.search(r'src/([^/]+)/index\.md:.*\[([^\]]+)\]\(([^\)]+)\)', line)
        if match:
            chapter = match.group(1)
            title = match.group(2).strip()
            url = match.group(3).strip()
            
            # Filter out some common non-link stuff if needed, or just include all
            if chapter not in links:
                links[chapter] = []
            
            # Avoid duplicates
            if not any(l['url'] == url for l in links[chapter]):
                links[chapter].append({'title': title, 'url': url})

# Update navigation data
for item in nav_data['main']:
    # Extract chapter from url (e.g., /01_intro/ -> 01_intro)
    chapter_match = re.search(r'/([^/]+)/', item['url'])
    if chapter_match:
        chapter = chapter_match.group(1)
        if chapter in links:
            item['subitems'] = links[chapter]

# Write back
with open('src/_data/navigation.yml', 'w') as f:
    yaml.dump(nav_data, f, allow_unicode=True, sort_keys=False)

print("Navigation updated.")
