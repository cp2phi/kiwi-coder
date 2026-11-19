# 🔐 密码破译 第 7 关：过关检查 / Secret Code level 7: win check
try:
    _a = answer
except NameError:
    _a = None
if _a is None:
    print("__KC_HINT__ 📦 把解出来的密码放进变量 answer（比如 answer = \"...\"）。|📦 Put the decoded message into the variable answer (like answer = \"...\").")
elif _a == _plain:
    print("__KC_WIN__")
else:
    _msg = "🔍 answer 还不对。"
    _msg_en = "🔍 answer isn't right yet."
    _a = str(_a)
    _i = 0
    while _i < len(_plain) and _i < len(_a) and _a[_i] == _plain[_i]:
        _i = _i + 1
    if _i < len(secret):
        _c = secret[_i]
        if _c == " ":
            _msg = _msg + "第 " + str(_i + 1) + " 个字符是空格——空格不用变，原样留着。"
            _msg_en = _msg_en + " Character " + str(_i + 1) + " is a space — spaces don't change, keep them as they are."
        else:
            _msg = _msg + "第 " + str(_i + 1) + " 个字母 '" + _c + "' 应该退回成 '" + _plain[_i] + "'。退过 a 的时候，要从 z 那头接着数（试试 % 26）。"
            _msg_en = _msg_en + " Letter " + str(_i + 1) + " '" + _c + "' should go back to '" + _plain[_i] + "'. When you go back past a, carry on from z (try % 26)."
    else:
        _msg = _msg + "长度不一样：需要 " + str(len(_plain)) + " 个字符，你的有 " + str(len(_a)) + " 个。"
        _msg_en = _msg_en + " Wrong length: it needs " + str(len(_plain)) + " characters, yours has " + str(len(_a)) + "."
    print("__KC_HINT__ " + _msg + "|" + _msg_en)
