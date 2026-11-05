#!/usr/bin/env node
/* 🧪 用浏览器里的 Python（Skulpt）跑所有 .py 文件，确保教材代码都能运行
 *
 *   node tools/check-code.js                 跑 lessons/、games/、my-work/ 下所有 .py
 *   node tools/check-code.js lessons/03      只跑某个文件夹
 *   node tools/check-code.js path/to/x.py    只跑一个文件
 *
 * 规则：
 *   - 文件里有 ___（要孩子填的空）：报 NameError「___ 没填」算通过（标 🔲）
 *   - 文件开头 `# test-input: 5 | yes | 小海龟` 给 input() 喂答案（默认全部回答 5）
 *   - 文件开头 `# test-skip: 原因` 跳过
 *   - 文件开头 `# test-expect-error: ValueError` 期望报这种错（虫虫医院的病号代码）
 *   - 游戏的 prelude / check / target 文件（名字含 setup / check / target）单独不跑；
 *     同一文件夹里如果有 levelN-start.py + levelN-setup.py + levelN-check.py 会拼起来跑
 * 需要先 `cd tools && npm i`（装 playwright）。
 */
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
let chromium;
try { ({ chromium } = require(path.join(__dirname, 'node_modules', 'playwright'))); }
catch (e) { try { ({ chromium } = require('playwright')); } catch (e2) { console.error('先运行：cd tools && npm i'); process.exit(2); } }

function walk(p, acc) {
  const st = fs.statSync(p);
  if (st.isFile()) { if (p.endsWith('.py')) acc.push(p); return acc; }
  for (const f of fs.readdirSync(p)) {
    if (f === 'node_modules' || f.startsWith('.') || f === '_site') continue;
    walk(path.join(p, f), acc);
  }
  return acc;
}
const args = process.argv.slice(2);
const targets = (args.length ? args : ['lessons', 'games', 'my-work']).map(a => path.resolve(ROOT, a)).filter(fs.existsSync);
let files = [];
targets.forEach(t => walk(t, files));
files = [...new Set(files)].sort();

function header(code, key) {
  const m = new RegExp('^#\\s*' + key + ':\\s*(.*)$', 'm').exec(code.split('\n').slice(0, 8).join('\n'));
  return m ? m[1].trim() : null;
}
const isHidden = f => /(^|[-_])(setup|prelude|check|target)\.py$/.test(path.basename(f));

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  page.on('pageerror', e => console.log('  (page error) ' + e.message));
  await page.goto('file://' + path.join(__dirname, 'runner.html'));
  await page.waitForFunction(() => window.Sk && window.runPy, null, { timeout: 60000 });

  let pass = 0, fail = 0, skip = 0;
  const failures = [];
  for (const f of files) {
    const rel = path.relative(ROOT, f);
    let code = fs.readFileSync(f, 'utf8');
    if (isHidden(f)) continue;
    const skipWhy = header(code, 'test-skip');
    if (skipWhy) { console.log('⏭  ' + rel + '  (' + skipWhy + ')'); skip++; continue; }
    const inputs = (header(code, 'test-input') || '').split('|').map(s => s.trim()).filter(Boolean);
    const expectErr = header(code, 'test-expect-error');
    // 关卡：把 setup + start + check 拼起来
    const dir = path.dirname(f), base = path.basename(f, '.py');
    const m = /^(.*?)-(start|starter)$/.exec(base);
    let composed = code, note = '';
    if (m) {
      const pre = ['-setup.py', '-prelude.py'].map(s => path.join(dir, m[1] + s)).find(fs.existsSync);
      const chk = path.join(dir, m[1] + '-check.py');
      if (pre) composed = fs.readFileSync(pre, 'utf8') + '\n' + composed;
      if (fs.existsSync(chk)) composed = composed + '\n' + fs.readFileSync(chk, 'utf8');
      if (pre || fs.existsSync(chk)) note = '  (+setup/check)';
    }
    const hasBlank = /___/.test(code);
    const r = await page.evaluate(([c, i]) => window.runPy(c, i, 20000), [composed, inputs]);
    if (r.ok) {
      if (expectErr) { console.log('❌ ' + rel + '  期望报 ' + expectErr + ' 但正常跑完了'); fail++; failures.push(rel); }
      else { console.log('✅ ' + rel + note + (r.out.includes('__KC_WIN__') ? '  🏆win' : '')); pass++; }
    } else if (hasBlank && /name '_+' is not defined/.test(r.err)) {
      console.log('🔲 ' + rel + '  (有空要填，正常)'); pass++;
    } else if (expectErr && r.err.indexOf(expectErr) >= 0) {
      console.log('✅ ' + rel + '  (按预期报 ' + expectErr + ')'); pass++;
    } else {
      console.log('❌ ' + rel + note + '\n     ' + r.err.split('\n')[0] + (r.line ? '  [line ' + r.line + ']' : ''));
      fail++; failures.push(rel);
    }
  }
  await browser.close();
  console.log('\n' + pass + ' passed, ' + fail + ' failed, ' + skip + ' skipped' + (failures.length ? '\nFAILED:\n  ' + failures.join('\n  ') : ''));
  process.exit(fail ? 1 : 0);
})();
