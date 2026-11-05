#!/usr/bin/env bash
# 🏗️ 用 Docker 里的 GitHub Pages 环境构建网站到 _site/（和 GitHub 上一样的 Jekyll 版本）
#   tools/build.sh            构建
#   tools/build.sh serve      构建并在 http://localhost:4000/kiwi-coder/ 预览
set -e
cd "$(dirname "$0")/.."
IMG=kc-pages
if ! docker image inspect $IMG >/dev/null 2>&1; then
  echo "📦 第一次：构建 Docker 镜像（几分钟）…"
  docker build -q -t $IMG -f tools/Dockerfile.pages tools
fi
rm -rf _site
if [ "$1" = "serve" ]; then
  docker run --rm -it -p 4000:4000 -v "$PWD":/site $IMG jekyll serve -s /site -d /site/_site --host 0.0.0.0 --baseurl /kiwi-coder
else
  docker run --rm -v "$PWD":/site $IMG jekyll build -s /site -d /site/_site --safe
  echo "✅ 构建完成 → _site/"
fi
