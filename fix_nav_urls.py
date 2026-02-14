import yaml

# Load navigation
with open('src/_data/navigation.yml', 'r') as f:
    nav_data = yaml.safe_load(f)

def fix_url(url):
    if url and not url.startswith('/') and not url.startswith('http'):
        return '/' + url
    return url

for item in nav_data['main']:
    item['url'] = fix_url(item['url'])
    if 'subitems' in item and item['subitems']:
        for sub in item['subitems']:
            sub['url'] = fix_url(sub['url'])

# Write back
with open('src/_data/navigation.yml', 'w') as f:
    yaml.dump(nav_data, f, allow_unicode=True, sort_keys=False)

print("Navigation URLs fixed.")
