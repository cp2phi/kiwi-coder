---
title: 作品墙
title_en: Gallery
playground: true
---

# 🎨 <span class="zh">我的作品墙</span><span class="en">My Gallery</span>

<p><span class="zh">放进 <code>my-work/</code> 文件夹的每一个 <code>.py</code> 文件都会出现在这里——<b>存完刷新就能看到</b>，不用等。点一张卡片就能运行、改代码！</span><span class="en">Every <code>.py</code> file in the <code>my-work/</code> folder shows up here — <b>save it, refresh, and it's here</b>. Click a card to run it or change the code!</span></p>

<div class="gallery-head">
  <button class="pg-btn" id="g-refresh">🔄 <span class="zh">刷新</span><span class="en">Refresh</span></button>
  <button class="pg-btn" id="g-thumbs">🖼️ <span class="zh">生成缩略图</span><span class="en">Make thumbnails</span></button>
  <span class="gallery-filters" id="g-filters">
    <button class="on" data-f="all"><span class="zh">全部</span><span class="en">All</span></button>
    <button data-f="hw"><span class="zh">作业</span><span class="en">Homework</span></button>
    <button data-f="free"><span class="zh">自由作品</span><span class="en">Free work</span></button>
  </span>
  <span class="gallery-status" id="g-status"></span>
</div>

<div class="gallery-grid" id="g-grid">
{% assign works = site.static_files | where: "extname", ".py" | sort: "path" | reverse %}
{% for f in works %}{% if f.path contains '/my-work/' %}
  <div class="work" data-name="{{ f.name }}" data-src="{{ f.path | relative_url }}" data-static="1">
    <div class="thumb"><span class="ph">🐢</span></div>
    <div class="info"><b>{{ f.basename }}</b><small>{{ f.name }}</small></div>
  </div>
{% endif %}{% endfor %}
</div>

<div class="card" id="g-empty" style="text-align:center;display:none"><div class="big-emoji">🖼️</div><p><span class="zh">作品墙还是空的。去 <a href="{{ '/playground/' | relative_url }}">画板</a> 做一个吧！</span><span class="en">The gallery is empty. Go make something in the <a href="{{ '/playground/' | relative_url }}">Playground</a>!</span></p></div>

<div class="box box-tip"><span class="box-title"><span class="zh">➕ 怎么加新作品？</span><span class="en">➕ How do I add something?</span></span>
<span class="zh"><b>最简单：</b>在任何画板上点 <b>📤 存到作品墙</b>，在 GitHub 页面点 <b>Commit changes</b>，回来刷新。<br>
<b>或者：</b>在 GitHub 打开 <a href="https://github.com/{{ site.github_repo }}/tree/{{ site.github_branch }}/my-work" target="_blank" rel="noopener">my-work 文件夹</a> → <b>Add file</b> → <b>Create new file</b> / <b>Upload files</b>。<br>
<b>小技巧：</b>代码的<b>第一行</b>写 <code># 🌈 作品名字</code>，作品墙就会用它当标题。作业用 <code>weekNN-homework</code> 当文件名，会自动标上「作业」。</span>
<span class="en"><b>Easiest:</b> click <b>📤 Save to Gallery</b> on any playground, click <b>Commit changes</b> on GitHub, come back and refresh.<br>
<b>Or:</b> open the <a href="https://github.com/{{ site.github_repo }}/tree/{{ site.github_branch }}/my-work" target="_blank" rel="noopener">my-work folder</a> on GitHub → <b>Add file</b> → <b>Create new file</b> / <b>Upload files</b>.<br>
<b>Tip:</b> write <code># 🌈 My title</code> on the <b>first line</b> and the gallery uses it as the title. Name homework <code>weekNN-homework</code> and it gets a "homework" tag.</span>
</div>

