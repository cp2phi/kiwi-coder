---
title: 第 1 课 · 教案
title_en: Lesson 1 · Teacher plan
lesson: "01"
tab: teacher
---

# 👩‍🏫 第 1 课教案（给老师 / 家长）

<p class="en box box-tip">This page is the lesson plan for the teacher / parent and is written in Chinese only.</p>

**目标：** 让孩子觉得 AI 和编程**很酷**，而且**自己能做到**。知识点很少，「我做出来了」的体验最重要。

**今天的一条铁律：** 老师**尽量不碰键盘和鼠标**。手放在背后，用嘴说「你猜？」「点哪里？」「报错说了什么？」——这就是「授之以渔」的第一步。

---

## 📋 课前准备（今晚做完）

<ul class="quests" data-key="teacher-prep">
  <li><b>账号</b>：GitHub 和 ChatGPT/Codex 的服务条款都要求<b>满 13 岁</b>。6 年级孩子通常不到 13 岁，建议<b>用家长的账号</b>（仓库主人就是家长账号），家长在旁边陪着登录、使用。等孩子满 13 岁，再给他开自己的账号，加为仓库协作者（Settings → Collaborators）。</li>
  <li><b>打开 GitHub Pages</b>：仓库 → Settings → Pages → Source 选 <b>Deploy from a branch</b>，Branch 选 <b>main</b> / <b>(root)</b> → Save。2 分钟后打开网站确认能访问。</li>
  <li><b>自己走一遍「改名片」</b>：改 <code>_data/me.yml</code> → Commit → 看 Actions 变绿 → 首页更新。记一下大概要等多久（通常 1 分钟左右）。</li>
  <li><b>试一遍 Codex</b>：用「提示词配方」生成一段指令，发给 Codex，把代码贴进 AI 画板运行。</li>
  <li><b>试一遍「存到作品墙」</b>：在画板点 📤，确认 GitHub 新建文件页能打开、能 Commit、作品墙能显示。</li>
  <li><b>备用方案</b>：网不好的话，电脑上装 <a href="https://thonny.org" target="_blank" rel="noopener">Thonny</a>，把 <code>lessons/01/code/</code> 里的 .py 文件下载好。</li>
  <li>准备一个<b>实体本子</b>当「工程师笔记本」（网站上的笔记本是电子版，两个都可以）。</li>
  <li>把网站加到浏览器书签栏，命名「我的编程基地」。</li>
</ul>

---

## ⏱️ 60 分钟时间表

<div class="table-wrap">
<table>
<tr><th>时间</th><th>环节</th><th>做什么 / 说什么</th><th>观察点</th></tr>
<tr><td><b>0–8</b></td><td>👋 破冰</td><td>聊：平时玩什么？喜欢什么游戏、动物、运动？Minecraft？最近在看什么？<br><b>问：「你觉得 AI 是什么？」</b>不纠正，只记下来——12 周后再问一次对比。<br>💬「今天结束时，你会有一个自己的网站，和一幅 AI 帮你画的画。」</td><td>把兴趣记下来（见下面的记录表），以后的项目都用它包装</td></tr>
<tr><td><b>8–20</b></td><td>🐙 GitHub</td><td>打开 <a href="../github/">GitHub 页</a>，孩子读、你补充 3 个比喻：<b>魔法文件夹 / 游戏存档 / 自动变网站</b>。<br>带他打开真实仓库，对照示意图找到 ①–⑥。<br><b>主任务：改名片</b>（把破冰聊到的内容写进 <code>me.yml</code>）→ Commit → 一起看 Actions 转圈 → 刷新首页 🎉</td><td>等待的 1 分钟正好讲 Actions。如果 YAML 写坏了（❌），别急着修——这是第一次「读报错」的好机会</td></tr>
<tr><td><b>20–27</b></td><td>🤖 Codex</td><td>打开 <a href="../codex/">Codex 页</a>。重点只讲两件事：<b>你是队长</b>、<b>三条守则</b>。<br>让他用 💬 问模式自己打字问 2–3 个问题（页面上有清单）。<br>特别让他问：「你会犯错吗？」</td><td>他打字慢没关系，别替他打</td></tr>
<tr><td><b>27–45</b></td><td>🐍 Python</td><td>打开 <a href="../python/">Python 页</a>，按页面顺序：<br>① Hello（5 分钟）：改名字 → 加一行 → 故意删引号看报错<br>② 正方形 PRIMM（10 分钟）：<b>先做猜一猜再运行</b>；90→120 一定要先猜<br>③ 挑战三角形 / 星星（5 分钟）：能不看提示就不看，引导他自己说出「转角 × 次数 = 360」</td><td>哪一步最兴奋？哪一步卡住？报错时他第一反应是什么？</td></tr>
<tr><td><b>45–54</b></td><td>✨ AI 画画</td><td>选一个点子（<b>用他的兴趣！</b>）→ 提示词配方 → 复制给 Codex → 贴到 AI 画板运行 → <b>改 1 个数字</b> → 📤 存到作品墙。</td><td>他会不会主动读 AI 的代码？有没有认出 forward / left？</td></tr>
<tr><td><b>54–60</b></td><td>📓 收尾</td><td>让他<b>给家人讲</b>今天做的东西（讲出来 = 真学会）。<br>写工程师笔记本 3 行。<br>花 1 分钟看<a href="../homework/">作业页</a>：说清楚青铜必做、其他随意；告诉他怎么交。</td><td>他能不能用自己的话说出 commit 和 forward 是什么</td></tr>
</table>
</div>

<div class="box box-warn"><span class="box-title">⏰ 时间不够时怎么砍</span>
优先级：<b>改名片</b> &gt; <b>Hello + 正方形 PRIMM</b> &gt; AI 画画 &gt; 挑战星星 &gt; Codex 提问。<br>
AI 画画来不及，就老师演示一遍。宁可做少，也别赶。
</div>

---

## 🗣️ 好用的话术

- 「**先别运行，你猜会怎样？**」（每次运行前都问，猜错了更好，最有印象）
- 「报错说了什么？**第几行**？」（不替他读，让他读）
- 「这个问题很好，**你觉得可以问谁**？」（引导到笔记本 / AI / 老师的顺序）
- 「AI 给的代码里，**哪一行你认识**？」
- 夸**过程**不夸聪明：「你刚才自己发现了 360 的规律！」而不是「你真聪明」。

## 📝 破冰记录表

（课后把这些写进 <code>_data/me.yml</code> 的 likes，或者记在自己的本子里）

- 喜欢的游戏：
- 喜欢的动物：
- 喜欢的运动 / 活动：
- 最近着迷的东西：
- 「AI 是什么」他的回答：
- 他对哪个环节最兴奋：

---

## 🔁 课后（这周内）

<ul class="quests" data-key="teacher-after">
  <li>作业交上来后（<code>my-work/week01-homework.py</code>），在 <a href="{{ '/feedback/' | relative_url }}">老师的话</a> 写反馈：1 个具体的表扬 + 1 个用提问方式的建议</li>
  <li>看他的笔记本，在下节课开头花 2 分钟聊「你卡在哪里、怎么解决的」</li>
  <li>准备第 2 课：复制 <code>lessons/01/</code> 改成 <code>lessons/02/</code>，在 <code>_data/lessons.yml</code> 把第 2 课设成 <code>ready: true</code>，在 <code>_config.yml</code> 改 <code>current_lesson: 2</code></li>
  <li>把他的兴趣用到第 2 课（聊天程序）的包装里：比如「Minecraft 村民聊天机器人」</li>
</ul>
