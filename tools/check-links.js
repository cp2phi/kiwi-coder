#!/usr/bin/env node
/* 🔗 检查构建好的网站（_site）里有没有坏链接 / 坏图片 / 坏脚本
 *   tools/build.sh && node tools/check-links.js [site-dir]
 */
const fs = require('fs');
const path = require('path');
const SITE = path.resolve(process.argv[2] || path.join(__dirname, '..', '_site'));
const BASE = '/kiwi-coder';
if (!fs.existsSync(SITE)) { console.error('没找到 ' + SITE + '，先运行 tools/build.sh'); process.exit(2); }
function walk(p, acc) {
  for (const f of fs.readdirSync(p)) {
    const q = path.join(p, f);
    if (fs.statSync(q).isDirectory()) walk(q, acc); else if (q.endsWith('.html')) acc.push(q);
  }
  return acc;
}
const pages = walk(SITE, []);
let bad = 0, total = 0;
const seen = new Set();
for (const pg of pages) {
  const html = fs.readFileSync(pg, 'utf8');
  const re = /(?:href|src|data-src|data-prelude|data-check|data-target)=["']([^"'#]+)(#[^"']*)?["']/g;
  let m;
  while ((m = re.exec(html))) {
    let u = m[1];
    if (/^(https?:|mailto:|data:|javascript:|\/\/)/.test(u)) continue;
    if (u.startsWith('{{')) continue;
    let target;
    if (u.startsWith('/')) {
      if (!u.startsWith(BASE + '/') && u !== BASE) { console.log('⚠️  ' + path.relative(SITE, pg) + ' → ' + u + '  (没有 baseurl，GitHub Pages 上会 404)'); bad++; continue; }
      target = path.join(SITE, u.slice(BASE.length));
    } else {
      target = path.resolve(path.dirname(pg), u);
    }
    const key = path.relative(SITE, pg) + ' → ' + u;
    if (seen.has(key)) continue;
    seen.add(key);
    total++;
    const ok = fs.existsSync(target) && (fs.statSync(target).isFile() || fs.existsSync(path.join(target, 'index.html')));
    if (!ok) { console.log('❌ ' + key); bad++; }
  }
}
console.log('\n' + total + ' links checked, ' + bad + ' broken');
process.exit(bad ? 1 : 0);
