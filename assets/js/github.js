/* 🐙 从 GitHub 实时读 my-work/ 文件夹：作品墙、作业「已交」状态都用它
 * 不用登录（GitHub 允许每小时 60 次匿名请求），结果在这台电脑上缓存 2 分钟
 *   KCGit.list()            → Promise<[{name, path, sha, size, url}]>   my-work 里的 .py 文件
 *   KCGit.read(file)        → Promise<string>                           文件内容
 *   KCGit.lastCommit(path)  → Promise<{date, message} | null>
 */
(function () {
  'use strict';
  var cfg = window.KC || {};
  var API = 'https://api.github.com/repos/' + cfg.repo;
  var TTL = 2 * 60 * 1000;

  function cache(key, val) {
    try {
      if (val === undefined) {
        var raw = sessionStorage.getItem('kcgit-' + key);
        if (!raw) return null;
        var obj = JSON.parse(raw);
        if (Date.now() - obj.t > TTL) return null;
        return obj.v;
      }
      sessionStorage.setItem('kcgit-' + key, JSON.stringify({ t: Date.now(), v: val }));
    } catch (e) { return null; }
  }
  function get(url) {
    return fetch(url, { headers: { Accept: 'application/vnd.github+json' } }).then(function (r) {
      if (!r.ok) throw new Error('GitHub ' + r.status);
      return r.json();
    });
  }
  function list(force) {
    var c = force ? null : cache('list');
    if (c) return Promise.resolve(c);
    return get(API + '/contents/my-work?ref=' + cfg.branch + '&t=' + Date.now()).then(function (items) {
      var files = items.filter(function (f) { return f.type === 'file' && /\.py$/i.test(f.name); }).map(function (f) {
        return { name: f.name, path: f.path, sha: f.sha, size: f.size, url: f.url, download: f.download_url };
      });
      cache('list', files);
      return files;
    });
  }
  function read(file) {
    var c = cache('file-' + file.sha);
    if (c != null) return Promise.resolve(c);
    return get(file.url).then(function (j) {
      var txt = '';
      try { txt = decodeURIComponent(escape(atob((j.content || '').replace(/\n/g, '')))); } catch (e) { txt = atob((j.content || '').replace(/\n/g, '')); }
      cache('file-' + file.sha, txt);
      return txt;
    });
  }
  function lastCommit(path) {
    var c = cache('commit-' + path);
    if (c) return Promise.resolve(c);
    return get(API + '/commits?path=' + encodeURIComponent(path) + '&per_page=1&sha=' + cfg.branch).then(function (arr) {
      var k = arr && arr[0] ? { date: arr[0].commit.author.date, message: arr[0].commit.message } : null;
      cache('commit-' + path, k);
      return k;
    }).catch(function () { return null; });
  }
  window.KCGit = { list: list, read: read, lastCommit: lastCommit };

  // 作业页：<div class="hw-status" data-file="week02-homework.py"> 会实时变成 ✅ / ⏳
  document.addEventListener('DOMContentLoaded', function () {
    var boxes = document.querySelectorAll('.hw-status[data-file]');
    if (!boxes.length) return;
    list().then(function (files) {
      boxes.forEach(function (b) {
        var name = b.getAttribute('data-file');
        var hit = files.filter(function (f) { return f.name === name; })[0];
        b.className = 'box hw-status ' + (hit ? 'box-good' : 'box-warn');
        b.innerHTML = hit
          ? '<span class="zh">✅ <b>作业已经交啦！</b>在 <a href="' + (cfg.base || '') + '/gallery/#' + name + '">作品墙</a> 上能看到。想改？在下面改完再存一次（同名会提示已存在，就换个名字，比如加 -v2）。</span><span class="en">✅ <b>Homework handed in!</b> See it on the <a href="' + (cfg.base || '') + '/gallery/#' + name + '">Gallery</a>. Want to change it? Edit below and save again (if the name exists, add -v2).</span>'
          : '<span class="zh">⏳ <b>还没交</b>：做完后点画板上的 <b>📤 存到作品墙</b>，文件名用 <code>' + name.replace(/\.py$/, '') + '</code>，这里就会变成 ✅。</span><span class="en">⏳ <b>Not handed in yet</b>: when you\'re done, click <b>📤 Save to Gallery</b> on the playground and name it <code>' + name.replace(/\.py$/, '') + '</code>. This turns into ✅.</span>';
      });
    }).catch(function () {});
  });
})();
