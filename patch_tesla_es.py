
with open('frontend/portfolio-es.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_snippet = "name:'Tesla Powerwall \u2014 Casa Metal + EV'"
new_block_str = """name:'Tesla Powerwall \u2014 Casa Metal + EV',loc:'Austin, TX',photos:[
            {src:'brand/tesla 3.jpg',cap:'3x Tesla Powerwall + cargador EV Nivel 2 \u2014 metal corrugado rojo'},
            {src:'brand/tesla2.jpg',cap:'Doble Tesla Powerwall + cargador EV, instalaci\u00f3n de conduit'},
            {src:'brand/WhatsApp Image 2026-03-31 at 11.12.55 PM.jpeg',cap:'Tesla Powerwall (logo T) + cargador EV + postes de seguridad \u2014 completado'},
            {src:'brand/tesla 5.jpg',cap:'Tesla Gateway + desconectadores Eaton \u2014 detalle de cableado'},
            {src:'brand/testa project1.jpg',cap:'Instalaci\u00f3n de conduit el\u00e9ctrico \u2014 pared lateral cerca de HVAC'},
            {src:'brand/tesla 4.jpg',cap:'Vista a\u00e9rea del vecindario \u2014 paneles solares en casa de metal rojo'}
        ]},"""

idx = content.find(old_snippet)
if idx == -1:
    print('ERROR: not found')
else:
    end_search_start = idx + len(old_snippet)
    end_idx = content.find(']},', end_search_start)
    if end_idx == -1:
        print('ERROR: end not found')
    else:
        content = content[:idx] + new_block_str + content[end_idx+3:]
        with open('frontend/portfolio-es.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print('SUCCESS: Tesla project updated in portfolio-es.html')

# Update card thumbnail too
with open('frontend/portfolio-es.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_card = 'src="brand/WhatsApp Image 2026-03-31 at 11.12.55 PM.jpeg" alt="Tesla casa metal"'
new_card = 'src="brand/tesla 3.jpg" alt="Tesla casa metal"'
if old_card in content:
    content = content.replace(old_card, new_card, 1)
    print('Updated card thumbnail in ES portfolio')
    with open('frontend/portfolio-es.html', 'w', encoding='utf-8') as f:
        f.write(content)

print('Done')
