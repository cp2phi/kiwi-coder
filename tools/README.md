# 🧰 tools：教材的自动检查

```bash
cd tools && npm i            # 第一次：装 playwright（会下载一个浏览器）
cd ..
node tools/check-code.js     # 用网页 Python 跑所有 .py，确保都能运行
tools/build.sh               # 用 Docker 构建网站（和 GitHub Pages 一样的环境）→ _site/
node tools/check-links.js    # 检查 _site 里的坏链接
node tools/serve.js          # 本地预览 _site：http://localhost:4000/kiwi-coder/
```

写新课的规范见 [docs/AUTHORING.md](../docs/AUTHORING.md)。
