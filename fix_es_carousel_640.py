with open('frontend/index-es.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update the CSS height to 640px
content = content.replace('height: 320px !important; /* Cap vertical a 320px para laptops */', 'height: 640px !important; /* Cap vertical a 640px para impact */')

with open('frontend/index-es.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("ES Carousel Height Updated to 640px.")
