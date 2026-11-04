/* 🐢 代码画板：在网页里运行 Python（turtle 海龟画画）
 *
 * 用法（写在 .md 里，页面开头要有 playground: true）：
 *   <div class="playground" data-src="code/square.py" data-title="正方形" data-title-en="Square" data-save="my-square"></div>
 *
 * 基本属性
 *   data-src        起始代码文件（也可以在 div 里放 <textarea>…</textarea> 直接写代码）
 *   data-title      标题       data-title-en  英文标题
 *   data-canvas     "no" = 不需要海龟画布（只用 print / input）
 *   data-save       「存到作品墙」时默认的文件名
 *   data-draft      填一个名字 = 自动在这台电脑上记住没写完的代码
 *   data-images     显示「🖼️ 图片」按钮：上传图片，用 screen.addshape("dog.gif") 让海龟变成它
 *   data-rows       编辑器最少显示几行（默认 10）
 *
 * 关卡 / 游戏属性（给游戏板块和练习用）
 *   data-prelude    隐藏在孩子代码「前面」运行的代码文件（比如画迷宫、定义 move() 指令）
 *   data-check      隐藏在孩子代码「后面」运行的代码文件（检查有没有过关）
 *                   也可以写在 div 里：<script type="text/x-python" data-role="prelude">…</script>
 *                   检查代码里 print("__KC_WIN__") = 过关；print("__KC_HINT__ 提示文字|hint text") = 给提示（不显示在输出里）
 *   data-expect     期望的输出（用 \n 分行）。输出一样就过关
 *   data-target     目标图案的代码文件：旁边会画出目标，运行后比较相似度，≥ data-threshold（默认 85）过关
 *   data-badge      过关时颁发的徽章 id（比如 maze-1），会存在这台电脑上
 *   data-autorun    页面打开就自动运行一次
 *   data-hide-code  只显示画布，不显示代码（用来展示目标 / 示例）
 */
