---
title: 游戏
title_en: Games
---

# 🎮 <span class="zh">游戏板块</span><span class="en">Games</span>

<p class="zh">每个游戏都是<b>用代码来玩</b>的：看目标 → 写几行指令 → 点运行 → 马上看到结果。过一关得一颗星 ⭐（记在这台电脑上，首页的徽章架能看到）。</p>
<p class="en">Every game here is <b>played with code</b>: look at the goal → write a few commands → click Run → see what happens. Each level you beat earns a star ⭐ (saved on this computer; see your badge shelf on the home page).</p>

<div class="box box-tip"><span class="zh">💡 不知道从哪开始？按<b>解锁的顺序</b>玩：上完第几课，就能玩标着「第几课」的游戏。卡住了就用四步法：读提示 → 翻笔记本 → 问 AI 要提示 → 问老师。</span><span class="en">💡 Not sure where to start? Play in <b>unlock order</b>: after lesson N you can play the games marked "Lesson N". Stuck? Use the 4 steps: read the hint → check your notebook → ask AI for a hint → ask your teacher.</span></div>

<div class="game-grid">
{% for g in site.data.games %}
  <a class="game-card{% if g.lesson > site.current_lesson %} locked{% endif %}" href="{{ '/games/' | append: g.id | append: '/' | relative_url }}">
    <span class="stars"><b data-badge-count="{{ g.id }}">0</b> / {{ g.levels }} ⭐</span>
    <div class="e">{{ g.icon }}</div>
    <h3><span class="zh">{{ g.title }}</span><span class="en">{{ g.title_en }}</span></h3>
    <p><span class="zh">{{ g.blurb }}</span><span class="en">{{ g.blurb_en }}</span></p>
    <span class="skill">🐍 <span class="zh">{{ g.skill }}</span><span class="en">{{ g.skill_en }}</span> · <span class="zh">第 {{ g.lesson }} 课后</span><span class="en">after Lesson {{ g.lesson }}</span></span>
  </a>
{% endfor %}
</div>

<div class="box box-think"><span class="box-title"><span class="zh">🧪 想自己发明一个游戏？</span><span class="en">🧪 Want to invent your own game?</span></span>
<span class="zh">去 <a href="{{ '/playground/' | relative_url }}">自由画板</a>，或者在第 10–12 课做你自己的项目！</span><span class="en">Head to the <a href="{{ '/playground/' | relative_url }}">Playground</a>, or build your own project in Lessons 10–12!</span></div>
