---
title: 自由画板
playground: true
---

# 🧪 自由画板

想试什么就试什么！代码会<b>自动记在这台电脑上</b>。做出满意的作品，就点 <b>📤 存到作品墙</b>。

<div class="playground" data-title="🧪 自由画板" data-save="my-drawing" data-draft="free">
<textarea># 🎨 我的新作品
import turtle

t = turtle.Turtle()
t.shape("turtle")

t.forward(100)
</textarea>
</div>

<div class="cmds">
  <div class="cmd"><code>t.forward(100)</code><span>往前走</span></div>
  <div class="cmd"><code>t.left(90)</code> / <code>t.right(90)</code><span>左转 / 右转</span></div>
  <div class="cmd"><code>t.color("red")</code><span>笔的颜色</span></div>
  <div class="cmd"><code>t.pensize(5)</code><span>笔的粗细</span></div>
  <div class="cmd"><code>t.speed(0)</code><span>最快速度</span></div>
  <div class="cmd"><code>turtle.bgcolor("black")</code><span>背景颜色</span></div>
  <div class="cmd"><code>t.penup()</code> / <code>t.pendown()</code><span>抬笔 / 落笔</span></div>
  <div class="cmd"><code>t.goto(x, y)</code><span>走到某个位置</span></div>
  <div class="cmd"><code>t.circle(50)</code><span>画圆</span></div>
  <div class="cmd"><code>t.begin_fill()</code> … <code>t.end_fill()</code><span>涂满颜色</span></div>
</div>

<div class="swatches" data-colors="red orange gold yellow limegreen green turquoise deepskyblue blue navy purple violet hotpink pink brown black white gray"></div>

<div class="box box-tip"><span class="box-title">💻 想在电脑上运行？</span>点 <b>⬇ 下载</b> 得到 <code>.py</code> 文件，用 <b>Thonny</b> 或 <b>VS Code</b> 打开运行。电脑上的 Python 能做的事情比网页更多！</div>
