import re

def optimize_index(filename, is_es=False):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add loading="lazy" to carousel images
    content = re.sub(r'(<div class="vhc-slide".*?<img src=".*?")', 
                     r'\1 loading="lazy"', content, flags=re.DOTALL)

    # 2. Add aria-labels to carousel buttons
    if is_es:
        content = content.replace('id="vhcPrevEs"', 'id="vhcPrevEs" aria-label="Ir a diapositiva anterior"')
        content = content.replace('id="vhcNextEs"', 'id="vhcNextEs" aria-label="Ir a siguiente diapositiva"')
    else:
        content = content.replace('id="vhcPrev"', 'id="vhcPrev" aria-label="Go to previous slide"')
        content = content.replace('id="vhcNext"', 'id="vhcNext" aria-label="Go to next slide"')

    # 3. Add fade-in animation to slides
    animation_css = """
        .vhc-slide img {
            transition: opacity 0.8s ease-in-out;
        }
        .vhc-slide.active img {
            opacity: 1;
        }
        /* Simple fade effect during slide transition */
        .vhc-carousel {
            transition: transform 0.6s cubic-bezier(0.25, 1, 0.5, 1);
        }
    """
    content = content.replace('</style>', animation_css + '\n    </style>')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

optimize_index('frontend/index.html')
optimize_index('frontend/index-es.html', is_es=True)
print("Index files optimized (Performance + A11y).")