<script>
(function () {
  var grid = document.getElementById('g-grid');
  var status = document.getElementById('g-status');
  var empty = document.getElementById('g-empty');
  var base = (window.KC && KC.base) || '';
  var THUMBS = {};
  try { THUMBS = JSON.parse(localStorage.getItem('kc-thumbs') || '{}'); } catch (e) {}
  function both(zh, en) { return '<span class="zh">' + zh + '</span><span class="en">' + en + '</span>'; }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function titleOf(code, name) {
    var first = (code.split('\n')[0] || '').trim();
    var m = /^#\s*(.+)$/.exec(first);
    var t = m ? m[1].replace(/\s*\(.*?\)\s*$/, '').trim() : name.replace(/\.py$/, '');
    return t.length > 60 ? t.slice(0, 60) + '…' : t;
  }
  function hwOf(name) { var m = /^week(\d\d)/.exec(name); return m ? +m[1] : null; }
  function setStatus(zh, en) { status.innerHTML = both(zh, en); }

  // 一张卡片
  function card(f) {
    var c = grid.querySelector('.work[data-name="' + f.name + '"]');
    if (!c) {
      c = document.createElement('div');
      c.className = 'work';
      c.setAttribute('data-name', f.name);
      c.innerHTML = '<div class="thumb"><span class="ph">🐢</span></div><div class="info"><b>' + esc(f.name.replace(/\.py$/, '')) + '</b><small>' + esc(f.name) + '</small></div>';
      grid.insertBefore(c, grid.firstChild);
      c.querySelector('.thumb').insertAdjacentHTML('beforeend', '<span class="new">NEW</span>');
    }
    c.setAttribute('data-sha', f.sha || '');
    c.file = f;
    var hw = hwOf(f.name);
    c.setAttribute('data-kind', hw ? 'hw' : 'free');
    var info = c.querySelector('.info');
    if (hw && !info.querySelector('.tag')) info.insertAdjacentHTML('beforeend', '<span class="tag hw">📅 ' + both('第 ' + hw + ' 课作业', 'Lesson ' + hw + ' homework') + '</span>');
    var th = THUMBS[f.sha];
    if (th) c.querySelector('.thumb').innerHTML = th.indexOf('data:image') === 0 ? '<img src="' + th + '" alt="">' : '<pre>' + esc(th) + '</pre>';
    c.onclick = function (e) { if (!c.classList.contains('open') && !e.target.closest('.viewer')) open(c); };
    return c;
  }

  // 点开一张卡片：里面出现画板
  var opened = null;
  function open(c) {
    if (opened) close(opened);
    opened = c;
    c.classList.add('open');
    var f = c.file;
    var v = document.createElement('div');
    v.className = 'viewer';
    v.innerHTML = '<div class="viewer-bar"><b>' + esc(c.querySelector('.info b').textContent) + '</b>' +
      '<a class="pg-btn" target="_blank" rel="noopener" href="https://github.com/' + KC.repo + '/edit/' + KC.branch + '/my-work/' + encodeURIComponent(f.name) + '">✏️ ' + both('在 GitHub 上改', 'Edit on GitHub') + '</a>' +
      '<button class="pg-btn g-close">✕ ' + both('关闭', 'Close') + '</button></div>' +
      '<div class="playground" data-title="' + esc(f.name) + '" data-save="' + esc(f.name.replace(/\.py$/, '')) + '"></div>';
    c.appendChild(v);
    v.querySelector('.g-close').onclick = function (e) { e.stopPropagation(); close(c); };
    var pgEl = v.querySelector('.playground');
    var pg = new KCPlayground(pgEl);
    (f.sha ? KCGit.read(f) : fetch(c.getAttribute('data-src')).then(function (r) { return r.text(); })).then(function (code) {
      pg.initial = code; pg.setCode(code);
      pg.run();
      // 跑完以后顺手存一张缩略图
      var done = function () {
        document.removeEventListener('kc-run-ok', done);
        setTimeout(function () { var s = pg.snapshot(240); if (s && f.sha) { THUMBS[f.sha] = s; saveThumbs(); c.querySelector('.thumb').innerHTML = '<img src="' + s + '" alt="">'; } }, 200);
      };
      document.addEventListener('kc-run-ok', done);
    });
    c.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
  function close(c) {
    var v = c.querySelector('.viewer');
    if (v) { try { if (window.Sk && Sk.TurtleGraphics && Sk.TurtleGraphics.reset) Sk.TurtleGraphics.reset(); } catch (e) {} v.remove(); }
    c.classList.remove('open');
    if (opened === c) opened = null;
  }
  function saveThumbs() {
    try { localStorage.setItem('kc-thumbs', JSON.stringify(THUMBS)); } catch (e) {
      // 存不下了：只留最近 12 张
      var keys = Object.keys(THUMBS); while (keys.length > 12) delete THUMBS[keys.shift()];
      try { localStorage.setItem('kc-thumbs', JSON.stringify(THUMBS)); } catch (e2) {}
    }
  }

  // 读 GitHub：有新文件就加进来，标题从第一行注释读
  var FILES = [];
  function refresh(force) {
    setStatus('⏳ 正在从 GitHub 读取…', '⏳ Loading from GitHub…');
    return KCGit.list(force).then(function (files) {
      FILES = files;
      var names = {};
      files.forEach(function (f) { names[f.name] = 1; card(f); });
      // GitHub 上已经删掉的，这里也拿掉
      grid.querySelectorAll('.work').forEach(function (c) { if (!names[c.getAttribute('data-name')]) c.remove(); });
      // 按文件名倒序（新作业在前）
      Array.prototype.slice.call(grid.querySelectorAll('.work')).sort(function (a, b) { return a.getAttribute('data-name') < b.getAttribute('data-name') ? 1 : -1; }).forEach(function (c) { grid.appendChild(c); });
      empty.style.display = files.length ? 'none' : '';
      setStatus('✅ ' + files.length + ' 个作品（GitHub 实时）', '✅ ' + files.length + ' works (live from GitHub)');
      // 标题
      files.forEach(function (f) {
        KCGit.read(f).then(function (code) {
          var c = grid.querySelector('.work[data-name="' + f.name + '"]');
          if (c) { c.querySelector('.info b').textContent = titleOf(code, f.name); c.code = code; }
        }).catch(function () {});
      });
      applyFilter();
    }).catch(function (e) {
      setStatus('⚠️ 读不到 GitHub（' + e.message + '），显示的是上次发布时的作品。', '⚠️ Could not reach GitHub (' + e.message + '); showing works from the last site build.');
      var statics = grid.querySelectorAll('.work[data-static]');
      empty.style.display = statics.length ? 'none' : '';
      statics.forEach(function (c) { c.file = { name: c.getAttribute('data-name') }; c.onclick = function (e) { if (!c.classList.contains('open') && !e.target.closest('.viewer')) open(c); }; });
    });
  }

  // 一键生成所有缩略图：一个接一个地跑（最多 6 秒一个）
  function makeThumbs() {
    var cards = Array.prototype.slice.call(grid.querySelectorAll('.work')).filter(function (c) { return c.file && c.file.sha && !THUMBS[c.file.sha]; });
    if (!cards.length) { setStatus('✅ 缩略图都有了', '✅ All thumbnails are ready'); return; }
    var box = document.createElement('div');
    box.className = 'playground'; box.style.position = 'fixed'; box.style.left = '-9999px'; box.style.width = '600px';
    document.body.appendChild(box);
    var pg = new KCPlayground(box);
    var i = 0;
    function next() {
      if (i >= cards.length) { try { Sk.TurtleGraphics.reset(); } catch (e) {} box.remove(); setStatus('✅ 缩略图做好了', '✅ Thumbnails done'); return; }
      var c = cards[i++];
      setStatus('🖼️ 正在画 ' + i + ' / ' + cards.length + '：' + c.file.name, '🖼️ Drawing ' + i + ' / ' + cards.length + ': ' + c.file.name);
      KCGit.read(c.file).then(function (code) {
        // 把速度调到最快，省时间
        code = code.replace(/\.speed\(\s*[^)]*\)/g, '.speed(0)');
        pg.setCode(code);
        var finished = false;
        var finish = function () {
          if (finished) return; finished = true;
          document.removeEventListener('kc-run-ok', finish); document.removeEventListener('kc-run-error', finish);
          setTimeout(function () {
            var s = pg.snapshot(240);
            var out = pg.out.textContent.trim();
            var th = (s && pg.canvasEl.querySelector('canvas')) ? s : (out ? out.slice(0, 300) : null);
            if (th) { THUMBS[c.file.sha] = th; saveThumbs(); c.querySelector('.thumb').innerHTML = th.indexOf('data:image') === 0 ? '<img src="' + th + '" alt="">' : '<pre>' + esc(th) + '</pre>'; }
            pg.stop(); next();
          }, 150);
        };
        document.addEventListener('kc-run-ok', finish);
        document.addEventListener('kc-run-error', finish);
        setTimeout(finish, 6000);
        pg.run();
      }, next);
    }
    // 程序要 input() 的话，自动回答
    pg.askInput = function (prompt, myRun) { pg.out.textContent += (prompt || '') + '5\n'; return Promise.resolve('5'); };
    next();
  }

  var filter = 'all';
  function applyFilter() {
    grid.querySelectorAll('.work').forEach(function (c) {
      var k = c.getAttribute('data-kind') || (hwOf(c.getAttribute('data-name')) ? 'hw' : 'free');
      c.style.display = (filter === 'all' || filter === k) ? '' : 'none';
    });
  }
  document.getElementById('g-filters').addEventListener('click', function (e) {
    var b = e.target.closest('button'); if (!b) return;
    filter = b.getAttribute('data-f');
    this.querySelectorAll('button').forEach(function (x) { x.classList.toggle('on', x === b); });
    applyFilter();
  });
  document.getElementById('g-refresh').onclick = function () { refresh(true); };
  document.getElementById('g-thumbs').onclick = makeThumbs;

  document.addEventListener('DOMContentLoaded', function () {
    refresh(false).then(function () {
      // 网址后面带 #文件名 就直接打开它
      var h = decodeURIComponent(location.hash.slice(1));
      if (h) { var c = grid.querySelector('.work[data-name="' + h + '"]'); if (c) open(c); }
    });
  });
})();
</script>