(function () {
  'use strict';

  var active = null;        // 最近一次运行的画板
  var gameActive = null;    // 主程序跑完了但还有定时器 / 键盘在工作的画板
  var queue = Promise.resolve();
  var SIZE = 600;
  var PRAISE = [
    ['太棒了！', 'Awesome!'], ['电脑听你的话了！', 'The computer listened to you!'], ['漂亮！', 'Beautiful!'],
    ['你真是个程序员！', 'You are a real programmer!'], ['一次就跑通！', 'Worked first time!'], ['海龟为你点赞 🐢👍', 'The turtle says nice work 🐢👍']
  ];
  // 网页 Python 少几个指令，这里悄悄补上（放在孩子代码前面，报错行号会自动减掉这几行）
  var SHIM = [
    'import turtle as _kc_t',
    '_kc_t.Turtle.shapesize = lambda self, *a, **k: None',
    '_kc_t.Turtle.turtlesize = lambda self, *a, **k: None',
    '_kc_t.Screen.colormode = lambda self, *a, **k: None',
    '_kc_t.Screen.onkeypress = _kc_t.Screen.onkey',
    '_kc_t.Screen.onkeyrelease = lambda self, *a, **k: None',
    ''
  ].join('\n');

  // 海龟的图片形状（screen.addshape("dog.gif")）
  var SHAPE_MAX = 80;
  var IMAGES = {};
  var REPO_IMAGES = {};
  try { IMAGES = JSON.parse(localStorage.getItem('kc-images') || '{}'); } catch (e) {}
  function saveImages() {
    try { localStorage.setItem('kc-images', JSON.stringify(IMAGES)); return true; } catch (e) { return false; }
  }
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
  // Skulpt 1.2.0 的 bug：addshape / register_shape 漏写了参数名
  function patchSkulpt() {
    var files = Sk.builtinFiles && Sk.builtinFiles.files;
    var src = files && files['src/lib/turtle.js'];
    if (src && src.indexOf('$register_shape.co_varnames') < 0) {
      files['src/lib/turtle.js'] = src.replace('e.$register_shape.minArgs=1,', 'e.$register_shape.minArgs=1,e.$register_shape.co_varnames=["name","shape"],');
    }
  }
  function imageUrl(name) { return ((window.KC && KC.base) || '') + '/my-work/' + encodeURIComponent(name); }

  function T(zh, en) { return window.KC && KC.lang() === 'en' ? en : zh; }
  function both(zh, en) { return '<span class="zh">' + zh + '</span><span class="en">' + en + '</span>'; }
  function builtinRead(x) {
    if (Sk.builtinFiles === undefined || Sk.builtinFiles.files[x] === undefined) throw "File not found: '" + x + "'";
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
  function countLines(s) { return s ? s.split('\n').length : 0; }
  function fetchText(url) {
    return fetch(url, { cache: 'no-cache' }).then(function (r) { if (!r.ok) throw new Error(r.status); return r.text(); });
  }

  // 把 Python 的报错翻译成小朋友看得懂的话：返回 [中文, English]
  function explain(type, msg, lineText, prevText) {
    var m;
    var isSyntax = type === 'SyntaxError' || type === 'ParseError' || type === 'TokenError';
    var codePart = (lineText || '').replace(/"[^"]*"|'[^']*'/g, '');
    if (type === 'NameError' && (m = /name '(_+)' is not defined/.exec(msg))) {
      return ['这里有个 <b>' + esc(m[1]) + '</b> 空格还没填哦！把它换成你想好的数字（或颜色）。',
        'There is a blank <b>' + esc(m[1]) + '</b> to fill in! Replace it with a number (or a colour).'];
    }
    if (type === 'NameError' && (m = /name '(.+?)' is not defined/.exec(msg))) {
      return ['电脑不认识「<b>' + esc(m[1]) + '</b>」这个名字。检查一下：<br>① 拼写对吗？② 大小写对吗？（<code>Turtle</code> 和 <code>turtle</code> 不一样）<br>③ 如果是文字，记得用引号包起来，比如 <code>"red"</code>。④ 是不是还没有「创建」它？（变量要先 <code>名字 = …</code> 才能用）',
        'The computer doesn\'t know the name "<b>' + esc(m[1]) + '</b>". Check:<br>① Is it spelled right? ② Are the capital letters right? (<code>Turtle</code> and <code>turtle</code> are different)<br>③ If it\'s a word like a colour, put it in quotes, like <code>"red"</code>. ④ Did you create it first? (a variable needs <code>name = …</code> before you use it)'];
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
    if (isSyntax && /:\s*(#.*)?$/.test(prevText || '') && /^\s*(if|elif|else|for|while|def)\b/.test(prevText || '') && !/^\s+/.test(lineText || '')) {
      return ['上一行以冒号 <code>:</code> 结尾，所以<b>这一行要往右缩进 4 个空格</b>——它是「属于」上一行的。',
        'The line above ends with a colon <code>:</code>, so <b>this line must be indented 4 spaces</b> — it belongs to the line above.'];
    }
    if (type === 'IndentationError' || (isSyntax && /indent/i.test(msg))) {
      return ['这一行前面的<b>空格（缩进）</b>不对。普通的代码要顶格写；<code>for</code>、<code>if</code>、<code>while</code>、<code>def</code> 下面「属于它」的代码要往右缩 4 个空格，而且要缩得一样多。',
        'The <b>spaces at the start</b> of this line (indentation) are wrong. Normal lines start at the edge; lines that belong to a <code>for</code>, <code>if</code>, <code>while</code> or <code>def</code> are pushed in 4 spaces, all by the same amount.'];
    }
    if (isSyntax && /:\s*$/.test(codePart) === false && /^\s*(for|if|elif|else|while|def)\b/.test(lineText || '')) {
      return ['<code>for</code>、<code>if</code>、<code>while</code>、<code>def</code> 这一行的<b>最后要有一个冒号 <code>:</code></b>。',
        'A <code>for</code>, <code>if</code>, <code>while</code> or <code>def</code> line needs a <b>colon <code>:</code> at the end</b>.'];
    }
    if (isSyntax) {
      return ['电脑<b>看不懂这一行的写法</b>。检查：括号 <code>( )</code> 是不是成对？引号 <code>" "</code> 是不是成对？等号是不是写成了 <code>=</code>（比较要用 <code>==</code>）？<br>小秘密：错误有时候其实在<b>上一行</b>（比如上一行少了一个括号）。',
        'The computer <b>can\'t read how this line is written</b>. Check: do the brackets <code>( )</code> come in pairs? Do the quotes <code>" "</code> come in pairs? Did you use <code>=</code> where you meant <code>==</code>?<br>Secret tip: sometimes the mistake is really on the <b>line above</b>.'];
    }
    if (type === 'AttributeError' && (m = /has no attribute '(.+?)'/.exec(msg))) {
      return ['海龟不认识「<b>' + esc(m[1]) + '</b>」这个指令。是不是拼错了？对照一下 <a href="' + ((window.KC && KC.base) || '') + '/cheatsheet/">📖 小词典</a>。',
        'The turtle doesn\'t know the command "<b>' + esc(m[1]) + '</b>". Is it spelled wrong? Check the <a href="' + ((window.KC && KC.base) || '') + '/cheatsheet/">📖 cheat sheet</a>.'];
    }
    if (type === 'TypeError' && /missing|takes|argument/.test(msg)) {
      return ['括号里放的东西<b>太多或太少</b>了。比如 <code>forward()</code> 括号里要放一个数字：<code>forward(100)</code>。',
        'There are <b>too many or too few</b> things inside the brackets. For example, <code>forward()</code> needs one number: <code>forward(100)</code>.'];
    }
    if (type === 'TypeError' && /str|int|concatenate|unsupported/.test(msg)) {
      return ['<b>文字和数字不能直接加在一起</b>。想把数字放进句子，用 <code>f"今年 {age} 岁"</code>；想把文字变成数字，用 <code>int(…)</code>。',
        '<b>You can\'t add words and numbers directly</b>. To put a number in a sentence use <code>f"I am {age}"</code>; to turn text into a number use <code>int(…)</code>.'];
    }
    if (type === 'TypeError') {
      return ['<b>东西的种类</b>搞混了。比如 <code>forward()</code> 里要放数字，<code>color()</code> 里要放带引号的颜色名 <code>"red"</code>。',
        'Something is the <b>wrong kind</b>. For example, <code>forward()</code> needs a number and <code>color()</code> needs a colour name in quotes, like <code>"red"</code>.'];
    }
    if (type === 'ImportError' || type === 'ModuleNotFoundError') {
      return ['网页画板只认识 <code>turtle</code>、<code>random</code>、<code>math</code>、<code>time</code> 这几个工具箱。电脑上装的 Python 认识的更多。',
        'This web playground only knows the <code>turtle</code>, <code>random</code>, <code>math</code> and <code>time</code> toolboxes. Python on a computer knows many more.'];
    }
    if (type === 'IndexError') {
      return ['列表里<b>没有这个位置</b>。记住：第一个是 <code>[0]</code>，最后一个是 <code>[len(列表) - 1]</code>。',
        'The list <b>has no item at that position</b>. Remember: the first one is <code>[0]</code> and the last is <code>[len(list) - 1]</code>.'];
    }
    if (type === 'KeyError') {
      return ['字典里<b>没有这个钥匙（键）</b>。检查拼写，或者用 <code>.get(键, "默认值")</code>。',
        'The dictionary <b>has no such key</b>. Check the spelling, or use <code>.get(key, "default")</code>.'];
    }
    if (/color/i.test(msg)) {
      return ['海龟<b>不认识这个颜色</b>。颜色名要用英文、加引号，比如 <code>"red"</code>、<code>"gold"</code>。',
        'The turtle <b>doesn\'t know this colour</b>. Use an English colour name in quotes, like <code>"red"</code> or <code>"gold"</code>.'];
    }
    if (type === 'ZeroDivisionError') return ['不能<b>除以 0</b>，数学老师也不允许 😄', 'You can\'t <b>divide by 0</b> — your maths teacher wouldn\'t allow it either 😄'];
    if (type === 'ValueError' && /int\(|invalid literal/.test(msg)) return ['<code>int()</code> 只能把<b>数字</b>文字变成数字，比如 <code>int("12")</code>。输入的不是数字就会出错。', '<code>int()</code> can only turn <b>number</b> text into a number, like <code>int("12")</code>. Typing letters makes it fail.'];
    if (type === 'ValueError') return ['这个<b>值</b>不对，比如本来要数字，却给了文字。', 'This <b>value</b> is wrong — for example, it wanted a number but got words.'];
    if (type === 'AssertionError') return ['一个<b>测试没通过</b>：<code>assert</code> 后面的条件不是 True。看看它检查的是什么。', 'A <b>test failed</b>: the condition after <code>assert</code> was not True. Look at what it checks.'];
    if (type === 'RecursionError') return ['函数<b>自己调用自己</b>太多次了，停不下来。', 'The function <b>called itself</b> too many times and couldn\'t stop.'];
    if (type === 'TimeLimitError' || /time limit/i.test(msg)) return ['程序<b>跑太久</b>了，可能是 <code>while</code> 循环永远停不下来（条件一直是 True）。', 'The program <b>ran too long</b>. Maybe a <code>while</code> loop never ends (the condition stays True).'];
    return ['出错啦！别担心——<b>报错是电脑在给你线索</b>。看看是第几行，再读一读英文提示。',
      'Oops! Don\'t worry — <b>an error is the computer giving you a clue</b>. Look at the line number and read the message.'];
  }

  // ---------- 相似度：比较两块画布上的「墨水」 ----------
  function composite(container, N) {
    var cs = Array.prototype.slice.call(container.querySelectorAll('canvas'));
    if (!cs.length) return null;
    // Skulpt 叠了两层：最上面一层是海龟的小图标，不算
    if (cs.length > 1) {
      cs.sort(function (a, b) { return (+a.style.zIndex || 0) - (+b.style.zIndex || 0); });
      cs.pop();
    }
    var c = document.createElement('canvas');
    c.width = N; c.height = N;
    var ctx = c.getContext('2d');
    cs.forEach(function (src) { try { ctx.drawImage(src, 0, 0, N, N); } catch (e) {} });
    return c;
  }
  function inkMask(container, N) {
    // 先按原始大小合成，再按格子「池化」（直接缩小画会丢掉 alpha，导致两边都空、相似度假 100%）
    var c = composite(container, SIZE);
    if (!c) return null;
    var d = c.getContext('2d').getImageData(0, 0, SIZE, SIZE).data;
    var mask = new Uint8Array(N * N), n = 0;
    for (var y = 0; y < SIZE; y++) for (var x = 0; x < SIZE; x++) {
      if (d[(y * SIZE + x) * 4 + 3] > 40) {
        var k = Math.floor(y * N / SIZE) * N + Math.floor(x * N / SIZE);
        if (!mask[k]) { mask[k] = 1; n++; }
      }
    }
    return { mask: mask, n: n, N: N };
  }
  function dilate(m) {
    var N = m.N, out = new Uint8Array(N * N);
    for (var y = 0; y < N; y++) for (var x = 0; x < N; x++) {
      if (!m.mask[y * N + x]) continue;
      for (var dy = -1; dy <= 1; dy++) for (var dx = -1; dx <= 1; dx++) {
        var yy = y + dy, xx = x + dx;
        if (yy >= 0 && yy < N && xx >= 0 && xx < N) out[yy * N + xx] = 1;
      }
    }
    return out;
  }
  function similarity(a, b) {
    if (!a || !b) return 0;
    if (!a.n && !b.n) return 100;
    var da = dilate(a), db = dilate(b), hit = 0;
    for (var i = 0; i < a.N * a.N; i++) { if (a.mask[i] && db[i]) hit++; if (b.mask[i] && da[i]) hit++; }
    return Math.round(100 * hit / (a.n + b.n));
  }

  // ---------- 画板 ----------
  function Playground(root) {
    var self = this;
    this.root = root;
    this.src = root.getAttribute('data-src');
    this.title = root.getAttribute('data-title') || '🐢 代码画板';
    this.titleEn = root.getAttribute('data-title-en') || (root.getAttribute('data-title') ? this.title : '🐢 Code Playground');
    this.hasCanvas = root.getAttribute('data-canvas') !== 'no';
    this.saveName = root.getAttribute('data-save') || 'my-drawing';
    this.draftKey = root.getAttribute('data-draft') ? 'kc-draft-' + root.getAttribute('data-draft') : null;
    this.allowImages = root.hasAttribute('data-images') && this.hasCanvas;
    this.hideCode = root.hasAttribute('data-hide-code');
    this.autorun = root.hasAttribute('data-autorun') || this.hideCode;
    this.badge = root.getAttribute('data-badge');
    this.expect = root.getAttribute('data-expect');
    if (this.expect != null) this.expect = this.expect.replace(/\\n/g, '\n');
    this.targetSrc = root.getAttribute('data-target');
    this.threshold = +(root.getAttribute('data-threshold') || 85);
    this.rows = +(root.getAttribute('data-rows') || 10);
    this.prelude = ''; this.check = ''; this.targetCode = '';
    var inlineRoles = {};
    Array.prototype.forEach.call(root.querySelectorAll('script[type="text/x-python"]'), function (s) {
      inlineRoles[s.getAttribute('data-role') || 'prelude'] = s.textContent.replace(/^\n/, '');
    });
    this.inline = inlineRoles;
    var inline = root.querySelector('textarea');
    this.initial = inline ? inline.value.replace(/^\n/, '') : '';
    this.runId = 0;
    this.won = false;
    this.build();
    this.load();
  }

  Playground.prototype.build = function () {
    var self = this;
    var r = this.root;
    r.innerHTML = '';
    r.classList.add('pg');
    if (this.hideCode) r.classList.add('pg-show');

    var head = el('div', 'pg-head');
    head.appendChild(el('span', 'pg-title', both(esc(this.title), esc(this.titleEn))));
    this.btnRun = el('button', 'pg-btn run');
    this.btnRun.title = 'Ctrl + Enter';
    head.appendChild(this.btnRun);
    if (!this.hideCode) {
      this.btnReset = el('button', 'pg-btn', both('↺ 还原', '↺ Reset'));
      this.btnCopy = el('button', 'pg-btn', both('📋 复制', '📋 Copy'));
      this.btnDown = el('button', 'pg-btn', both('⬇ 下载', '⬇ Download'));
      this.btnSave = el('button', 'pg-btn', both('📤 存到作品墙', '📤 Save to Gallery'));
      [this.btnReset, this.btnCopy, this.btnDown, this.btnSave].forEach(function (b) { head.appendChild(b); });
    }
    r.appendChild(head);
    this.setRunning(false);
    if (this.allowImages) this.buildImages(head);

    var main = el('div', 'pg-main' + (this.hasCanvas ? '' : ' no-canvas') + (this.hideCode ? ' only-canvas' : ''));
    var ed = el('div', 'pg-editor');
    var ta = el('textarea');
    ta.spellcheck = false;
    ta.value = this.initial;
    ed.appendChild(ta);
    if (!this.hideCode) main.appendChild(ed);

    var stage = el('div', 'pg-stage');
    if (this.targetSrc || this.inline.target) {
      this.targetBox = el('div', 'pg-target');
      this.targetBox.appendChild(el('div', 'pg-target-label', both('🎯 目标', '🎯 Target')));
      this.targetCanvas = el('div', 'pg-canvas small');
      this.targetBox.appendChild(this.targetCanvas);
      this.meter = el('div', 'pg-meter', both('运行后这里会显示相似度', 'Run your code to see how similar it is'));
      this.targetBox.appendChild(this.meter);
      stage.appendChild(this.targetBox);
    }
    if (this.hasCanvas) {
      this.canvasEl = el('div', 'pg-canvas');
      this.canvasEl.appendChild(el('div', 'pg-empty', both('点 <b>▶ 运行</b>，海龟会在这里画画 🐢', 'Click <b>▶ Run</b> and the turtle will draw here 🐢')));
      stage.appendChild(this.canvasEl);
    }
    this.out = el('pre', 'pg-out');
    if (this.hideCode) this.out.style.display = 'none';
    stage.appendChild(this.out);
    this.inBox = el('div', 'pg-in');
    stage.appendChild(this.inBox);
    main.appendChild(stage);
    r.appendChild(main);

    this.hintBox = el('div', 'pg-hint');
    this.errBox = el('div', 'pg-err');
    this.okBox = el('div', 'pg-ok');
    this.saveBox = el('div', 'pg-save');
    r.appendChild(this.hintBox);
    r.appendChild(this.errBox);
    r.appendChild(this.okBox);
    r.appendChild(this.saveBox);

    if (!this.hideCode && window.CodeMirror) {
      this.cm = CodeMirror.fromTextArea(ta, {
        mode: 'python', lineNumbers: true, indentUnit: 4, tabSize: 4,
        viewportMargin: Infinity, lineWrapping: false,
        extraKeys: {
          'Ctrl-Enter': function () { self.run(); },
          'Cmd-Enter': function () { self.run(); },
          Tab: function (cm) { cm.replaceSelection('    '); }
        }
      });
      this.cm.getWrapperElement().style.minHeight = (this.rows * 24 + 16) + 'px';
      this.cm.on('change', function () { self.clearMark(); self.saveDraft(); });
    } else {
      this.ta = ta;
      ta.addEventListener('input', function () { self.saveDraft(); });
    }

    this.btnRun.onclick = function () { self.running ? self.stop() : self.run(); };
    if (!this.hideCode) {
      this.btnReset.onclick = function () {
        if (self.getCode() === self.initial || confirm(T('要回到最开始的代码吗？你改的地方会消失哦。', 'Go back to the starting code? Your changes will be lost.'))) self.setCode(self.initial);
      };
      this.btnCopy.onclick = function () { self.copy(self.getCode(), self.btnCopy); };
      this.btnDown.onclick = function () { self.download(); };
      this.btnSave.onclick = function () { self.saveToGitHub(); };
    }
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
      b.onclick = function () { delete IMAGES[b.getAttribute('data-n')]; self.renderImages(saveImages()); };
    });
  };

  Playground.prototype.load = function () {
    var self = this;
    var draft = null;
    if (this.draftKey) { try { draft = localStorage.getItem(this.draftKey); } catch (e) {} }
    var jobs = [];
    var r = this.root;
    if (this.src) {
      jobs.push(fetchText(this.src).then(function (text) {
        self.initial = text;
        self.setCode(draft || text);
      }).catch(function () {
        self.setCode('# 😢 ' + T('没找到代码文件：', 'Code file not found: ') + self.src + '\n');
      }));
    } else if (draft) this.setCode(draft);
    var pre = r.getAttribute('data-prelude'), chk = r.getAttribute('data-check');
    if (this.inline.prelude) this.prelude = this.inline.prelude;
    if (this.inline.check) this.check = this.inline.check;
    if (this.inline.target) this.targetCode = this.inline.target;
    if (pre) jobs.push(fetchText(pre).then(function (t) { self.prelude = t; }));
    if (chk) jobs.push(fetchText(chk).then(function (t) { self.check = t; }));
    if (this.targetSrc) jobs.push(fetchText(this.targetSrc).then(function (t) { self.targetCode = t; }));
    this.ready = Promise.all(jobs).then(function () {
      if (self.targetCode) self.drawTarget();
      if (self.autorun) self.run();
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
  Playground.prototype.setRunning = function (on, game) {
    this.running = on;
    if (on && game) this.btnRun.innerHTML = both('■ 结束游戏', '■ End game');
    else this.btnRun.innerHTML = on ? both('■ 停下', '■ Stop') : (this.hideCode ? both('▶ 再画一次', '▶ Draw again') : both('▶ 运行', '▶ Run'));
    this.btnRun.className = 'pg-btn ' + (on ? 'stop' : 'run');
  };
  Playground.prototype.stop = function () {
    this.runId++;
    if (this.pendingInput) { this.pendingInput(''); this.pendingInput = null; }
    this.inBox.className = 'pg-in';
    if (window.Sk && Sk.TurtleGraphics) {
      try { if (gameActive === this) Sk.TurtleGraphics.reset(); else if (Sk.TurtleGraphics.stop) Sk.TurtleGraphics.stop(); } catch (e) {}
    }
    if (gameActive === this) gameActive = null;
    this.setRunning(false);
    this.out.textContent += T('\n⏹ 停下了。\n', '\n⏹ Stopped.\n');
  };

  // 把隐藏的代码和孩子的代码拼起来；offset = 孩子代码前面有几行
  Playground.prototype.assemble = function (code) {
    // 每次运行换一个随机口令，孩子自己 print("__KC_WIN__") 是不算过关的
    this.nonce = '__KC_' + Math.random().toString(36).slice(2, 10) + '_';
    var tok = this.nonce;
    var pre = this.prelude ? this.prelude.replace(/\s+$/, '').split('__KC_').join(tok) + '\n' : '';
    var chk = this.check ? '\n' + this.check.split('__KC_').join(tok) : '';
    var head = (this.hasCanvas ? SHIM : '') + pre;
    return { full: head + code + chk, offset: countLines(head) - (head ? 1 : 0), codeLines: countLines(code) };
  };

  Playground.prototype.run = function () {
    var self = this;
    if (!window.Sk) { alert(T('Python 还在加载，等几秒再试试～', 'Python is still loading — try again in a few seconds.')); return; }
    if (gameActive && gameActive !== self) gameActive.stop();
    if (active && active !== self && active.running) active.stop();
    active = self;
    var myRun = ++this.runId;
    var code = this.getCode();
    this.clearMark();
    this.out.textContent = '';
    this.hintBox.className = 'pg-hint';
    this.errBox.className = 'pg-err';
    this.okBox.className = 'pg-ok';
    this.saveBox.className = 'pg-save';
    this.inBox.className = 'pg-in';
    this.setRunning(true);

    var missing = shapeNames(code).filter(function (n) { return !IMAGES[n] && !REPO_IMAGES[n]; });
    var prep = missing.length ? Promise.all(missing.map(function (n) {
      return shrink(imageUrl(n), SHAPE_MAX).then(function (d) { REPO_IMAGES[n] = d; }, function () {});
    })) : Promise.resolve();
    queue = queue.then(function () {
      return prep.then(function () {
        if (myRun !== self.runId) return;
        var lost = missing.filter(function (n) { return !REPO_IMAGES[n]; })[0];
        if (lost) {
          var lineNo = code.split('\n').findIndex(function (l) { return l.indexOf(lost) >= 0 && /addshape|register_shape/.test(l); }) + 1;
          self.setRunning(false);
          self.showError({ tp$name: 'Error', toString: function () { return 'Missing asset: ' + imageUrl(lost) + ' on line ' + lineNo; } }, code, 0);
          return;
        }
        return self.start(myRun, code);
      });
    }).catch(function () {});
  };

  Playground.prototype.start = function (myRun, code) {
    var self = this;
    patchSkulpt();
    var asm = this.assemble(code);
    // Skulpt 的 turtle 模块没有 bgcolor、setup 这类「屏幕」指令，换成 Screen() 上的同名指令（行数不变）
    var runCode = asm.full.replace(/\bturtle\.(bgcolor|setup|exitonclick|listen|onkey|onkeypress|onkeyrelease|ontimer|onscreenclick|tracer|update|title|delay)\(/g, 'turtle.Screen().$1(');
    var isGame = /\b(ontimer|onkey|onkeypress|onclick|onscreenclick)\s*\(/.test(code);
    this.won = false;
    this.hints = [];

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
    Sk.TurtleGraphics.assets = function (name) { return IMAGES[name] || REPO_IMAGES[name] || imageUrl(name); };

    var partial = '';
    function emit(t) {
      if (myRun !== self.runId) return;
      partial += t;
      var lines = partial.split('\n');
      partial = lines.pop();
      var tok = self.nonce;
      lines.forEach(function (ln) {
        if (ln.indexOf(tok + 'WIN__') === 0) { self.won = true; return; }
        if (ln.indexOf(tok + 'HINT__') === 0) { self.hints.push(ln.slice(tok.length + 6).trim()); return; }
        self.out.textContent += ln + '\n';
      });
      if (partial && partial.indexOf('__KC_') !== 0) { self.out.textContent += partial; partial = ''; }
      self.out.scrollTop = 1e9;
    }

    Sk.configure({
      output: emit,
      read: builtinRead,
      __future__: Sk.python3,
      inputfunTakesPrompt: true,
      inputfun: function (prompt) { return self.askInput(prompt, myRun); },
      execLimit: null,
      yieldLimit: 100,
      killableWhile: true,
      killableFor: true
    });

    return Sk.misceval.asyncToPromise(function () {
      return Sk.importMainWithBody('<stdin>', false, runCode, true);
    }, {
      '*': function () { if (myRun !== self.runId) throw new Error('__kc_stopped__'); }
    }).then(function () {
      if (myRun !== self.runId) return;
      if (partial) { self.out.textContent += partial; partial = ''; }
      self.inBox.className = 'pg-in';
      self.finish(code, isGame);
    }, function (err) {
      if (myRun !== self.runId) return;
      if (err && err.message === '__kc_stopped__') return;
      self.inBox.className = 'pg-in';
      self.setRunning(false);
      self.showError(err, code, asm.offset, asm.codeLines);
    });
  };

  // 主程序跑完了：检查有没有过关、要不要继续等键盘
  Playground.prototype.finish = function (code, isGame) {
    var self = this;
    var win = this.won;
    var msg = null;
    if (this.expect != null) {
      var got = this.out.textContent.replace(/\s+$/, '').split('\n').map(function (l) { return l.replace(/\s+$/, ''); }).join('\n');
      var want = this.expect.replace(/\s+$/, '').split('\n').map(function (l) { return l.replace(/\s+$/, ''); }).join('\n');
      if (got === want) win = true;
      else {
        msg = '<div class="pg-diff"><div><b>' + both('你的输出', 'Your output') + '</b><pre>' + esc(got || '(空 / empty)') + '</pre></div><div><b>' + both('需要的输出', 'Wanted output') + '</b><pre>' + esc(want) + '</pre></div></div>' + both('还差一点点！对比一下左右两边哪里不一样（空格和标点也算哦）。', 'Almost! Compare the two sides — where are they different? (Spaces and punctuation count too.)');
      }
    }
    if (this.targetCode && this.targetMask) {
      var mine = inkMask(this.canvasEl, 96);
      var s = similarity(mine, this.targetMask);
      var good = s >= this.threshold;
      this.meter.innerHTML = '<span class="bar"><i style="width:' + s + '%" class="' + (good ? 'good' : '') + '"></i></span> ' + both('相似度 <b>' + s + '%</b>' + (good ? '' : '（要 ' + this.threshold + '% 才过关）'), 'Similarity <b>' + s + '%</b>' + (good ? '' : ' (need ' + this.threshold + '%)'));
      if (good) win = true;
      else if (!msg && !this.hints.length) msg = both('相似度 ' + s + '%，再调一调数字、颜色或位置试试！', 'Similarity ' + s + '%. Tweak the numbers, colours or position and try again!');
    }
    if (this.hints.length && !win) {
      msg = this.hints.map(function (h) { var p = h.split('|'); return both(esc(p[0]), esc(p[1] || p[0])); }).join('<br>');
    }
    if (win) {
      this.setRunning(isGame, isGame);
      if (isGame) gameActive = this;
      this.okBox.innerHTML = both('🏆 <b>过关！</b>太厉害了！', '🏆 <b>Level complete!</b> Amazing!');
      this.okBox.className = 'pg-ok show win';
      if (window.kcConfetti) kcConfetti(160);
      if (this.badge && window.KC && KC.badge) KC.badge(this.badge);
      document.dispatchEvent(new CustomEvent('kc-win', { detail: { badge: this.badge, playground: this } }));
      return;
    }
    if (msg) { this.hintBox.innerHTML = '💡 ' + msg; this.hintBox.className = 'pg-hint show'; }
    if (isGame && this.hasCanvas) {
      gameActive = this;
      this.setRunning(true, true);
      this.okBox.innerHTML = both('🎮 <b>游戏开始了！</b>先点一下画布，再按键盘 / 鼠标。玩完点「■ 结束游戏」。', '🎮 <b>Game on!</b> Click the canvas first, then use the keyboard / mouse. Click "■ End game" when done.');
      this.okBox.className = 'pg-ok show';
      try { var cv = this.canvasEl.querySelector('canvas'); if (cv) { this.canvasEl.setAttribute('tabindex', '0'); } if (Sk.TurtleGraphics.focus) Sk.TurtleGraphics.focus(true); } catch (e) {}
      document.dispatchEvent(new CustomEvent('kc-run-ok'));
      return;
    }
    this.setRunning(false);
    if (!msg) {
      var p = PRAISE[Math.floor(Math.random() * PRAISE.length)];
      this.okBox.innerHTML = both('✅ 运行成功！' + p[0], '✅ It worked! ' + p[1]);
      this.okBox.className = 'pg-ok show';
    }
    document.dispatchEvent(new CustomEvent('kc-run-ok'));
  };

  // 目标图案：悄悄画一次，记住它的「墨水」
  Playground.prototype.drawTarget = function () {
    var self = this;
    queue = queue.then(function () {
      return new Promise(function (resolve) {
        patchSkulpt();
        if (Sk.TurtleGraphics && Sk.TurtleGraphics.stop) { try { Sk.TurtleGraphics.stop(); } catch (e) {} }
        Sk.TurtleGraphics = Sk.TurtleGraphics || {};
        self.targetCanvas.innerHTML = '';
        Sk.TurtleGraphics.target = self.targetCanvas;
        Sk.TurtleGraphics.width = SIZE; Sk.TurtleGraphics.height = SIZE;
        var code = 'import turtle as _kc_t\n_kc_t.Screen().tracer(0)\n' + SHIM + self.targetCode + '\n_kc_t.Screen().update()\n';
        code = code.replace(/\bturtle\.(bgcolor|setup|tracer|update|title)\(/g, 'turtle.Screen().$1(');
        Sk.configure({ output: function () {}, read: builtinRead, __future__: Sk.python3, execLimit: 15000 });
        Sk.misceval.asyncToPromise(function () { return Sk.importMainWithBody('<stdin>', false, code, true); }).then(function () {
          self.targetMask = inkMask(self.targetCanvas, 96);
          try { var sp = self.targetCanvas.querySelectorAll('canvas'); if (sp.length > 1) sp[0].style.display = 'none'; } catch (e) {}
          resolve();
        }, function (e) { self.meter.textContent = '😢 ' + e.toString(); resolve(); });
      });
    });
    return queue;
  };

  // input()：在输出下面出现一个输入框，而不是弹窗
  Playground.prototype.askInput = function (prompt, myRun) {
    var self = this;
    return new Promise(function (resolve) {
      if (myRun !== self.runId) { resolve(''); return; }
      var box = self.inBox;
      box.innerHTML = '<label>' + esc(prompt || '') + '</label><input type="text" autocomplete="off"><button class="pg-btn run">↵ ' + both('确定', 'OK') + '</button>';
      box.className = 'pg-in show';
      var input = box.querySelector('input'), btn = box.querySelector('button');
      var done = function () {
        if (myRun !== self.runId) return;
        var v = input.value;
        self.pendingInput = null;
        box.className = 'pg-in';
        self.out.textContent += (prompt || '') + v + '\n';
        self.out.scrollTop = 1e9;
        setTimeout(function () { resolve(v); }, 10);
      };
      self.pendingInput = function () { resolve(''); };
      btn.onclick = done;
      input.onkeydown = function (e) { if (e.key === 'Enter') { e.preventDefault(); done(); } };
      setTimeout(function () { input.focus(); }, 30);
    });
  };

  Playground.prototype.showError = function (err, code, offset, codeLines) {
    var self = this;
    var type = (err && err.tp$name) || 'Error';
    var raw = err && err.toString ? err.toString() : String(err);
    var msg = raw;
    try { if (err.args && err.args.v && err.args.v[0]) msg = String(err.args.v[0].v); } catch (e) {}
    var line = null;
    try { if (err.traceback && err.traceback.length) line = err.traceback[0].lineno; } catch (e) {}
    if (!line) { var lm = /line (\d+)/.exec(raw); if (lm) line = +lm[1]; }
    offset = offset || 0;
    var hiddenErr = false;
    if (line != null) {
      line = line - offset;
      if (line < 1 || (codeLines && line > codeLines)) { hiddenErr = true; line = null; }
    }
    raw = raw.replace(/line (\d+)/g, function (_, n) { var k = +n - offset; return 'line ' + (k >= 1 ? k : '?'); });
    var lines = code.split('\n');
    var lineText = line ? (lines[line - 1] || '') : '';
    var prevText = line && line > 1 ? (lines[line - 2] || '') : '';

    if (this.cm && line && line <= this.cm.lineCount()) {
      this.markLine = line - 1;
      this.cm.addLineClass(this.markLine, 'background', 'err-line');
      this.cm.scrollIntoView({ line: this.markLine, ch: 0 }, 80);
    }

    var L = line || '?';
    var ex = explain(type, msg, lineText, prevText);
    if (hiddenErr) {
      ex = ['关卡的检查代码出了问题——可能是你的代码改掉了关卡需要的东西（比如把海龟 <code>t</code> 删了或改名了）。点「↺ 还原」再试试。',
        'The level\'s checking code hit a problem — maybe your code changed something the level needs (like deleting or renaming the turtle <code>t</code>). Click "↺ Reset" and try again.'];
    }
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
        '我在学 Python，我是小学生。\n我想让程序：___（写下你想让它做什么）\n但是运行时报错了：\n' + raw + '\n\n我的代码是：\n```python\n' + code + '\n```\n请给我一个提示，告诉我去看哪里，不要直接给我改好的答案。',
        'I\'m a primary school student learning Python.\nI want my program to: ___ (write what you want it to do)\nBut I got this error:\n' + raw + '\n\nMy code:\n```python\n' + code + '\n```\nPlease give me a hint about where to look. Don\'t give me the fixed code.'
      );
      self.copy(ask, this);
    };
    document.dispatchEvent(new CustomEvent('kc-run-error', { detail: { type: type, line: line } }));
  };

  // 画布快照（作品墙的缩略图用）
  Playground.prototype.snapshot = function (N) {
    if (!this.hasCanvas) return null;
    var c = composite(this.canvasEl, N || 240);
    if (!c) return null;
    var out = document.createElement('canvas');
    out.width = c.width; out.height = c.height;
    var ctx = out.getContext('2d');
    var bg = '#ffffff';
    try { bg = getComputedStyle(this.canvasEl.querySelector('canvas').parentElement).backgroundColor || bg; } catch (e) {}
    ctx.fillStyle = bg; ctx.fillRect(0, 0, out.width, out.height);
    ctx.drawImage(c, 0, 0);
    return out.toDataURL('image/png');
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
    var code = this.getCode();
    if (!/^#/.test(code.trim())) code = '# 🎨 ' + name + '\n' + code;
    var url = 'https://github.com/' + cfg.repo + '/new/' + cfg.branch + '/my-work' +
      '?filename=' + encodeURIComponent(name + '.py') +
      '&value=' + encodeURIComponent(code);
    this.saveBox.innerHTML =
      both('<b>📤 准备好了！</b>点下面的按钮打开 GitHub：', '<b>📤 Ready!</b> Click the button to open GitHub:') + '<br>' +
      '<a class="go" target="_blank" rel="noopener" href="' + esc(url) + '">' + both('打开 GitHub，保存 ' + esc(name) + '.py', 'Open GitHub to save ' + esc(name) + '.py') + '</a><br>' +
      both('然后：点右上角绿色的 <b>Commit changes...</b> → 再点一次 <b>Commit changes</b>。回到<a href="' + (cfg.base || '') + '/gallery/">作品墙</a>刷新一下，马上就能看到！<br><span class="muted">（如果提示名字已存在，就换一个名字再存）</span><br>⚠️ 如果绿色按钮写的是 <b>Propose changes</b> 而不是 Commit changes，说明你的账号还没有保存权限——请找老师把你加为仓库协作者。',
        'Then click the green <b>Commit changes...</b> button → click <b>Commit changes</b> again. Go back to the <a href="' + (cfg.base || '') + '/gallery/">Gallery</a> and refresh — it shows up right away!<br><span class="muted">(If it says the name already exists, pick a different name.)</span><br>⚠️ If the green button says <b>Propose changes</b> instead of Commit changes, your account can\'t save here yet — ask your teacher to add you as a collaborator.');
    this.saveBox.className = 'pg-save show';
  };

  function init() {
    var list = document.querySelectorAll('.playground');
    for (var i = 0; i < list.length; i++) if (!list[i].classList.contains('pg')) new Playground(list[i]);
  }
  window.KCPlayground = Playground;
  window.KCPlayground.init = init;
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
