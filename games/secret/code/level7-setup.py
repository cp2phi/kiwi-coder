# 🔐 密码破译 第 7 关：隐藏代码（每次运行随机出题）/ Secret Code level 7: hidden setup (a new puzzle every run)
import random

_words = ["kiwi", "pizza", "zebra", "taniwha", "volcano", "yellow", "jazz", "fox", "wizard", "quiz", "sky", "beach", "lizard", "waka", "tuatara", "pukeko", "rugby", "wave", "storm", "moana"]


def _shift(text, k):
    out = ""
    for c in text:
        if c == " ":
            out = out + c
        else:
            out = out + chr((ord(c) - 97 + k) % 26 + 97)
    return out


def _wraps(text, k):
    # 至少有一个字母要「转过 z」，不然这关太简单 / at least one letter must wrap past z
    for c in text:
        if c != " " and ord(c) - 97 + k >= 26:
            return True
    return False


_plain = random.choice(_words) + " " + random.choice(_words)
key = random.randint(3, 23)
while not _wraps(_plain, key):
    _plain = random.choice(_words) + " " + random.choice(_words)
    key = random.randint(3, 23)
secret = _shift(_plain, key)
