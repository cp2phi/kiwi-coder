/* 🎉 网站上的小互动：任务清单、猜一猜、彩带、颜色盘、提示词配方、角度实验室 */
(function () {
  'use strict';

  function store(key, val) {
    try {
      if (val === undefined) return localStorage.getItem(key);
      localStorage.setItem(key, val);
    } catch (e) { return null; }
  }

  // ---------- 彩带 ----------
  var COLORS = ['#ef4444', '#f59e0b', '#10b981', '#3b82f6', '#8b5cf6', '#ec4899', '#facc15'];
  function confetti(n) {
    var layer = document.getElementById('confetti-layer');
    if (!layer) return;
    for (var i = 0; i < (n || 80); i++) {
      var p = document.createElement('i');
      p.style.left = Math.random() * 100 + 'vw';
      p.style.background = COLORS[i % COLORS.length];
      p.style.animationDuration = 1.8 + Math.random() * 1.8 + 's';
      p.style.animationDelay = Math.random() * 0.4 + 's';
      p.style.transform = 'rotate(' + Math.random() * 360 + 'deg)';
      layer.appendChild(p);
      setTimeout(function (el) { el.remove(); }.bind(null, p), 4200);
    }
  }
  window.kcConfetti = confetti;

  // ---------- 任务清单 ----------
  // <ul class="quests" data-key="l1"><li>...</li></ul>
  document.querySelectorAll('.quests').forEach(function (ul) {
    var key = 'kc-quest-' + (ul.getAttribute('data-key') || location.pathname);
    var saved = {};
    try { saved = JSON.parse(store(key) || '{}'); } catch (e) {}
    var items = ul.querySelectorAll(':scope > li');
    var bar = document.querySelector('.progress[data-for="' + ul.getAttribute('data-key') + '"] > span');
    var label = document.querySelector('.progress-label[data-for="' + ul.getAttribute('data-key') + '"]');
    function update(celebrate) {
      var done = ul.querySelectorAll(':scope > li.done').length;
      if (bar) bar.style.width = (done / items.length * 100) + '%';
      if (label) label.textContent = done + ' / ' + items.length;
      if (celebrate && done === items.length) confetti(140);
    }
    items.forEach(function (li, i) {
      var body = document.createElement('div');
      body.className = 'q-body';
      while (li.firstChild) body.appendChild(li.firstChild);
      var box = document.createElement('span');
      box.className = 'check';
      li.appendChild(box);
      li.appendChild(body);
      if (saved[i]) li.classList.add('done');
      li.addEventListener('click', function (e) {
        if (e.target.closest('a')) return;
        li.classList.toggle('done');
        saved[i] = li.classList.contains('done');
        store(key, JSON.stringify(saved));
        if (saved[i]) confetti(18);
        update(saved[i]);
      });
    });
    update(false);
  });

  // ---------- 猜一猜 ----------
  // <div class="quiz" data-answer="2"><p class="q">问题</p><div class="opts"><button>A</button>...</div><div class="why">解释</div></div>
  document.querySelectorAll('.quiz').forEach(function (q) {
    var ans = +q.getAttribute('data-answer');
    var btns = q.querySelectorAll('.opts button');
    btns.forEach(function (b, i) {
      b.addEventListener('click', function () {
        if (i + 1 === ans) {
          b.classList.add('right');
          b.textContent = '✅ ' + b.textContent.replace(/^❌ /, '');
          q.classList.add('answered');
          confetti(30);
        } else {
          b.classList.remove('wrong'); void b.offsetWidth; b.classList.add('wrong');
          if (!/^❌/.test(b.textContent)) b.textContent = '❌ ' + b.textContent;
        }
      });
    });
    var giveUp = q.querySelector('.give-up');
    if (giveUp) giveUp.addEventListener('click', function () { q.classList.add('answered'); });
  });

  // ---------- 颜色盘：点一下复制颜色名 ----------
  document.querySelectorAll('.swatches').forEach(function (box) {
    (box.getAttribute('data-colors') || '').split(/\s+/).filter(Boolean).forEach(function (c) {
      var b = document.createElement('button');
      b.className = 'swatch';
      b.type = 'button';
      b.innerHTML = '<i style="background:' + c + '"></i>"' + c + '"';
      b.title = '点一下复制';
      b.addEventListener('click', function () {
        var txt = '"' + c + '"';
        if (navigator.clipboard) navigator.clipboard.writeText(txt).catch(function () {});
        b.classList.add('copied');
        setTimeout(function () { b.classList.remove('copied'); }, 900);
      });
      box.appendChild(b);
    });
  });

  // ---------- 首页头像：点一点会转 ----------
  var av = document.querySelector('.hero-avatar');
  if (av) {
    var clicks = 0;
    av.addEventListener('click', function () {
      clicks++;
      av.animate([{ transform: 'rotate(0) scale(1)' }, { transform: 'rotate(360deg) scale(1.2)' }, { transform: 'rotate(360deg) scale(1)' }], { duration: 600 });
      if (clicks % 5 === 0) confetti(100);
    });
  }

  // ---------- 提示词配方 ----------
  var recipe = document.querySelector('.recipe');
  if (recipe) {
    var f = function (n) { return recipe.querySelector('[name="' + n + '"]'); };
    var out = recipe.querySelector('.result');
    var score = recipe.querySelector('.score');
    recipe.querySelectorAll('.chips').forEach(function (chips) {
      var target = f(chips.getAttribute('data-for'));
      chips.querySelectorAll('.chip').forEach(function (c) {
        c.type = 'button';
        c.addEventListener('click', function () {
          if (chips.hasAttribute('data-multi')) {
            c.classList.toggle('on');
            target.value = Array.prototype.map.call(chips.querySelectorAll('.chip.on'), function (x) { return x.textContent; }).join('、');
          } else {
            target.value = c.textContent;
          }
          build();
        });
      });
    });
    var build = function () {
      var what = f('what').value.trim();
      var detail = f('detail').value.trim();
      var colors = f('colors').value.trim();
      var extra = f('extra').value.trim();
      var stars = 0;
      var lines = ['我是小学 6 年级的学生，正在学 Python 的 turtle 海龟画画。'];
      if (what) { lines.push('请帮我写一个程序，画：' + what + '。'); stars++; }
      if (detail) { lines.push('细节：' + detail + '。'); stars++; }
      if (colors) { lines.push('颜色：' + colors + '。'); stars++; }
      lines.push('要求：');
      lines.push('1. 只用 turtle、random、math 这几个模块（我在网页画板里运行）');
      lines.push('2. 代码不超过 40 行，每一行加简单的中文注释');
      lines.push('3. 用 t = turtle.Turtle() 创建海龟，画布大小大约 600 x 600');
      if (extra) { lines.push('4. ' + extra); stars++; }
      lines.push('写完以后，告诉我哪 2 个数字改了会最好玩。');
      out.textContent = lines.join('\n');
      var msg = ['先写「画什么」吧 ✏️', '⭐ 有点意思，再加点细节？', '⭐⭐ 不错！说清楚颜色会更好', '⭐⭐⭐ 很清楚了！', '⭐⭐⭐⭐ 超级清楚的指令！AI 一定能懂'];
      score.textContent = msg[stars];
    };
    recipe.addEventListener('input', build);
    var copyBtn = recipe.querySelector('.copy-prompt');
    if (copyBtn) copyBtn.addEventListener('click', function () {
      var t = out.textContent;
      var ok = function () { copyBtn.textContent = '✅ 复制好了，去粘贴给 Codex 吧！'; setTimeout(function () { copyBtn.textContent = '📋 复制这段指令'; }, 2000); };
      if (navigator.clipboard) navigator.clipboard.writeText(t).then(ok, function () { window.prompt('复制：', t); });
      else window.prompt('复制：', t);
    });
    build();
  }

  // ---------- 角度实验室：海龟转 X 度、走 N 次 ----------
  var lab = document.querySelector('.lab');
  if (lab) {
    var cv = lab.querySelector('canvas');
    var ctx = cv.getContext('2d');
    var ang = lab.querySelector('[name="angle"]');
    var rep = lab.querySelector('[name="repeat"]');
    var read = lab.querySelector('.readout');
    var draw = function () {
      var a = +ang.value, n = +rep.value;
      var W = cv.width, H = cv.height, step = 110;
      // 先算出路径，再居中
      var pts = [[0, 0]], x = 0, y = 0, h = 0;
      for (var i = 0; i < n; i++) {
        x += step * Math.cos(h * Math.PI / 180);
        y += step * Math.sin(h * Math.PI / 180);
        pts.push([x, y]);
        h -= a;
      }
      var xs = pts.map(function (p) { return p[0]; }), ys = pts.map(function (p) { return p[1]; });
      var minX = Math.min.apply(0, xs), maxX = Math.max.apply(0, xs), minY = Math.min.apply(0, ys), maxY = Math.max.apply(0, ys);
      var s = Math.min((W - 40) / Math.max(maxX - minX, 1), (H - 40) / Math.max(maxY - minY, 1), 1.6);
      var ox = W / 2 - (minX + maxX) / 2 * s, oy = H / 2 - (minY + maxY) / 2 * s;
      ctx.clearRect(0, 0, W, H);
      ctx.lineWidth = 4; ctx.lineJoin = 'round'; ctx.strokeStyle = getComputedStyle(document.documentElement).getPropertyValue('--brand') || '#16a34a';
      ctx.beginPath();
      pts.forEach(function (p, i) { var px = ox + p[0] * s, py = oy + p[1] * s; i ? ctx.lineTo(px, py) : ctx.moveTo(px, py); });
      ctx.stroke();
      var last = pts[pts.length - 1];
      ctx.font = '28px serif'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
      ctx.fillText('🐢', ox + last[0] * s, oy + last[1] * s);
      var closed = Math.abs(last[0]) < 0.5 && Math.abs(last[1]) < 0.5;
      read.innerHTML = '转 <b>' + a + '°</b> × 走 <b>' + n + '</b> 次 = 一共转了 <b>' + (a * n) + '°</b><br>' +
        (closed ? '🎉 回到起点了！图形合上了！' : '🔓 还没回到起点…');
    };
    ang.addEventListener('input', draw);
    rep.addEventListener('input', draw);
    lab.querySelectorAll('[data-preset]').forEach(function (b) {
      b.addEventListener('click', function () { var v = b.getAttribute('data-preset').split(','); ang.value = v[0]; rep.value = v[1]; draw(); });
    });
    draw();
  }

  // 第一次运行成功的时候撒彩带
  document.addEventListener('kc-run-ok', function () {
    if (!window.__kcFirstRun) { window.__kcFirstRun = true; confetti(90); }
  });
})();
