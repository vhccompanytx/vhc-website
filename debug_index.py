with open('frontend/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the actual vhcSlide function JS
idx = content.find('function vhcSlide')
if idx != -1:
    print('vhcSlide function:')
    print(content[idx:idx+1000])
else:
    # try script tags near carousel
    idx2 = content.find('vhcCarousel')
    # find last script that references this  
    all_idxs = []
    start = 0
    while True:
        i = content.find('vhcCarousel', start)
        if i == -1: break
        all_idxs.append(i)
        start = i + 1
    print('All vhcCarousel occurrences:', all_idxs)
    # show the last one (likely the script)
    if all_idxs:
        last = all_idxs[-1]
        print(content[last:last+1200])
