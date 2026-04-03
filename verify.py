import re
with open('frontend/index.html','r',encoding='utf-8') as f:
    c = f.read()
slides = re.findall(r'class="vhc-slide"[^>]+>', c)
print('EN slides found:', len(slides))
for s in slides[:3]:
    print(' ', repr(s[:150]))
