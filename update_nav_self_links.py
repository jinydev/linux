import yaml

# Load navigation
with open('src/_data/navigation.yml', 'r') as f:
    nav_data = yaml.safe_load(f)

for item in nav_data['main']:
    if 'subitems' in item and item['subitems']:
        # Check if first subitem is the main link
        first_sub = item['subitems'][0]
        if first_sub['url'] != item['url']:
            # Prepend main link
            # Use a slightly different title or same? c01 used "1주차 하기". 
            # I'll just use the main title "01.리눅스와 소개".
            main_link = {'title': item['title'], 'url': item['url']}
            item['subitems'].insert(0, main_link)

# Write back
with open('src/_data/navigation.yml', 'w') as f:
    yaml.dump(nav_data, f, allow_unicode=True, sort_keys=False)

print("Navigation updated with self-links.")
