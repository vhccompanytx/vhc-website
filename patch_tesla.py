
with open('frontend/portfolio.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the Tesla Metal Home project in the JS data and update it
old_snippet = "name:'Tesla Powerwall \u2014 Metal Home + EV',loc:'Austin, TX',photos:["
new_photos = """name:'Tesla Powerwall \u2014 Metal Home + EV',loc:'Austin, TX',photos:[
            {src:'brand/tesla 3.jpg',cap:'3x Tesla Powerwall + Level 2 EV charger \u2014 red corrugated metal, full system view'},
            {src:'brand/tesla2.jpg',cap:'Dual Tesla Powerwall + EV charger, conduit rails work'},
            {src:'brand/WhatsApp Image 2026-03-31 at 11.12.55 PM.jpeg',cap:'Tesla Powerwall (T logo) + EV charger + safety bollards \u2014 completed'},
            {src:'brand/tesla 5.jpg',cap:'Tesla Gateway + Eaton disconnects \u2014 completed wiring detail'},
            {src:'brand/testa project1.jpg',cap:'Electrical conduit installation \u2014 side wall near HVAC'},
            {src:'brand/tesla 4.jpg',cap:'Aerial neighborhood view \u2014 blue solar panels on red metal home'}
        ]}"""

idx = content.find(old_snippet)
if idx == -1:
    print('ERROR: snippet not found')
else:
    # find the end of this project object (ends with ]},)
    end_search_start = idx + len(old_snippet)
    end_idx = content.find(']},', end_search_start)
    if end_idx == -1:
        print('ERROR: end not found')
    else:
        old_block = content[idx:end_idx+3]
        print('Old block found, length:', len(old_block))
        new_block = new_photos + ','
        content = content[:idx] + new_block + content[end_idx+3:]
        with open('frontend/portfolio.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print('SUCCESS: Tesla project updated with 6 photos in portfolio.html')

# Also update the card thumbnail and photo count display in HTML
# Update card to show 6 photos
with open('frontend/portfolio.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update the card thumbnail for Tesla Metal Home to use tesla 3.jpg
old_card_img = 'src="brand/WhatsApp Image 2026-03-31 at 11.12.55 PM.jpeg" alt="Tesla Powerwall red metal home"'
new_card_img = 'src="brand/tesla 3.jpg" alt="Tesla Powerwall red metal home"'
if old_card_img in content:
    content = content.replace(old_card_img, new_card_img, 1)
    print('Updated card thumbnail for Tesla Metal Home')

with open('frontend/portfolio.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done with portfolio.html')
