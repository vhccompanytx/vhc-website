import re

for fname in ['frontend/index.html', 'frontend/index-es.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace all slide style: aspect-ratio:16/10;flex-shrink:0;height:auto
    # → height: clamp(280px, 50vh, 480px); flex-shrink:0  (no aspect-ratio, just capped height)
    original = content

    # Pattern 1 (slide 1 - no border-radius)
    content = content.replace(
        'style="min-width:100%;position:relative;overflow:hidden;aspect-ratio:16/10;flex-shrink:0;height:auto;"',
        'style="min-width:100%;position:relative;overflow:hidden;height:clamp(280px,50vh,480px);flex-shrink:0;"'
    )
    # Pattern 2 (slides 2-8 - with border-radius)
    content = content.replace(
        'style="min-width:100%;position:relative;border-radius:20px;overflow:hidden;aspect-ratio:16/10;flex-shrink:0;height:auto;"',
        'style="min-width:100%;position:relative;overflow:hidden;height:clamp(280px,50vh,480px);flex-shrink:0;"'
    )

    changed = content != original
    print(f'{fname}: {"CHANGED" if changed else "NO CHANGE"}')

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

print('Done')
