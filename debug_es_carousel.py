with open('frontend/index-es.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_block = """<script>
            (function(){
                var c=document.getElementById('vhcCarouselEs');
                var slides=c.querySelectorAll('.vhc-slide');
                var dotsEl=document.getElementById('vhcDotsEs');
                var cur=0, total=slides.length, timer;
                c.style.transition='transform .5s cubic-bezier(.4,0,.2,1)';
                slides.forEach(function(_,i){
                    var d=document.createElement('button');
                    d.style.cssText='width:8px;height:8px;border-radius:50%;border:none;cursor:pointer;transition:all .3s;background:'+(i===0?'var(--vhc-gold)':'rgba(10,18,41,0.2)');
                    d.setAttribute('aria-label','Diapositiva '+(i+1));
                    (function(idx){d.onclick=function(){goToEs(idx);};})(i);
                    dotsEl.appendChild(d);
                });
                function goToEs(n){
                    cur=(n%total+total)%total;
                    c.style.transform='translateX(-'+cur+'00%)';
                    dotsEl.querySelectorAll('button').forEach(function(d,i){
                        d.style.background=i===cur?'var(--vhc-gold)':'rgba(10,18,41,0.2)';
                        d.style.width=i===cur?'22px':'8px';
                    });
                    clearInterval(timer);
                    timer=setInterval(function(){goToEs(cur+1);},5000);
                }
                window.vhcSlideEs=function(d){goToEs(cur+d);};
                c.style.transition='transform .5s cubic-bezier(.4,0,.2,1)';
                timer=setInterval(function(){goToEs(cur+1);},5000);
            })();
        </script>"""

new_block = """<script>
            (function(){
                var w=document.querySelector('.vhc-carousel-wrapper');
                var c=document.getElementById('vhcCarouselEs');
                var slides=c.querySelectorAll('.vhc-slide');
                var dotsEl=document.getElementById('vhcDotsEs');
                var cur=0, total=slides.length, timer;
                c.style.transition='transform .5s cubic-bezier(.4,0,.2,1)';
                slides.forEach(function(_,i){
                    var d=document.createElement('button');
                    d.style.cssText='width:8px;height:8px;border-radius:50%;border:none;cursor:pointer;transition:all .3s;background:'+(i===0?'var(--vhc-gold)':'rgba(10,18,41,0.2)');
                    d.setAttribute('aria-label','Diapositiva '+(i+1));
                    (function(idx){d.onclick=function(){goToEs(idx);};})(i);
                    dotsEl.appendChild(d);
                });
                function goToEs(n){
                    cur=(n%total+total)%total;
                    c.style.transform='translateX(-'+cur+'00%)';
                    dotsEl.querySelectorAll('button').forEach(function(d,i){
                        d.style.background=i===cur?'var(--vhc-gold)':'rgba(10,18,41,0.2)';
                        d.style.width=i===cur?'22px':'8px';
                    });
                    clearInterval(timer);
                    timer=setInterval(function(){goToEs(cur+1);},5500);
                }
                window.vhcSlideEs=function(d){goToEs(cur+d);};
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
                    if(dx < -50) goToEs(cur+1);
                    else if(dx > 50) goToEs(cur-1);
                    else goToEs(cur);
                });
                timer=setInterval(function(){goToEs(cur+1);},5500);
            })();
        </script>"""

if old_block in content:
    content = content.replace(old_block, new_block)
    print('SUCCESS')
    with open('frontend/index-es.html', 'w', encoding='utf-8') as f:
        f.write(content)
else:
    print('ERROR: block not found')
