# 🔐 密码破译 第 9 关：隐藏代码（随机密码本 + 乱糟糟的密信）/ Secret Code level 9: hidden setup (a random codebook + a messy message)
import random

_phrases = ["meet at the big tree!", "the kiwi is in the nest", "pizza party at noon!", "hide the map under the rock", "the eagle has landed", "bring two apples and a torch", "go left at the river", "the password is pohutukawa", "dont tell the teacher!", "the cake is a lie"]
_abc = "abcdefghijklmnopqrstuvwxyz"


def _make_book():
    # 加密用的密码本：真字母 → 密码字母 / the ENCODING book: real letter → secret letter
    letters = []
    for c in _abc:
        letters.append(c)
    random.shuffle(letters)
    book = {}
    for i in range(26):
        book[_abc[i]] = letters[i]
    return book


def _make_secret(plain, book):
    # 加密，再弄乱：随机大写 + 前后多几个空格 / encode it, then mess it up: random capitals + extra spaces at both ends
    out = " " * random.randint(1, 3)
    for c in plain:
        if c in book:
            c = book[c]
            if random.random() < 0.4:
                c = c.upper()
        out = out + c
    return out + " " * random.randint(1, 3)


code_book = _make_book()
_plain = random.choice(_phrases)
secret = _make_secret(_plain, code_book)
