with open('frontend/index-es.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: CSS height override in <style>
content = content.replace('height: 380px; /* Altura optimizada para laptops */', 'height: 320px !important; /* Cap vertical a 320px para laptops */')

# Fix 2: Remove height:auto from all slides
import re
content = re.sub(r'class="vhc-slide" style="min-width:100%;position:relative;overflow:hidden;height:auto;flex-shrink:0;"',
                 r'class="vhc-slide" style="min-width:100%;position:relative;overflow:hidden;flex-shrink:0;"', 
                 content)

# Fix 3: Force images to cover 100% height
content = re.sub(r'style="width:100%;height:100%;object-fit:cover;display:block;"',
                 r'style="width:100%;height:100% !important;object-fit:cover !important;display:block;"',
                 content)

with open('frontend/index-es.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("ES Carousel Fixed to 320px + inline specificity fix.")
