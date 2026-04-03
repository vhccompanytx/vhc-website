import re

# ── New JS block with touch support ──────────────────────────────────────────
NEW_JS = """        <script>
            (function(){
                var w=document.querySelector('.vhc-carousel-wrapper');
                var c=document.getElementById('vhcCarousel');
                var slides=c.querySelectorAll('.vhc-slide');
                var dotsEl=document.getElementById('vhcDots');
                var cur=0, total=slides.length, timer;
                c.style.transition='transform .5s cubic-bezier(.4,0,.2,1)';
                // Build dots
                slides.forEach(function(_,i){
                    var d=document.createElement('button');
                    d.style.cssText='width:8px;height:8px;border-radius:50%;border:none;cursor:pointer;transition:all .3s;background:'+(i===0?'var(--vhc-gold)':'rgba(10,18,41,0.2)');
                    d.setAttribute('aria-label','Slide '+(i+1));
                    (function(idx){d.onclick=function(){goTo(idx);};})(i);
                    dotsEl.appendChild(d);
                });
                function goTo(n){
                    cur=(n%total+total)%total;
                    c.style.transform='translateX(-'+cur+'00%)';
                    dotsEl.querySelectorAll('button').forEach(function(d,i){
                        d.style.background=i===cur?'var(--vhc-gold)':'rgba(10,18,41,0.2)';
                        d.style.width=i===cur?'22px':'8px';
                    });
                    clearInterval(timer);
                    timer=setInterval(function(){goTo(cur+1);},5500);
                }
                window.vhcSlide=function(d){goTo(cur+d);};
                // Touch / swipe support
                var tx=0, dragging=false;
                var el=w||c;
                el.addEventListener('touchstart',function(e){
                    tx=e.touches[0].clientX; dragging=true;
                    c.style.transition='none';
                    clearInterval(timer);
                },{ passive:true });
                el.addEventListener('touchmove',function(e){
                    if(!dragging) return;
                    var dx=e.touches[0].clientX-tx;
                    var base=-(cur*100);
                    var pct=base+(dx/el.offsetWidth*100);
                    c.style.transform='translateX('+pct+'%)';
                },{ passive:true });
                el.addEventListener('touchend',function(e){
                    if(!dragging) return; dragging=false;
                    var dx=e.changedTouches[0].clientX-tx;
                    c.style.transition='transform .5s cubic-bezier(.4,0,.2,1)';
                    if(dx < -50) goTo(cur+1);
                    else if(dx > 50) goTo(cur-1);
                    else goTo(cur);
                });
                timer=setInterval(function(){goTo(cur+1);},5500);
            })();
        </script>"""

for fname in ['frontend/index.html', 'frontend/index-es.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    is_es = ('Es' in fname.split('index')[1])
    carousel_id = 'vhcCarouselEs' if is_es else 'vhcCarousel'
    dots_id = 'vhcDotsEs' if is_es else 'vhcDots'
    slide_fn = 'vhcSlideEs' if is_es else 'vhcSlide'
    label_text = 'Diapositiva' if is_es else 'Slide'
    cta_text = 'Ver Todos' if is_es else 'See All'

    # 1. Fix slide height → aspect-ratio
    # Replace all: height:480px;flex-shrink:0 → aspect-ratio:16/10;flex-shrink:0;height:auto
    content = re.sub(
        r'(class="vhc-slide"[^>]*?)height:480px;flex-shrink:0;',
        r'\1aspect-ratio:16/10;flex-shrink:0;height:auto;',
        content
    )
    # Also handle the one slide that had overflow before height
    content = re.sub(
        r'(class="vhc-slide"[^>]*?overflow:hidden;)height:480px;flex-shrink:0;',
        r'\1aspect-ratio:16/10;flex-shrink:0;height:auto;',
        content
    )
    print(f'{fname}: slide height replaced')

    # 2. Replace the entire script block
    # For EN
    old_script_start = '        <script>\n            (function(){\n                var c=document.getElementById(\'' + carousel_id + '\');\n'
    old_script_end = '            })();\n        </script>'

    start_idx = content.find(old_script_start)
    if start_idx == -1:
        # Try with \r\n
        old_script_start = '        <script>\r\n            (function(){\r\n                var c=document.getElementById(\'' + carousel_id + '\');\r\n'
        start_idx = content.find(old_script_start)

    end_idx = content.find(old_script_end, start_idx if start_idx != -1 else 0)

    if start_idx != -1 and end_idx != -1:
        # Build the new JS for this file (swap IDs)
        new_js = NEW_JS.replace('vhcCarousel', carousel_id, 1)
        new_js = new_js.replace("'vhcDots'", "'" + dots_id + "'", 1)
        new_js = new_js.replace('window.vhcSlide', 'window.' + slide_fn)
        new_js = new_js.replace("'Slide '", "'" + label_text + " '")
        content = content[:start_idx] + new_js + '\n' + content[end_idx + len(old_script_end):]
        print(f'{fname}: JS replaced')
    else:
        print(f'{fname}: JS start={start_idx} end={end_idx} - NOT replaced')

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'{fname}: done\n')
