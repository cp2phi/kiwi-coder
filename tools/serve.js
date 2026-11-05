#!/usr/bin/env node
/* 🌐 不用 Docker 也能预览构建好的 _site：node tools/serve.js → http://localhost:4000/kiwi-coder/ */
const http = require('http'), fs = require('fs'), path = require('path');
const SITE = path.resolve(process.argv[2] || path.join(__dirname, '..', '_site'));
const BASE = '/kiwi-coder';
const types = { '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'text/javascript', '.py': 'text/plain; charset=utf-8', '.png': 'image/png', '.gif': 'image/gif', '.jpg': 'image/jpeg', '.svg': 'image/svg+xml', '.json': 'application/json', '.yml': 'text/plain' };
http.createServer((req, res) => {
  let u = decodeURIComponent(req.url.split('?')[0]);
  if (!u.startsWith(BASE)) { res.writeHead(302, { Location: BASE + '/' }); return res.end(); }
  let p = path.join(SITE, u.slice(BASE.length));
  if (fs.existsSync(p) && fs.statSync(p).isDirectory()) p = path.join(p, 'index.html');
  if (!fs.existsSync(p)) { res.writeHead(404); return res.end('404 ' + u); }
  res.writeHead(200, { 'Content-Type': types[path.extname(p)] || 'application/octet-stream' });
  fs.createReadStream(p).pipe(res);
}).listen(+process.env.PORT || 4000, () => console.log('→ http://localhost:' + (process.env.PORT || 4000) + BASE + '/'));
