/* 🐢 代码画板：在网页里运行 Python（turtle 海龟画画）
 * 用法（写在 .md 里）：
 *   <div class="playground" data-src="code/square.py" data-title="正方形" data-title-en="Square" data-save="my-square"></div>
 *   data-src       起始代码文件
 *   data-title-en  英文标题（不写就用中文标题）
 *   data-canvas    "no" = 不需要海龟画布（只用 print）
 *   data-save      「存到作品墙」时默认的文件名
 *   data-draft     填一个名字 = 自动在这台电脑上记住没写完的代码
 *   data-images    显示「🖼️ 图片」按钮：上传图片，用 screen.addshape("dog.gif") 让海龟变成它
 */
(function () {
  'use strict';

  var active = null;
  var SIZE = 600;
  var PRAISE = [
    ['太棒了！', 'Awesome!'], ['电脑听你的话了！', 'The computer listened to you!'], ['漂亮！', 'Beautiful!'],
    ['你真是个程序员！', 'You are a real programmer!'], ['一次就跑通！', 'Worked first time!'], ['海龟为你点赞 🐢👍', 'The turtle says nice work 🐢👍']
  ];

  // 海龟的图片形状（screen.addshape("dog.gif")）
  // IMAGES：孩子在画板上传的图（存在这台电脑上）；REPO_IMAGES：从 GitHub 的 my-work/ 读来的图（只在本次打开页面时有效）
  var SHAPE_MAX = 80;
  var IMAGES = {};
  var REPO_IMAGES = {};
  try { IMAGES = JSON.parse(localStorage.getItem('kc-images') || '{}'); } catch (e) {}
  function saveImages() {
    try { localStorage.setItem('kc-images', JSON.stringify(IMAGES)); return true; } catch (e) { return false; }
  }
  // 图片太大就缩到 max 像素以内（不缩的话海龟会变成一张巨大的图）
  function shrink(src, max) {
    return new Promise(function (resolve, reject) {
      var img = new Image();
      img.onload = function () {
        var w = img.naturalWidth, h = img.naturalHeight;
        if (w <= max && h <= max) { resolve(src); return; }
        var k = max / Math.max(w, h);
        var c = document.createElement('canvas');
        c.width = Math.max(1, Math.round(w * k));
        c.height = Math.max(1, Math.round(h * k));
        c.getContext('2d').drawImage(img, 0, 0, c.width, c.height);
        resolve(c.toDataURL('image/png'));
      };
      img.onerror = reject;
      img.src = src;
    });
  }
  function shapeNames(code) {
    var names = [], re = /(?:addshape|register_shape)\(\s*["']([^"']+)["']/g, m;
    while ((m = re.exec(code))) names.push(m[1]);
    return names;
  }
  // Skulpt 1.2.0 的 bug：addshape / register_shape 漏写了参数名，一调用就报「takes 1 positional argument」
  // 在 turtle 模块被载入前，给它的源码补上（和 setup 等指令的写法一样）
  function patchSkulpt() {
    var files = Sk.builtinFiles && Sk.builtinFiles.files;
    var src = files && files['src/lib/turtle.js'];
    if (src && src.indexOf('$register_shape.co_varnames') < 0) {
      files['src/lib/turtle.js'] = src.replace('e.$register_shape.minArgs=1,', 'e.$register_shape.minArgs=1,e.$register_shape.co_varnames=["name","shape"],');
    }
  }
  function imageUrl(name) { return ((window.KC && KC.base) || '') + '/my-work/' + encodeURIComponent(name); }

  // 当前语言选一句
  function T(zh, en) { return window.KC && KC.lang() === 'en' ? en : zh; }
  // 两种语言都放进页面，切换按钮一点就变
  function both(zh, en) { return '<span class="zh">' + zh + '</span><span class="en">' + en + '</span>'; }

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

  // 把 Python 的报错翻译成小朋友看得懂的话：返回 [中文, English]
  function explain(type, msg, lineText) {
    var m;
    var isSyntax = type === 'SyntaxError' || type === 'ParseError' || type === 'TokenError';
    // 引号里的字不算（比如 print("你好！") 里的「！」没问题）
    var codePart = (lineText || '').replace(/"[^"]*"|'[^']*'/g, '');
    if (type === 'NameError' && (m = /name '(_+)' is not defined/.exec(msg))) {
      return ['这里有个 <b>' + esc(m[1]) + '</b> 空格还没填哦！把它换成你想好的数字（或颜色）。',
        'There is a blank <b>' + esc(m[1]) + '</b> to fill in! Replace it with a number (or a colour).'];
    }
    if (type === 'NameError' && (m = /name '(.+?)' is not defined/.exec(msg))) {
      return ['电脑不认识「<b>' + esc(m[1]) + '</b>」这个名字。检查一下：<br>① 拼写对吗？② 大小写对吗？（<code>Turtle</code> 和 <code>turtle</code> 不一样）<br>③ 如果是文字，记得用引号包起来，比如 <code>"red"</code>。',
        'The computer doesn\'t know the name "<b>' + esc(m[1]) + '</b>". Check:<br>① Is it spelled right? ② Are the capital letters right? (<code>Turtle</code> and <code>turtle</code> are different)<br>③ If it\'s a word like a colour, put it in quotes, like <code>"red"</code>.'];
    }
    if ((m = /Missing asset: .*\/([^\/\s]+)/.exec(msg))) {
      var img = esc(decodeURIComponent(m[1]));
      return ['找不到图片「<b>' + img + '</b>」。先点画板上的 <b>🖼️ 图片</b> 上传它；文件名要和代码里写的<b>一模一样</b>。',
        'Can\'t find the picture "<b>' + img + '</b>". Click <b>🖼️ Picture</b> on the playground to upload it first. The file name must match your code <b>exactly</b>.'];
    }
    if (isSyntax && /[（）：，“”‘’；。！]/.test(codePart)) {
      var ch = codePart.match(/[（）：，“”‘’；。！]/)[0];
      return ['这一行有<b>中文符号「' + esc(ch) + '」</b>！写代码要用英文符号 <code>( ) : , "</code>。<br>把输入法切换成英文，再把这个符号重新打一次。',
        'This line has a <b>Chinese symbol "' + esc(ch) + '"</b>! Code needs English symbols <code>( ) : , "</code>.<br>Switch your keyboard to English and type it again.'];
    }
    if (type === 'IndentationError') {
      return ['这一行前面的<b>空格（缩进）</b>不对。普通的代码要顶格写，前面不要有空格；<code>for</code> 下面的代码前面要有一样多的空格。',
        'The <b>spaces at the start</b> of this line (indentation) are wrong. Normal lines start right at the edge; lines inside a <code>for</code> need the same number of spaces.'];
    }
    if (isSyntax) {
      return ['电脑<b>看不懂这一行的写法</b>。检查：括号 <code>( )</code> 是不是成对？引号 <code>" "</code> 是不是成对？<br>小秘密：错误有时候其实在<b>上一行</b>（比如上一行少了一个括号）。',
        'The computer <b>can\'t read how this line is written</b>. Check: do the brackets <code>( )</code> come in pairs? Do the quotes <code>" "</code> come in pairs?<br>Secret tip: sometimes the mistake is really on the <b>line above</b>.'];
    }
    if (type === 'AttributeError' && (m = /has no attribute '(.+?)'/.exec(msg))) {
      return ['海龟不认识「<b>' + esc(m[1]) + '</b>」这个指令。是不是拼错了？对照一下指令卡片。',
        'The turtle doesn\'t know the command "<b>' + esc(m[1]) + '</b>". Is it spelled wrong? Check the command cards.'];
    }
    if (type === 'TypeError' && /missing|takes|argument/.test(msg)) {
      return ['括号里放的东西<b>太多或太少</b>了。比如 <code>forward()</code> 括号里要放一个数字：<code>forward(100)</code>。',
        'There are <b>too many or too few</b> things inside the brackets. For example, <code>forward()</code> needs one number: <code>forward(100)</code>.'];
    }
    if (type === 'TypeError') {
      return ['<b>东西的种类</b>搞混了。比如 <code>forward()</code> 里要放数字，<code>color()</code> 里要放带引号的颜色名 <code>"red"</code>。',
        'Something is the <b>wrong kind</b>. For example, <code>forward()</code> needs a number and <code>color()</code> needs a colour name in quotes, like <code>"red"</code>.'];
    }
    if (type === 'ImportError' || type === 'ModuleNotFoundError') {
      return ['网页画板只认识 <code>turtle</code>、<code>random</code>、<code>math</code>、<code>time</code> 这几个工具箱。电脑上装的 Python 认识的更多。',
        'This web playground only knows the <code>turtle</code>, <code>random</code>, <code>math</code> and <code>time</code> toolboxes. Python on a computer knows many more.'];
    }
    if (/color/i.test(msg)) {
      return ['海龟<b>不认识这个颜色</b>。颜色名要用英文、加引号，比如 <code>"red"</code>、<code>"gold"</code>。',
        'The turtle <b>doesn\'t know this colour</b>. Use an English colour name in quotes, like <code>"red"</code> or <code>"gold"</code>.'];
    }
    if (type === 'ZeroDivisionError') return ['不能<b>除以 0</b>，数学老师也不允许 😄', 'You can\'t <b>divide by 0</b> — your maths teacher wouldn\'t allow it either 😄'];
    if (type === 'ValueError') return ['这个<b>值</b>不对，比如本来要数字，却给了文字。', 'This <b>value</b> is wrong — for example, it wanted a number but got words.'];
    return ['出错啦！别担心——<b>报错是电脑在给你线索</b>。看看是第几行，再读一读英文提示。',
      'Oops! Don\'t worry — <b>an error is the computer giving you a clue</b>. Look at the line number and read the message.'];
  }

  function Playground(root) {
    this.root = root;
    this.src = root.getAttribute('data-src');
    this.title = root.getAttribute('data-title') || '🐢 代码画板';
    this.titleEn = root.getAttribute('data-title-en') || (root.getAttribute('data-title') ? this.title : '🐢 Code Playground');
    this.hasCanvas = root.getAttribute('data-canvas') !== 'no';
    this.saveName = root.getAttribute('data-save') || 'my-drawing';
    this.draftKey = root.getAttribute('data-draft') ? 'kc-draft-' + root.getAttribute('data-draft') : null;
    this.allowImages = root.hasAttribute('data-images') && this.hasCanvas;
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
    head.appendChild(el('span', 'pg-title', both(esc(this.title), esc(this.titleEn))));
    this.btnRun = el('button', 'pg-btn run');
    this.btnReset = el('button', 'pg-btn', both('↺ 还原', '↺ Reset'));
    this.btnCopy = el('button', 'pg-btn', both('📋 复制', '📋 Copy'));
    this.btnDown = el('button', 'pg-btn', both('⬇ 下载', '⬇ Download'));
    this.btnSave = el('button', 'pg-btn', both('📤 存到作品墙', '📤 Save to Gallery'));
    this.btnRun.title = 'Ctrl + Enter';
    [this.btnRun, this.btnReset, this.btnCopy, this.btnDown, this.btnSave].forEach(function (b) { head.appendChild(b); });
    r.appendChild(head);
    this.setRunning(false);
    if (this.allowImages) this.buildImages(head);

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
      this.canvasEl.appendChild(el('div', 'pg-empty', both('点 <b>▶ 运行</b>，海龟会在这里画画 🐢', 'Click <b>▶ Run</b> and the turtle will draw here 🐢')));
      stage.appendChild(this.canvasEl);
    }
    this.out = el('pre', 'pg-out');
    stage.appendChild(this.out);
    main.appendChild(stage);
    r.appendChild(main);

    this.errBox = el('div', 'pg-err');
    this.okBox = el('div', 'pg-ok');
    this.saveBox = el('div', 'pg-save');
    r.appendChild(this.errBox);
    r.appendChild(this.okBox);
    r.appendChild(this.saveBox);

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
      if (self.getCode() === self.initial || confirm(T('要回到最开始的代码吗？你改的地方会消失哦。', 'Go back to the starting code? Your changes will be lost.'))) self.setCode(self.initial);
    };
    this.btnCopy.onclick = function () { self.copy(self.getCode(), self.btnCopy); };
    this.btnDown.onclick = function () { self.download(); };
    this.btnSave.onclick = function () { self.saveToGitHub(); };
  };

  // 🖼️ 上传图片，让海龟变成这张图
  Playground.prototype.buildImages = function (head) {
    var self = this;
    var btn = el('button', 'pg-btn', both('🖼️ 图片', '🖼️ Picture'));
    btn.title = 'GIF / PNG / JPG';
    head.insertBefore(btn, this.btnReset);
    var input = el('input');
    input.type = 'file';
    input.accept = 'image/gif,image/png,image/jpeg,image/webp';
    input.style.display = 'none';
    this.imgPanel = el('div', 'pg-imgs');
    this.root.appendChild(input);
    this.root.appendChild(this.imgPanel);
    btn.onclick = function () { input.click(); };
    input.onchange = function () {
      var f = input.files && input.files[0];
      input.value = '';
      if (!f) return;
      if (f.size > 5 * 1024 * 1024) { alert(T('图片太大了（超过 5MB），换一张小一点的吧。', 'That picture is too big (over 5 MB). Try a smaller one.')); return; }
      var name = f.name.trim().toLowerCase().replace(/\s+/g, '-');
      var rd = new FileReader();
      rd.onload = function () {
        shrink(rd.result, SHAPE_MAX).then(function (d) {
          IMAGES[name] = d;
          self.renderImages(saveImages());
        }, function () { alert(T('这个文件打不开，换一张图片试试。', 'Couldn\'t open that file — try another picture.')); });
      };
      rd.readAsDataURL(f);
    };
    this.renderImages(true);
  };

  Playground.prototype.renderImages = function (saved) {
    var self = this;
    var names = Object.keys(IMAGES);
    if (!names.length) {
      this.imgPanel.innerHTML = '<span class="muted">' + both('点 <b>🖼️ 图片</b> 上传一张图（GIF / PNG / JPG），就能让海龟变成它！', 'Click <b>🖼️ Picture</b> to upload an image (GIF / PNG / JPG) and turn the turtle into it!') + '</span>';
      return;
    }
    var html = names.map(function (n) {
      return '<span class="pg-img"><img src="' + IMAGES[n] + '" alt=""><code>' + esc(n) + '</code>' +
        '<button class="pg-btn kc-use" data-n="' + esc(n) + '">' + both('📋 复制用法', '📋 Copy code') + '</button>' +
        '<button class="pg-btn kc-del" data-n="' + esc(n) + '" title="Delete">✕</button></span>';
    }).join('');
    if (!saved) html += '<div class="muted">' + both('⚠️ 这台电脑存不下了，关掉网页后图片会消失。', '⚠️ No space left on this computer — the picture disappears when you close the page.') + '</div>';
    html += '<div class="muted" style="font-size:.85rem">' + both('💡 想让作品墙也显示这张图？把原图上传到 GitHub 的 my-work 文件夹（Add file → Upload files），文件名要一样。',
      '💡 Want it in the Gallery too? Upload the picture to the my-work folder on GitHub (Add file → Upload files) with the same name.') + '</div>';
    this.imgPanel.innerHTML = html;
    this.imgPanel.querySelectorAll('.kc-use').forEach(function (b) {
      b.onclick = function () {
        var n = b.getAttribute('data-n');
        self.copy('screen = turtle.Screen()\nscreen.addshape("' + n + '")\nt.shape("' + n + '")\n', b);
      };
    });
    this.imgPanel.querySelectorAll('.kc-del').forEach(function (b) {
      b.onclick = function () {
        delete IMAGES[b.getAttribute('data-n')];
        self.renderImages(saveImages());
      };
    });
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
      self.setCode('# 😢 ' + T('没找到代码文件：', 'Code file not found: ') + self.src + '\n');
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
    this.btnRun.innerHTML = on ? both('■ 停下', '■ Stop') : both('▶ 运行', '▶ Run');
    this.btnRun.className = 'pg-btn ' + (on ? 'stop' : 'run');
  };

  Playground.prototype.stop = function () {
    this.runId++;
    if (window.Sk && Sk.TurtleGraphics && Sk.TurtleGraphics.stop) { try { Sk.TurtleGraphics.stop(); } catch (e) {} }
    this.setRunning(false);
    this.out.textContent += T('\n⏹ 停下了。\n', '\n⏹ Stopped.\n');
  };

  Playground.prototype.run = function () {
    var self = this;
    if (!window.Sk) { alert(T('Python 还在加载，等几秒再试试～', 'Python is still loading — try again in a few seconds.')); return; }
    if (active && active !== self && active.running) active.stop();
    active = self;
    var myRun = ++this.runId;
    var code = this.getCode();
    // Skulpt 的 turtle 模块没有 bgcolor、setup 这类「屏幕」指令，换成 Screen() 上的同名指令（行数不变，报错行号照样准）
    var runCode = code.replace(/\bturtle\.(bgcolor|setup|exitonclick|listen|onkey|onkeypress|ontimer|onscreenclick)\(/g, 'turtle.Screen().$1(');

    this.clearMark();
    this.out.textContent = '';
    this.errBox.className = 'pg-err';
    this.okBox.className = 'pg-ok';
    this.saveBox.className = 'pg-save';
    this.setRunning(true);

    // 代码里用到、但没在画板上传过的图片，先从 GitHub 的 my-work/ 读进来并缩小
    var missing = shapeNames(code).filter(function (n) { return !IMAGES[n] && !REPO_IMAGES[n]; });
    if (missing.length) {
      Promise.all(missing.map(function (n) {
        return shrink(imageUrl(n), SHAPE_MAX).then(function (d) { REPO_IMAGES[n] = d; }, function () {});
      })).then(function () {
        if (myRun !== self.runId) return;
        // 哪儿都找不到的图片：Skulpt 不会报错，海龟会悄悄消失，所以这里先告诉孩子
        var lost = missing.filter(function (n) { return !REPO_IMAGES[n]; })[0];
        if (lost) {
          var lineNo = code.split('\n').findIndex(function (l) { return l.indexOf(lost) >= 0 && /addshape|register_shape/.test(l); }) + 1;
          self.setRunning(false);
          self.showError({ tp$name: 'Error', toString: function () { return 'Missing asset: ' + imageUrl(lost) + ' on line ' + lineNo; } }, code);
          return;
        }
        self.start(myRun, code, runCode);
      });
      return;
    }
    this.start(myRun, code, runCode);
  };

  Playground.prototype.start = function (myRun, code, runCode) {
    var self = this;
    patchSkulpt();
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
    // addshape("dog.gif") 按名字找图：先找上传的，再找 GitHub my-work/ 里的
    Sk.TurtleGraphics.assets = function (name) { return IMAGES[name] || REPO_IMAGES[name] || imageUrl(name); };

    Sk.configure({
      output: function (t) { if (myRun === self.runId) { self.out.textContent += t; self.out.scrollTop = 1e9; } },
      read: builtinRead,
      __future__: Sk.python3,
      inputfunTakesPrompt: true,
      inputfun: function (prompt) {
        return new Promise(function (resolve) {
          setTimeout(function () {
            var v = window.prompt(prompt || T('请输入：', 'Type your answer:'), '');
            v = v === null ? '' : v;
            self.out.textContent += (prompt || '') + v + '\n';
            resolve(v);
          }, 30);
        });
      },
      // 不限时间（慢慢画的大图也不会被打断）；每 100 毫秒让一下浏览器，死循环时「停下」按钮也能点
      execLimit: null,
      yieldLimit: 100,
      killableWhile: true,
      killableFor: true
    });

    Sk.misceval.asyncToPromise(function () {
      return Sk.importMainWithBody('<stdin>', false, runCode, true);
    }, {
      '*': function () { if (myRun !== self.runId) throw new Error('__kc_stopped__'); }
    }).then(function () {
      if (myRun !== self.runId) return;
      self.setRunning(false);
      var p = PRAISE[Math.floor(Math.random() * PRAISE.length)];
      self.okBox.innerHTML = both('✅ 运行成功！' + p[0], '✅ It worked! ' + p[1]);
      self.okBox.className = 'pg-ok show';
      document.dispatchEvent(new CustomEvent('kc-run-ok'));
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

    var L = line || '?';
    var ex = explain(type, msg, lineText);
    this.errBox.innerHTML =
      '<b>' + both('🐞 第 ' + L + ' 行出了个小问题', '🐞 Small problem on line ' + L) + '</b><br>' + both(ex[0], ex[1]) +
      '<span class="raw">' + both('电脑的原话：', 'What the computer said: ') + esc(raw) + '</span>' +
      '<div style="margin-top:10px;font-size:.9rem">' +
      both('🛟 卡住了？① 看第 ' + L + ' 行 → ② 翻笔记本 → ③ ', '🛟 Stuck? ① Look at line ' + L + ' → ② Check your notebook → ③ ') +
      '<button class="pg-btn kc-ask">' + both('📋 复制「问 AI 要提示」的话', '📋 Copy a "hint please" message for AI') + '</button>' +
      both(' → ④ 问老师', ' → ④ Ask your teacher') + '</div>';
    this.errBox.className = 'pg-err show';
    this.errBox.querySelector('.kc-ask').onclick = function () {
      var ask = T(
        '我在学 Python turtle，我是小学生。\n我想让程序：___（写下你想让它做什么）\n但是运行时报错了：\n' + raw + '\n\n我的代码是：\n```python\n' + code + '\n```\n请给我一个提示，告诉我去看哪里，不要直接给我改好的答案。',
        'I\'m a primary school student learning Python turtle.\nI want my program to: ___ (write what you want it to do)\nBut I got this error:\n' + raw + '\n\nMy code:\n```python\n' + code + '\n```\nPlease give me a hint about where to look. Don\'t give me the fixed code.'
      );
      self.copy(ask, this);
    };
  };

  Playground.prototype.copy = function (text, btn) {
    var old = btn.innerHTML;
    var done = function () { btn.innerHTML = both('✅ 复制好了', '✅ Copied'); setTimeout(function () { btn.innerHTML = old; }, 1500); };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(done, function () { window.prompt(T('复制下面的文字：', 'Copy this text:'), text); });
    } else {
      window.prompt(T('复制下面的文字：', 'Copy this text:'), text);
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

  // 不自动弹新窗口（容易被浏览器拦截），而是给出一个让孩子自己点的按钮
  Playground.prototype.saveToGitHub = function () {
    var cfg = window.KC || {};
    var name = window.prompt(T('给作品起个英文文件名（字母、数字、- 都可以）：\n比如 rainbow-star、week01-homework',
      'Give your work a file name (letters, numbers and - are OK):\ne.g. rainbow-star, week01-homework'), this.saveName);
    if (!name) return;
    name = name.trim().toLowerCase().replace(/\.py$/, '').replace(/[^a-z0-9_-]+/g, '-').replace(/^-+|-+$/g, '') || 'my-drawing';
    var url = 'https://github.com/' + cfg.repo + '/new/' + cfg.branch + '/my-work' +
      '?filename=' + encodeURIComponent(name + '.py') +
      '&value=' + encodeURIComponent(this.getCode());
    this.saveBox.innerHTML =
      both('<b>📤 准备好了！</b>点下面的按钮打开 GitHub：', '<b>📤 Ready!</b> Click the button to open GitHub:') + '<br>' +
      '<a class="go" target="_blank" rel="noopener" href="' + esc(url) + '">' + both('打开 GitHub，保存 ' + esc(name) + '.py', 'Open GitHub to save ' + esc(name) + '.py') + '</a><br>' +
      both('然后：点右上角绿色的 <b>Commit changes...</b> → 再点一次 <b>Commit changes</b>。1～2 分钟后作品墙上就会出现！<br><span class="muted">（如果提示名字已存在，就换一个名字再存）</span><br>⚠️ 如果绿色按钮写的是 <b>Propose changes</b> 而不是 Commit changes，说明你的账号还没有保存权限——请找老师把你加为仓库协作者。',
        'Then click the green <b>Commit changes...</b> button → click <b>Commit changes</b> again. Your work shows up in the Gallery in 1–2 minutes!<br><span class="muted">(If it says the name already exists, pick a different name.)</span><br>⚠️ If the green button says <b>Propose changes</b> instead of Commit changes, your account can\'t save here yet — ask your teacher to add you as a collaborator.');
    this.saveBox.className = 'pg-save show';
  };

  function init() {
    var list = document.querySelectorAll('.playground');
    for (var i = 0; i < list.length; i++) new Playground(list[i]);
  }
  window.KCPlayground = Playground;
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
