---
title: Python 小词典
title_en: Python cheat sheet
---

# 📖 <span class="zh">Python 小词典</span><span class="en">Python cheat sheet</span>

<p><span class="zh">学过的每一个指令都在这里。忘了怎么写？来查一下，<b>点一下指令就能复制</b>。每一课学完，词典就会长大一点。</span><span class="en">Every command we've learned, all in one place. Forgot how to write something? Look it up — <b>click a command to copy it</b>. The dictionary grows a little after every lesson.</span></p>

{% assign keys = site.data.cheatsheet | sort %}
<div class="dict-nav">
{% for pair in site.data.cheatsheet %}{% assign sec = pair[1] %}
  <a href="#l{{ pair[0] }}"{% assign ln = pair[0] | plus: 0 %}{% if ln > site.current_lesson %} style="opacity:.45" onclick="var d=document.querySelector('.dict details');if(d)d.open=true"{% endif %}>{{ sec.icon }} <span class="zh">第 {{ pair[0] | plus: 0 }} 课</span><span class="en">L{{ pair[0] | plus: 0 }}</span></a>
{% endfor %}
</div>

<div class="dict">
{% assign later_shown = false %}
{% for pair in site.data.cheatsheet %}{% assign sec = pair[1] %}{% assign ln = pair[0] | plus: 0 %}
{% if ln > site.current_lesson and later_shown == false %}{% assign later_shown = true %}
<details class="hint" style="margin-top:2em"><summary><span class="zh">🔒 以后会学到的（想先偷看可以点开）</span><span class="en">🔒 Coming in later lessons (click to peek)</span></summary>
{% endif %}
<h2 id="l{{ pair[0] }}">{{ sec.icon }} <span class="zh">第 {{ pair[0] | plus: 0 }} 课：{{ sec.title }}</span><span class="en">Lesson {{ pair[0] | plus: 0 }}: {{ sec.title_en }}</span></h2>
<div class="table-wrap">
<table>
<tr><th><span class="zh">指令</span><span class="en">Command</span></th><th><span class="zh">它是干嘛的</span><span class="en">What it does</span></th><th><span class="zh">例子</span><span class="en">Example</span></th></tr>
{% for e in sec.entries %}
<tr><td><code class="dict-code">{{ e.code | escape }}</code></td><td><span class="zh">{{ e.zh }}</span><span class="en">{{ e.en }}</span></td><td><code class="dict-code">{{ e.example | escape }}</code></td></tr>
{% endfor %}
</table>
</div>
{% endfor %}
{% if later_shown %}</details>{% endif %}
</div>

<script>
document.querySelectorAll('.dict-code').forEach(function (c) {
  c.style.cursor = 'copy'; c.title = 'Copy';
  c.addEventListener('click', function () {
    if (navigator.clipboard) navigator.clipboard.writeText(c.textContent).catch(function () {});
    if (window.kcToast) kcToast('📋 <span class="zh">复制好了</span><span class="en">Copied</span>: <code>' + c.textContent.replace(/</g, '&lt;') + '</code>', 1400);
  });
});
</script>

<div class="box box-tip"><span class="zh">🧠 <b>记不住也没关系！</b>真正的程序员也天天查词典。重要的是知道<b>有这个东西</b>，和<b>去哪里查</b>。</span><span class="en">🧠 <b>It's fine not to remember everything!</b> Real programmers look things up every day. What matters is knowing <b>it exists</b> and <b>where to look</b>.</span></div>
