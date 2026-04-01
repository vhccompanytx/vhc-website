const fs = require('fs');
let ht = fs.readFileSync('c:/Users/vrgon/Desktop/VHC Web/index.html', 'utf8');

// 1. Remove contact section inline background and overlay
ht = ht.replace('<section id="contact" class="section-padding" style="background: url(\'brand/og_image.png\') center/cover; position: relative;">', '<section id="contact" class="section-padding" style="position: relative;">');
ht = ht.replace('<div style="position: absolute; inset: 0; background: rgba(244, 246, 249, 0.95); backdrop-filter: blur(10px);"></div>\r\n', '');
ht = ht.replace('<div style="position: absolute; inset: 0; background: rgba(244, 246, 249, 0.95); backdrop-filter: blur(10px);"></div>\n', '');

// 2. Dash removal in copy (Em-dashes)
// 2.1 Between sentences where next is lower case
ht = ht.replace(/ \u2014 ([a-z])/g, (m, p1) => '. ' + p1.toUpperCase());
// 2.2 Between sentences where next is upper case
ht = ht.replace(/ \u2014 ([A-Z])/g, '. $1');
// 2.3 Standalone or other usages
ht = ht.replace(/\u2014/g, '-');

// 3. EN-dashes (Used for ranges)
ht = ht.replace(/\u2013/g, '-');

fs.writeFileSync('c:/Users/vrgon/Desktop/VHC Web/index.html', ht);
console.log('Success');
