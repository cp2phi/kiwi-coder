# 🔐 密码破译 第 9 关：过关检查（再用 3 本秘密密码本考 decode()）/ Secret Code level 9: win check (tests decode() with 3 more secret codebooks)
try:
    _has_fn = callable(decode)
except NameError:
    _has_fn = False
if not _has_fn:
    print("__KC_HINT__ 🧩 这一关要写一个函数 def decode(text, book):，用 return 交出解密后的消息。|🧩 This level needs a function def decode(text, book): that returns the decoded message.")
else:
    _tests = [(_plain, code_book, secret)]
    for _k in range(3):
        _b = _make_book()
        _p = random.choice(_phrases)
        _tests.append((_p, _b, _make_secret(_p, _b)))
    _fail = None
    for _t in _tests:
        if _fail is None:
            try:
                _got = decode(_t[2], _t[1])
            except Exception as _x:
                _got = "(出错 / error: " + str(_x) + ")"
            if _got != _t[0]:
                _fail = "🔬 检查员试了 decode(\"" + _t[2] + "\", book)，应该得到 \"" + _t[0] + "\"，你的是 \"" + str(_got) + "\"。"
                _fail = _fail + "|🔬 The inspector tried decode(\"" + _t[2] + "\", book): it should give \"" + _t[0] + "\", yours gave \"" + str(_got) + "\"."
    if _fail is None:
        print("__KC_WIN__")
    else:
        _zh = _fail.split("|")[0]
        _en = _fail.split("|")[1]
        if _got == _got.strip() and _got == _got.lower() and len(_got) == len(_t[0]):
            _zh = _zh + "你是在用 book 反过来查吗？（用参数 book，不要用 code_book）"
            _en = _en + " Are you looking things up backwards in book? (Use the parameter book, not code_book.)"
        else:
            _zh = _zh + "别忘了：前后的空格要去掉，大写要变小写。"
            _en = _en + " Don't forget: strip the spaces at the ends and turn capitals into lowercase."
        print("__KC_HINT__ " + _zh + "|" + _en)
