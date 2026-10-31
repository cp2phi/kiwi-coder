/* 🐢 代码画板：在网页里运行 Python（turtle 海龟画画）
 * 用法（写在 .md 里）：
 *   <div class="playground" data-src="code/square.py" data-title="正方形" data-save="my-square"></div>
 *   data-src     起始代码文件（相对当前页面）
 *   data-canvas  "no" = 不需要海龟画布（只用 print）
 *   data-save    「存到作品墙」时默认的文件名
 *   data-draft   填一个名字 = 自动在这台电脑上记住没写完的代码
 */
(function () {
  'use strict';

  var active = null;
  var SIZE = 600;
  var PRAISE = ['太棒了！', '电脑听你的话了！', '漂亮！', '你真是个程序员！', '一次就跑通！', '海龟为你点赞 🐢👍'];

  function builtinRead(x) {
    if (Sk.builtinFiles === undefined || Sk.builtinFiles.files[x] === undefined) {
      throw "File not found: '" + x + "'";
    }
    return Sk.builtinFiles.files[x];
  }

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; });
  }

  function el(tag, cls, html) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html != null) e.innerHTML = html;
    return e;
  }

  // 把 Python 的报错翻译成小朋友看得懂的话
  function explain(type, msg, lineText) {
    var m;
    if (type === 'NameError' && (m = /name '(_+)' is not defined/.exec(msg))) {
      return '这里有个 <b>' + esc(m[1]) + '</b> 空格还没填哦！把它换成你想好的数字（或颜色）。';
    }
    if (type === 'NameError' && (m = /name '(.+?)' is not defined/.exec(msg))) {
      return '电脑不认识「<b>' + esc(m[1]) + '</b>」这个名字。检查一下：<br>① 拼写对吗？② 大小写对吗？（<code>Turtle</code> 和 <code>turtle</code> 不一样）<br>③ 如果是文字，记得用引号包起来，比如 <code>"red"</code>。';
    }
    if (/[（）：，“”‘’；。！]/.test(lineText || '') && (type === 'SyntaxError' || type === 'ParseError' || type === 'TokenError')) {
      var ch = (lineText.match(/[（）：，“”‘’；。！]/) || [''])[0];
      return '这一行有<b>中文符号「' + esc(ch) + '」</b>！写代码要用英文符号 <code>( ) : , "</code>。<br>把输入法切换成英文，再把这个符号重新打一次。';
    }
    if (type === 'IndentationError') {
      return '这一行前面的<b>空格（缩进）</b>不对。普通的代码要顶格写，前面不要有空格；<code>for</code> 下面的代码前面要有一样多的空格。';
    }
    if (type === 'SyntaxError' || type === 'ParseError' || type === 'TokenError') {
      return '电脑<b>看不懂这一行的写法</b>。检查：括号 <code>( )</code> 是不是成对？引号 <code>" "</code> 是不是成对？<br>小秘密：错误有时候其实在<b>上一行</b>（比如上一行少了一个括号）。';
    }
    if (type === 'AttributeError' && (m = /has no attribute '(.+?)'/.exec(msg))) {
      return '海龟不认识「<b>' + esc(m[1]) + '</b>」这个指令。是不是拼错了？对照一下指令卡片。';
    }
    if (type === 'TypeError' && /missing|takes|argument/.test(msg)) {
      return '括号里放的东西<b>太多或太少</b>了。比如 <code>forward()</code> 括号里要放一个数字：<code>forward(100)</code>。';
    }
    if (type === 'TypeError') {
      return '<b>东西的种类</b>搞混了。比如 <code>forward()</code> 里要放数字，<code>color()</code> 里要放带引号的颜色名 <code>"red"</code>。';
    }
    if (type === 'ImportError' || type === 'ModuleNotFoundError') {
      return '网页画板只认识 <code>turtle</code>、<code>random</code>、<code>math</code>、<code>time</code> 这几个工具箱。电脑上装的 Python 认识的更多。';
    }
    if (/color/i.test(msg)) {
      return '海龟<b>不认识这个颜色</b>。颜色名要用英文、加引号，比如 <code>"red"</code>、<code>"gold"</code>。';
    }
    if (type === 'ZeroDivisionError') return '不能<b>除以 0</b>，数学老师也不允许 😄';
    if (type === 'TimeLimitError') return '程序运行<b>太久</b>了，是不是有个停不下来的循环？';
    if (type === 'ValueError') return '这个<b>值</b>不对，比如本来要数字，却给了文字。';
    return '出错啦！别担心——<b>报错是电脑在给你线索</b>。看看是第几行，再读一读英文提示。';
  }

  function Playground(root) {
    this.root = root;
    this.src = root.getAttribute('data-src');
    this.title = root.getAttribute('data-title') || '🐢 代码画板';
    this.hasCanvas = root.getAttribute('data-canvas') !== 'no';
    this.saveName = root.getAttribute('data-save') || 'my-drawing';
    this.draftKey = root.getAttribute('data-draft') ? 'kc-draft-' + root.getAttribute('data-draft') : null;
    var inline = root.querySelector('textarea');
    this.initial = inline ? inline.value.replace(/^\n/, '') : '';
    this.runId = 0;
    this.build();
    this.load();
  }

  Playground.prototype.build = function () {
    var self = this;
    var r = this.root;
    r.innerHTML = '';
    r.classList.add('pg');

    var head = el('div', 'pg-head');
    head.appendChild(el('span', 'pg-title', esc(this.title)));
    this.btnRun = el('button', 'pg-btn run', '▶ 运行');
    this.btnReset = el('button', 'pg-btn', '↺ 还原');
    this.btnCopy = el('button', 'pg-btn', '📋 复制');
    this.btnDown = el('button', 'pg-btn', '⬇ 下载');
    this.btnSave = el('button', 'pg-btn', '📤 存到作品墙');
    this.btnRun.title = '快捷键：Ctrl + Enter';
    this.btnReset.title = '回到最开始的代码';
    this.btnCopy.title = '复制代码（可以粘贴给 AI 问问题）';
    this.btnDown.title = '下载成 .py 文件，在电脑上的 Python 里运行';
    this.btnSave.title = '打开 GitHub，把这段代码存进 my-work 文件夹';
    [this.btnRun, this.btnReset, this.btnCopy, this.btnDown, this.btnSave].forEach(function (b) { head.appendChild(b); });
    r.appendChild(head);

    var main = el('div', 'pg-main' + (this.hasCanvas ? '' : ' no-canvas'));
    var ed = el('div', 'pg-editor');
    var ta = el('textarea');
    ta.spellcheck = false;
    ta.value = this.initial;
    ed.appendChild(ta);
    main.appendChild(ed);

    var stage = el('div', 'pg-stage');
    if (this.hasCanvas) {
      this.canvasEl = el('div', 'pg-canvas');
      this.canvasEl.appendChild(el('div', 'pg-empty', '<span>点 <b>▶ 运行</b>，海龟会在这里画画 🐢</span>'));
      stage.appendChild(this.canvasEl);
    }
    this.out = el('pre', 'pg-out');
    stage.appendChild(this.out);
    main.appendChild(stage);
    r.appendChild(main);

    this.errBox = el('div', 'pg-err');
    this.okBox = el('div', 'pg-ok');
    r.appendChild(this.errBox);
    r.appendChild(this.okBox);

    if (window.CodeMirror) {
      this.cm = CodeMirror.fromTextArea(ta, {
        mode: 'python', lineNumbers: true, indentUnit: 4, tabSize: 4,
        viewportMargin: Infinity, lineWrapping: false,
        extraKeys: {
          'Ctrl-Enter': function () { self.run(); },
          'Cmd-Enter': function () { self.run(); },
          Tab: function (cm) { cm.replaceSelection('    '); }
        }
      });
      this.cm.on('change', function () { self.clearMark(); self.saveDraft(); });
    } else {
      this.ta = ta;
      ta.addEventListener('input', function () { self.saveDraft(); });
    }

    this.btnRun.onclick = function () { self.running ? self.stop() : self.run(); };
    this.btnReset.onclick = function () {
      if (self.getCode() === self.initial || confirm('要回到最开始的代码吗？你改的地方会消失哦。')) self.setCode(self.initial);
    };
    this.btnCopy.onclick = function () { self.copy(self.getCode(), self.btnCopy); };
    this.btnDown.onclick = function () { self.download(); };
    this.btnSave.onclick = function () { self.saveToGitHub(); };
  };

  Playground.prototype.load = function () {
    var self = this;
    var draft = null;
    if (this.draftKey) { try { draft = localStorage.getItem(this.draftKey); } catch (e) {} }
    if (!this.src) { if (draft) this.setCode(draft); return; }
    fetch(this.src, { cache: 'no-cache' }).then(function (res) {
      if (!res.ok) throw new Error(res.status);
      return res.text();
    }).then(function (text) {
      self.initial = text;
      self.setCode(draft || text);
    }).catch(function () {
      self.setCode('# 😢 没找到代码文件：' + self.src + '\n');
    });
  };

  Playground.prototype.getCode = function () { return this.cm ? this.cm.getValue() : this.ta.value; };
  Playground.prototype.setCode = function (c) { if (this.cm) this.cm.setValue(c); else this.ta.value = c; };
  Playground.prototype.saveDraft = function () {
    if (!this.draftKey) return;
    try { localStorage.setItem(this.draftKey, this.getCode()); } catch (e) {}
  };

  Playground.prototype.clearMark = function () {
    if (this.cm && this.markLine != null) { this.cm.removeLineClass(this.markLine, 'background', 'err-line'); this.markLine = null; }
  };

  Playground.prototype.setRunning = function (on) {
    this.running = on;
    this.btnRun.textContent = on ? '■ 停下' : '▶ 运行';
    this.btnRun.className = 'pg-btn ' + (on ? 'stop' : 'run');
  };

  Playground.prototype.stop = function () {
    this.runId++;
    if (window.Sk && Sk.TurtleGraphics && Sk.TurtleGraphics.stop) { try { Sk.TurtleGraphics.stop(); } catch (e) {} }
    this.setRunning(false);
    this.out.textContent += '\n⏹ 停下了。\n';
  };

  Playground.prototype.run = function () {
    var self = this;
    if (!window.Sk) { alert('Python 还在加载，等几秒再试试～'); return; }
    if (active && active !== self && active.running) active.stop();
    active = self;
    var myRun = ++this.runId;
    var code = this.getCode();

    this.clearMark();
    this.out.textContent = '';
    this.errBox.className = 'pg-err';
    this.okBox.className = 'pg-ok';
    this.setRunning(true);

    if (Sk.TurtleGraphics && Sk.TurtleGraphics.stop) { try { Sk.TurtleGraphics.stop(); } catch (e) {} }
    Sk.TurtleGraphics = Sk.TurtleGraphics || {};
    if (this.hasCanvas) {
      this.canvasEl.innerHTML = '';
      Sk.TurtleGraphics.target = this.canvasEl;
    } else {
      if (!this.hiddenTarget) { this.hiddenTarget = el('div'); this.hiddenTarget.style.display = 'none'; this.root.appendChild(this.hiddenTarget); }
      Sk.TurtleGraphics.target = this.hiddenTarget;
    }
    Sk.TurtleGraphics.width = SIZE;
    Sk.TurtleGraphics.height = SIZE;

    Sk.configure({
      output: function (t) { if (myRun === self.runId) { self.out.textContent += t; self.out.scrollTop = 1e9; } },
      read: builtinRead,
      __future__: Sk.python3,
      inputfunTakesPrompt: true,
      inputfun: function (prompt) {
        return new Promise(function (resolve) {
          setTimeout(function () {
            var v = window.prompt(prompt || '请输入：', '');
            v = v === null ? '' : v;
            self.out.textContent += (prompt || '') + v + '\n';
            resolve(v);
          }, 30);
        });
      },
      killableWhile: true,
      killableFor: true,
      execLimit: 60000
    });

    Sk.misceval.asyncToPromise(function () {
      return Sk.importMainWithBody('<stdin>', false, code, true);
    }, {
      '*': function () { if (myRun !== self.runId) throw new Error('__kc_stopped__'); }
    }).then(function () {
      if (myRun !== self.runId) return;
      self.setRunning(false);
      self.okBox.innerHTML = '✅ 运行成功！' + PRAISE[Math.floor(Math.random() * PRAISE.length)];
      self.okBox.className = 'pg-ok show';
      document.dispatchEvent(new CustomEvent('kc-run-ok', { detail: { title: self.title } }));
    }, function (err) {
      if (myRun !== self.runId) return;
      if (err && err.message === '__kc_stopped__') return;
      self.setRunning(false);
      self.showError(err, code);
    });
  };

  Playground.prototype.showError = function (err, code) {
    var self = this;
    var type = (err && err.tp$name) || 'Error';
    var raw = err && err.toString ? err.toString() : String(err);
    var msg = raw;
    try { if (err.args && err.args.v && err.args.v[0]) msg = String(err.args.v[0].v); } catch (e) {}
    var line = null;
    try { if (err.traceback && err.traceback.length) line = err.traceback[0].lineno; } catch (e) {}
    if (!line) { var lm = /line (\d+)/.exec(raw); if (lm) line = +lm[1]; }
    var lines = code.split('\n');
    var lineText = line ? (lines[line - 1] || '') : '';

    if (this.cm && line && line <= this.cm.lineCount()) {
      this.markLine = line - 1;
      this.cm.addLineClass(this.markLine, 'background', 'err-line');
      this.cm.scrollIntoView({ line: this.markLine, ch: 0 }, 80);
    }

    var html = '<b>🐞 第 ' + (line || '?') + ' 行出了个小问题</b><br>' + explain(type, msg, lineText) +
      '<span class="raw">电脑的原话：' + esc(raw) + '</span>' +
      '<div style="margin-top:10px;font-size:.9rem">🛟 卡住了？① 看第 ' + (line || '?') + ' 行 → ② 翻笔记本 → ③ <button class="pg-btn kc-ask">📋 复制「问 AI 要提示」的话</button> → ④ 问老师</div>';
    this.errBox.innerHTML = html;
    this.errBox.className = 'pg-err show';
    this.errBox.querySelector('.kc-ask').onclick = function () {
      var ask = '我在学 Python turtle，我是小学生。\n我想让程序：___（写下你想让它做什么）\n但是运行时报错了：\n' + raw +
        '\n\n我的代码是：\n```python\n' + code + '\n```\n请给我一个提示，告诉我去看哪里，不要直接给我改好的答案。';
      self.copy(ask, this);
    };
  };

  Playground.prototype.copy = function (text, btn) {
    var done = function () { var t = btn.textContent; btn.textContent = '✅ 复制好了'; setTimeout(function () { btn.textContent = t; }, 1500); };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(done, function () { window.prompt('复制下面的文字：', text); });
    } else {
      window.prompt('复制下面的文字：', text);
    }
  };

  Playground.prototype.download = function () {
    var name = (this.saveName || 'my-code') + '.py';
    var blob = new Blob([this.getCode()], { type: 'text/x-python' });
    var a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = name;
    document.body.appendChild(a);
    a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 500);
  };

  Playground.prototype.saveToGitHub = function () {
    var cfg = window.KC || {};
    var name = window.prompt('给作品起个英文文件名（字母、数字、- 都可以）：\n比如 rainbow-star、week01-homework', this.saveName);
    if (!name) return;
    name = name.trim().toLowerCase().replace(/\.py$/, '').replace(/[^a-z0-9_-]+/g, '-').replace(/^-+|-+$/g, '') || 'my-drawing';
    var url = 'https://github.com/' + cfg.repo + '/new/' + cfg.branch + '/my-work' +
      '?filename=' + encodeURIComponent(name + '.py') +
      '&value=' + encodeURIComponent(this.getCode());
    alert('马上打开 GitHub 👉\n\n1. 检查文件名是 ' + name + '.py\n2. 点右上角绿色的「Commit changes...」\n3. 再点一次「Commit changes」\n\n1~2 分钟后，作品墙上就会出现你的作品！\n（如果说名字已经存在，就换一个名字）');
    window.open(url, '_blank', 'noopener');
  };

  function init() {
    var list = document.querySelectorAll('.playground');
    for (var i = 0; i < list.length; i++) new Playground(list[i]);
  }
  window.KCPlayground = Playground;
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
