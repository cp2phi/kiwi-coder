/* 🎉 网站上的小互动：任务清单、猜一猜、彩带、颜色盘、提示词配方、徽章、进度 */
(function () {
  'use strict';

  function store(key, val) {
    try {
      if (val === undefined) return localStorage.getItem(key);
      localStorage.setItem(key, val);
    } catch (e) { return null; }
  }
  function readJSON(key, fallback) { try { return JSON.parse(store(key) || '') || fallback; } catch (e) { return fallback; } }
  function both(zh, en) { return '<span class="zh">' + zh + '</span><span class="en">' + en + '</span>'; }

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

  // ---------- 小提示条（右下角冒出来） ----------
  function toast(html, ms) {
    var box = document.getElementById('kc-toast');
    if (!box) return;
    var t = document.createElement('div');
    t.className = 'toast';
    t.innerHTML = html;
    box.appendChild(t);
    setTimeout(function () { t.classList.add('show'); }, 10);
    setTimeout(function () { t.classList.remove('show'); setTimeout(function () { t.remove(); }, 400); }, ms || 3500);
  }
  window.kcToast = toast;

  // ---------- 徽章：过关 / 完成任务时颁发，存在这台电脑上 ----------
  // KC.badge('maze-1') 颁发；KC.badges() 查看；页面上 [data-badge-id="maze-1"] 的元素会自动加 .earned
  var BADGES = readJSON('kc-badges', {});
  // label：[中文, English]，提示条里显示它（没有就显示 id）
  function badge(id, label) {
    if (!id) return;
    var fresh = !BADGES[id];
    if (fresh) {
      BADGES[id] = new Date().toISOString();
      store('kc-badges', JSON.stringify(BADGES));
      var lz = label ? label[0] : id, le = label ? (label[1] || label[0]) : id;
      toast('🏅 ' + both('新徽章：<b>' + lz + '</b>！去首页看看你的徽章架', 'New badge: <b>' + le + '</b>! Check your badge shelf on the home page'), 4500);
    }
    markBadges();
    document.dispatchEvent(new CustomEvent('kc-badge', { detail: { id: id, fresh: fresh } }));
  }
  function markBadges() {
    document.querySelectorAll('[data-badge-id]').forEach(function (el) {
      var id = el.getAttribute('data-badge-id');
      el.classList.toggle('earned', !!BADGES[id]);
      var when = el.querySelector('.when');
      if (when && BADGES[id]) when.textContent = BADGES[id].slice(0, 10);
    });
    document.querySelectorAll('[data-badge-count]').forEach(function (el) {
      var prefix = el.getAttribute('data-badge-count');
      var n = Object.keys(BADGES).filter(function (k) { return !prefix || k.indexOf(prefix + '-') === 0; }).length;
      el.textContent = n;
    });
    var shelf = document.querySelector('.badge-shelf-empty');
    if (shelf) shelf.style.display = Object.keys(BADGES).length ? 'none' : '';
  }
  window.KC = window.KC || {};
  KC.badge = badge;
  KC.badges = function () { return BADGES; };

  // ---------- 任务清单 ----------
  // <ul class="quests" data-key="l1"><li>...</li></ul>
  var PROGRESS = readJSON('kc-progress', {});
  document.querySelectorAll('.quests').forEach(function (ul) {
    var k = ul.getAttribute('data-key') || location.pathname;
    var key = 'kc-quest-' + k;
    var saved = readJSON(key, {});
    var items = ul.querySelectorAll(':scope > li');
    var bar = document.querySelector('.progress[data-for="' + k + '"] > span');
    var label = document.querySelector('.progress-label[data-for="' + k + '"]');
    function update(celebrate) {
      var done = ul.querySelectorAll(':scope > li.done').length;
      if (bar) bar.style.width = (done / items.length * 100) + '%';
      if (label) label.textContent = done + ' / ' + items.length;
      // 课程主清单（data-key="l3" 这种）记到总进度里，首页地图会显示
      if (/^l\d+$/.test(k)) { PROGRESS[k] = [done, items.length]; store('kc-progress', JSON.stringify(PROGRESS)); }
      if (celebrate && done === items.length) { confetti(140); if (/^l\d+$/.test(k)) badge('lesson-' + k.slice(1), ['第 ' + k.slice(1) + ' 课完成', 'Lesson ' + k.slice(1) + ' done']); }
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
        if (e.target.closest('a, button, input, .pg, details')) return;
        li.classList.toggle('done');
        saved[i] = li.classList.contains('done');
        store(key, JSON.stringify(saved));
        if (saved[i]) confetti(18);
        update(saved[i]);
      });
    });
    update(false);
  });
  // 地图上的小进度条
  document.querySelectorAll('[data-lesson-progress]').forEach(function (el) {
    var p = PROGRESS['l' + el.getAttribute('data-lesson-progress')];
    var bar = el.querySelector('i');
    if (p && p[1]) { bar.style.width = Math.round(p[0] / p[1] * 100) + '%'; el.classList.add('has'); if (p[0] === p[1]) el.classList.add('full'); }
  });

  // ---------- 猜一猜 ----------
  // <div class="quiz" data-answer="2"><p class="q">问题</p><div class="opts"><button>A</button>...</div><div class="why">解释</div></div>
  document.querySelectorAll('.quiz').forEach(function (q) {
    var ans = +q.getAttribute('data-answer');
    var btns = q.querySelectorAll('.opts button');
    btns.forEach(function (b, i) {
      b.type = 'button';
      b.addEventListener('click', function () {
        if (q.classList.contains('answered')) return;
        if (i + 1 === ans) {
          b.classList.remove('wrong');
          b.classList.add('right');
          q.classList.add('answered');
          confetti(30);
          var bid = q.getAttribute('data-badge');
          if (bid) { var qq = q.querySelector('.q'); badge(bid, qq ? [((qq.querySelector('.zh') || qq).textContent || '').slice(0, 24), ((qq.querySelector('.en') || qq).textContent || '').slice(0, 30)] : null); }
          document.dispatchEvent(new CustomEvent('kc-quiz-right', { detail: { quiz: q } }));
        } else {
          b.classList.remove('wrong'); void b.offsetWidth; b.classList.add('wrong');
          q.classList.add('tried');
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

  // ---------- 指令卡片：点一下复制指令 ----------
  document.querySelectorAll('.cmd code').forEach(function (c) {
    c.title = 'Copy';
    c.style.cursor = 'copy';
    c.addEventListener('click', function () {
      if (navigator.clipboard) navigator.clipboard.writeText(c.textContent).catch(function () {});
      toast('📋 ' + both('复制好了：', 'Copied: ') + '<code>' + c.textContent.replace(/</g, '&lt;') + '</code>', 1500);
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

  // ---------- 提示词配方（第 1 课的 AI 画画 + 其他课可复用） ----------
  document.querySelectorAll('.recipe').forEach(function (recipe) {
    var f = function (n) { return recipe.querySelector('[name="' + n + '"]'); };
    var out = recipe.querySelector('.result');
    var en = function () { return window.KC && KC.lang() === 'en'; };
    var shown = function (el) { var s = el.querySelector(en() ? '.en' : '.zh'); return (s || el).textContent; };
    var score = recipe.querySelector('.score');
    var kind = recipe.getAttribute('data-kind') || 'draw';
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
      var what = (f('what') || {}).value || '', detail = (f('detail') || {}).value || '', colors = (f('colors') || {}).value || '', extra = (f('extra') || {}).value || '';
      what = what.trim(); detail = detail.trim(); colors = colors.trim(); extra = extra.trim();
      var stars = 0;
      var E = en();
      var lines = [E ? "I'm a Year 6 student learning Python." : '我是小学 6 年级的学生，正在学 Python。'];
      if (kind === 'draw') {
        if (what) { lines.push((E ? 'Please write a turtle program that draws: ' : '请帮我写一个 turtle 海龟程序，画：') + what + (E ? '.' : '。')); stars++; }
        if (detail) { lines.push((E ? 'Details: ' : '细节：') + detail + (E ? '.' : '。')); stars++; }
        if (colors) { lines.push((E ? 'Colours: ' : '颜色：') + colors + (E ? '.' : '。')); stars++; }
        lines.push(E ? 'Rules:' : '要求：');
        lines.push(E ? '1. Only use the turtle, random and math modules (I run it in a web playground)' : '1. 只用 turtle、random、math 这几个模块（我在网页画板里运行）');
        lines.push(E ? '2. No more than 40 lines, with a short simple comment on each line' : '2. 代码不超过 40 行，每一行加简单的中文注释');
        lines.push(E ? '3. Make the turtle with t = turtle.Turtle(); the canvas is about 600 x 600' : '3. 用 t = turtle.Turtle() 创建海龟，画布大小大约 600 x 600');
      } else {
        if (what) { lines.push((E ? 'Please write a small text program that: ' : '请帮我写一个小程序：') + what + (E ? '.' : '。')); stars++; }
        if (detail) { lines.push((E ? 'Details: ' : '细节：') + detail + (E ? '.' : '。')); stars++; }
        if (colors) { lines.push((E ? 'It should use: ' : '要用到：') + colors + (E ? '.' : '。')); stars++; }
        lines.push(E ? 'Rules:' : '要求：');
        lines.push(E ? '1. Only use print, input, random and the Python I already know (variables, if, for, while, lists, functions)' : '1. 只用 print、input、random 和我学过的 Python（变量、if、for、while、列表、函数）');
        lines.push(E ? '2. No more than 40 lines, with a short simple comment on each line' : '2. 代码不超过 40 行，每一行加简单的中文注释');
        lines.push(E ? '3. No files, no internet, no extra modules' : '3. 不要用文件、网络和其他模块');
      }
      if (extra) { lines.push('4. ' + extra); stars++; }
      lines.push(E ? 'When you are done, tell me which 2 lines would be the most fun to change.' : '写完以后，告诉我哪 2 行改了会最好玩。');
      if (out) out.textContent = lines.join('\n');
      var msg = E
        ? ['First write what to make ✏️', '⭐ Good start — add some details?', '⭐⭐ Nice! One more detail helps', '⭐⭐⭐ Very clear!', '⭐⭐⭐⭐ Super clear instructions! The AI will get it']
        : ['先写「做什么」吧 ✏️', '⭐ 有点意思，再加点细节？', '⭐⭐ 不错！再说清楚一点会更好', '⭐⭐⭐ 很清楚了！', '⭐⭐⭐⭐ 超级清楚的指令！AI 一定能懂'];
      if (score) score.textContent = msg[stars];
    };
    recipe.addEventListener('input', build);
    document.addEventListener('kc-lang', build);
    var copyBtn = recipe.querySelector('.copy-prompt');
    if (copyBtn) copyBtn.addEventListener('click', function () {
      var t = out.textContent;
      var old = copyBtn.innerHTML;
      var ok = function () { copyBtn.innerHTML = '<span class="zh">✅ 复制好了，去粘贴给 AI 吧！</span><span class="en">✅ Copied — now paste it to the AI!</span>'; setTimeout(function () { copyBtn.innerHTML = old; }, 2000); };
      if (navigator.clipboard) navigator.clipboard.writeText(t).then(ok, function () { window.prompt('Copy:', t); });
      else window.prompt('Copy:', t);
    });
    build();
  });

  // ---------- 「复制这段话」按钮：<button class="copy-text" data-text="…">  或  紧跟在 <pre> 后面的 <button class="copy-prev"> ----------
  document.querySelectorAll('.copy-text, .copy-prev').forEach(function (b) {
    b.type = 'button';
    b.addEventListener('click', function () {
      var t = b.getAttribute('data-text') || '';
      if (b.classList.contains('copy-prev')) {
        // 往前找第一个「看得见」的元素（中英两个版本叠在一起时，复制当前语言那一个）
        // Markdown 会把按钮包进 <p>，这时从 <p> 往前找
        var from = b;
        if (!b.previousElementSibling && b.parentElement && b.parentElement.tagName === 'P') from = b.parentElement;
        var prev = from.previousElementSibling;
        while (prev && getComputedStyle(prev).display === 'none') prev = prev.previousElementSibling;
        t = prev ? prev.textContent : '';
      }
      if (navigator.clipboard) navigator.clipboard.writeText(t).catch(function () {});
      toast('📋 ' + both('复制好了！', 'Copied!'), 1500);
    });
  });

  // ---------- 第一次运行成功的时候撒彩带 ----------
  document.addEventListener('kc-run-ok', function () {
    if (!window.__kcFirstRun) { window.__kcFirstRun = true; confetti(90); }
  });

  // ---------- 本周课程提醒 ----------
  markBadges();
})();
