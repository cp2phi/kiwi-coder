/* 🎉 网站上的小互动：任务清单、猜一猜、彩带、颜色盘、提示词配方 */
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
          b.classList.remove('wrong');
          b.classList.add('right');
          q.classList.add('answered');
          confetti(30);
        } else {
          b.classList.remove('wrong'); void b.offsetWidth; b.classList.add('wrong');
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
      b.title = 'Copy';
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
    var en = function () { return window.KC && KC.lang() === 'en'; };
    // 按钮里有中英两种文字，取现在显示的那一种
    var shown = function (el) { var s = el.querySelector(en() ? '.en' : '.zh'); return (s || el).textContent; };
    var score = recipe.querySelector('.score');
    recipe.querySelectorAll('.chips').forEach(function (chips) {
      var target = f(chips.getAttribute('data-for'));
      chips.querySelectorAll('.chip').forEach(function (c) {
        c.type = 'button';
        c.addEventListener('click', function () {
          if (chips.hasAttribute('data-multi')) {
            c.classList.toggle('on');
            target.value = Array.prototype.map.call(chips.querySelectorAll('.chip.on'), function (x) { return shown(x); }).join(en() ? ', ' : '、');
          } else {
            target.value = shown(c);
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
      var E = en();
      var lines = [E ? "I'm a Year 6 student learning Python turtle drawing." : '我是小学 6 年级的学生，正在学 Python 的 turtle 海龟画画。'];
      if (what) { lines.push((E ? 'Please write a program that draws: ' : '请帮我写一个程序，画：') + what + (E ? '.' : '。')); stars++; }
      if (detail) { lines.push((E ? 'Details: ' : '细节：') + detail + (E ? '.' : '。')); stars++; }
      if (colors) { lines.push((E ? 'Colours: ' : '颜色：') + colors + (E ? '.' : '。')); stars++; }
      if (E) {
        lines.push('Rules:');
        lines.push('1. Only use the turtle, random and math modules (I run it in a web playground)');
        lines.push('2. No more than 40 lines, with a short simple comment on each line');
        lines.push('3. Make the turtle with t = turtle.Turtle(); the canvas is about 600 x 600');
      } else {
        lines.push('要求：');
        lines.push('1. 只用 turtle、random、math 这几个模块（我在网页画板里运行）');
        lines.push('2. 代码不超过 40 行，每一行加简单的中文注释');
        lines.push('3. 用 t = turtle.Turtle() 创建海龟，画布大小大约 600 x 600');
      }
      if (extra) { lines.push('4. ' + extra); stars++; }
      lines.push(E ? 'When you are done, tell me which 2 numbers would be the most fun to change.' : '写完以后，告诉我哪 2 个数字改了会最好玩。');
      out.textContent = lines.join('\n');
      var msg = E
        ? ['First write what to draw ✏️', '⭐ Good start — add some details?', '⭐⭐ Nice! Saying the colours helps too', '⭐⭐⭐ Very clear!', '⭐⭐⭐⭐ Super clear instructions! The AI will get it']
        : ['先写「画什么」吧 ✏️', '⭐ 有点意思，再加点细节？', '⭐⭐ 不错！说清楚颜色会更好', '⭐⭐⭐ 很清楚了！', '⭐⭐⭐⭐ 超级清楚的指令！AI 一定能懂'];
      score.textContent = msg[stars];
    };
    recipe.addEventListener('input', build);
    document.addEventListener('kc-lang', build);
    var copyBtn = recipe.querySelector('.copy-prompt');
    if (copyBtn) copyBtn.addEventListener('click', function () {
      var t = out.textContent;
      var old = copyBtn.innerHTML;
      var ok = function () { copyBtn.innerHTML = '<span class="zh">✅ 复制好了，去粘贴给 Codex 吧！</span><span class="en">✅ Copied — now paste it into Codex!</span>'; setTimeout(function () { copyBtn.innerHTML = old; }, 2000); };
      if (navigator.clipboard) navigator.clipboard.writeText(t).then(ok, function () { window.prompt('Copy:', t); });
      else window.prompt('Copy:', t);
    });
    build();
  }

  // 第一次运行成功的时候撒彩带
  document.addEventListener('kc-run-ok', function () {
    if (!window.__kcFirstRun) { window.__kcFirstRun = true; confetti(90); }
  });
})();
