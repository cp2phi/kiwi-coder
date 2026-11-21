# 🔐 密码破译 第 8 关：过关检查（再用 3 条秘密消息考 decode()）/ Secret Code level 8: win check (tests decode() on 3 more secret messages)
try:
    _has_fn = callable(decode)
except NameError:
    _has_fn = False
if not _has_fn:
    print("__KC_HINT__ 🧩 这一关要写一个函数 def decode(text):，用 return 交出解密后的消息。|🧩 This level needs a function def decode(text): that returns the decoded message.")
else:
    _tests = [_plain]
    for _k in range(3):
        _tests.append(random.choice(_phrases))
    _fail = None
    for _p in _tests:
        if _fail is None:
            _e = _encode(_p)
            try:
                _got = decode(_e)
            except Exception as _x:
                _got = "(出错 / error: " + str(_x) + ")"
            if _got != _p:
                _fail = "🔬 检查员试了 decode(\"" + _e + "\")，应该得到 \"" + _p + "\"，你的是 \"" + str(_got) + "\"。再对一对例子找规律！|🔬 The inspector tried decode(\"" + _e + "\"): it should give \"" + _p + "\", yours gave \"" + str(_got) + "\". Compare with the examples and look for the rule!"
    if _fail is None:
        print("__KC_WIN__")
    else:
        print("__KC_HINT__ " + _fail)
