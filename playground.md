---
title: 自由画板
title_en: Playground
playground: true
---

# 🧪 <span class="zh">自由画板</span><span class="en">Playground</span>

<p><span class="zh">想试什么就试什么！代码会<b>自动记在这台电脑上</b>。做出满意的作品，就点 <b>📤 存到作品墙</b>。</span><span class="en">Try anything you like! Your code is <b>saved on this computer automatically</b>. Made something you love? Click <b>📤 Save to Gallery</b>.</span></p>

<div class="playground" data-title="🧪 自由画板" data-title-en="🧪 Playground" data-save="my-drawing" data-draft="free" data-images>
<textarea># 🎨 我的新作品 My new drawing
import turtle

t = turtle.Turtle()
t.shape("turtle")

t.forward(100)
</textarea>
</div>

<div class="box box-tip"><span class="box-title"><span class="zh">🖼️ 让海龟变成你的图片</span><span class="en">🖼️ Turn the turtle into your picture</span></span>
<span class="zh">① 点画板上的 <b>🖼️ 图片</b>，选一张 GIF / PNG / JPG（会自动缩小）。② 在代码里这样写（文件名要和上传的<b>一模一样</b>）：</span>
<span class="en">① Click <b>🖼️ Picture</b> on the playground and choose a GIF / PNG / JPG (it gets shrunk automatically). ② Write this in your code (the file name must match <b>exactly</b>):</span>
<pre style="margin:.6em 0">import turtle

screen = turtle.Screen()
screen.addshape("dog.gif")   # 先把图片注册成形状 / register the picture as a shape

t = turtle.Turtle()
t.shape("dog.gif")           # 再使用它 / then use it
t.forward(100)</pre>
<span class="zh">图片不会跟着海龟转方向（电脑上的 Python 也是这样）。</span><span class="en">The picture doesn't turn when the turtle turns (same as Python on a computer).</span>
</div>

<div class="cmds">
  <div class="cmd"><code>t.forward(100)</code><span><span class="zh">往前走</span><span class="en">Move forward</span></span></div>
  <div class="cmd"><code>t.left(90)</code> / <code>t.right(90)</code><span><span class="zh">左转 / 右转</span><span class="en">Turn left / right</span></span></div>
  <div class="cmd"><code>t.color("red")</code><span><span class="zh">笔的颜色</span><span class="en">Pen colour</span></span></div>
  <div class="cmd"><code>t.pensize(5)</code><span><span class="zh">笔的粗细</span><span class="en">Pen thickness</span></span></div>
  <div class="cmd"><code>t.speed(0)</code><span><span class="zh">最快速度</span><span class="en">Fastest speed</span></span></div>
  <div class="cmd"><code>turtle.bgcolor("black")</code><span><span class="zh">背景颜色</span><span class="en">Background colour</span></span></div>
  <div class="cmd"><code>t.penup()</code> / <code>t.pendown()</code><span><span class="zh">抬笔 / 落笔</span><span class="en">Pen up / pen down</span></span></div>
  <div class="cmd"><code>t.goto(x, y)</code><span><span class="zh">走到某个位置</span><span class="en">Go to a spot</span></span></div>
  <div class="cmd"><code>t.circle(50)</code><span><span class="zh">画圆</span><span class="en">Draw a circle</span></span></div>
  <div class="cmd"><code>t.begin_fill()</code> … <code>t.end_fill()</code><span><span class="zh">涂满颜色</span><span class="en">Fill with colour</span></span></div>
</div>

<div class="swatches" data-colors="red orange gold yellow limegreen green turquoise deepskyblue blue navy purple violet hotpink pink brown black white gray"></div>

<div class="box box-tip"><span class="zh">💻 <b>想在电脑上运行？</b>点 <b>⬇ 下载</b> 得到 <code>.py</code> 文件，用 <b>Thonny</b> 或 <b>VS Code</b> 打开运行。</span><span class="en">💻 <b>Want to run it on your computer?</b> Click <b>⬇ Download</b> to get a <code>.py</code> file and open it in <b>Thonny</b> or <b>VS Code</b>.</span></div>
