# 🔐 密码破译 第 8 关：隐藏代码（间谍密码机，每次随机出题）/ Secret Code level 8: hidden setup (the spy machine, a new message every run)
import random

_phrases = ["meet at the beach", "the eagle has landed", "kiwi birds cannot fly", "hide the map", "bring two apples", "go left at the river", "the code is purple", "pizza at noon", "look under the bridge", "the tui sings at dawn", "run to the waka", "the treasure is in the cave"]


def _encode(text):
    # 密码机：先倒过来，再在每个字符后面塞一个乱码字母 / the machine: reverse it, then stuff a junk letter after every character
    out = ""
    for c in text[::-1]:
        out = out + c + chr(random.randint(97, 122))
    return out


_plain = random.choice(_phrases)
secret = _encode(_plain)
