---
title: 作品墙
title_en: Gallery
playground: true
---

# 🎨 <span class="zh">我的作品墙</span><span class="en">My Gallery</span>

<p><span class="zh">放进 <code>my-work/</code> 文件夹的每一个 <code>.py</code> 文件，都会<b>自动</b>出现在这里，点 ▶ 就能运行！</span><span class="en">Every <code>.py</code> file in the <code>my-work/</code> folder shows up here <b>automatically</b>. Click ▶ to run it!</span></p>

<div class="box box-tip"><span class="box-title"><span class="zh">➕ 怎么加新作品？</span><span class="en">➕ How do I add something?</span></span>
<span class="zh"><b>最简单：</b>在任何画板上点 <b>📤 存到作品墙</b>。<br>
<b>或者：</b>在 GitHub 打开 <a href="https://github.com/{{ site.github_repo }}/tree/{{ site.github_branch }}/my-work" target="_blank" rel="noopener">my-work 文件夹</a> → <b>Add file</b> → <b>Create new file</b> / <b>Upload files</b>。<br>
<b>小技巧：</b>代码的<b>第一行</b>写 <code># 🌈 作品名字</code>，作品墙就会用它当标题。</span>
<span class="en"><b>Easiest:</b> click <b>📤 Save to Gallery</b> on any playground.<br>
<b>Or:</b> open the <a href="https://github.com/{{ site.github_repo }}/tree/{{ site.github_branch }}/my-work" target="_blank" rel="noopener">my-work folder</a> on GitHub → <b>Add file</b> → <b>Create new file</b> / <b>Upload files</b>.<br>
<b>Tip:</b> write <code># 🌈 My title</code> on the <b>first line</b> of your code and the gallery uses it as the title.</span>
</div>

{% assign works = site.static_files | where: "extname", ".py" | sort: "path" | reverse %}
{% assign count = 0 %}
{% for f in works %}
  {% if f.path contains '/my-work/' %}
  {% assign count = count | plus: 1 %}
<div class="playground gallery-item" data-src="{{ f.path | relative_url }}" data-title="📄 {{ f.name }}" data-save="{{ f.basename }}" data-file="{{ f.name }}"></div>
<p style="margin:-.8em 0 2em;font-size:.85rem;text-align:right"><a href="https://github.com/{{ site.github_repo }}/edit/{{ site.github_branch }}{{ f.path }}" target="_blank" rel="noopener">✏️ <span class="zh">在 GitHub 上改它</span><span class="en">Edit on GitHub</span></a> · <span class="muted">{{ f.modified_time | date: "%Y-%m-%d" }}</span></p>
  {% endif %}
{% endfor %}

{% if count == 0 %}
<div class="card" style="text-align:center"><div class="big-emoji">🖼️</div><p><span class="zh">作品墙还是空的。去 <a href="{{ '/playground/' | relative_url }}">画板</a> 做一个吧！</span><span class="en">The gallery is empty. Go make something in the <a href="{{ '/playground/' | relative_url }}">Playground</a>!</span></p></div>
{% endif %}

<script>
  // 用代码第一行的注释当作品标题
  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.gallery-item').forEach(function (pg) {
      fetch(pg.getAttribute('data-src')).then(function (r) { return r.text(); }).then(function (code) {
        var first = code.split('\n')[0] || '';
        var m = /^#\s*(.+)$/.exec(first.trim());
        if (m) {
          var t = pg.querySelector('.pg-title');
          if (t) t.textContent = m[1] + '  ·  ' + pg.getAttribute('data-file');
        }
      }).catch(function () {});
    });
  });
</script>
