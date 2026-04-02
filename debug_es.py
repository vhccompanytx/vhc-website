
with open('frontend/portfolio-es.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The em dash is stored as \\u2014 (literal backslash u 2014) in the file
# We need to find and replace the Tesla Metal Home block
old_snippet = r"name:'Tesla Powerwall \u2014 Casa Metal + EV',loc:'Austin, TX',photos:["

# Find start
start_idx = content.find(old_snippet)
if start_idx == -1:
    print('ERROR: not found - trying unicode')
    old_snippet2 = "name:'Tesla Powerwall \u2014 Casa Metal + EV',loc:'Austin, TX',photos:["
    start_idx = content.find(old_snippet2)
    if start_idx != -1:
        print('Found with unicode version at:', start_idx)
        old_snippet = old_snippet2
    else:
        print('Still not found')
        exit()
else:
    print('Found at:', start_idx)

# Find end of this entry (ends with ]},)
end_search_start = start_idx + len(old_snippet)
end_idx = content.find(']},', end_search_start)
print('End idx:', end_idx)
print('Old block:', repr(content[start_idx:end_idx+3]))

new_block = (old_snippet + r"""
            {src:'brand/tesla 3.jpg',cap:'3x Tesla Powerwall + cargador EV Nivel 2 \u2014 metal corrugado rojo'},
            {src:'brand/tesla2.jpg',cap:'Doble Tesla Powerwall + cargador EV, trabajo de conduit'},
            {src:'brand/WhatsApp Image 2026-03-31 at 11.12.55 PM.jpeg',cap:'Tesla Powerwall (logo T) + cargador EV + postes de seguridad \u2014 completado'},
            {src:'brand/tesla 5.jpg',cap:'Tesla Gateway + desconectadores Eaton \u2014 detalle de cableado'},
            {src:'brand/testa project1.jpg',cap:'Instalaci\u00f3n de conduit el\u00e9ctrico \u2014 pared lateral cerca de HVAC'},
            {src:'brand/tesla 4.jpg',cap:'Vista a\u00e9rea del vecindario \u2014 paneles solares en casa de metal rojo'}
        ]},""")

content = content[:start_idx] + new_block + content[end_idx+3:]
with open('frontend/portfolio-es.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('SUCCESS')
