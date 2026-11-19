# 🐞 虫虫医院 病号 9：检查（再用 2 份秘密记录测试）/ Bug Hospital patient 9: check (tests with 2 more secret lists)
try:
    _has_fn = callable(count_birds) and callable(most_seen)
except NameError:
    _has_fn = False

if not _has_fn:
    print("__KC_HINT__ 🩺 函数 count_birds 或 most_seen 不见了！别删掉，也别改名字。|🩺 count_birds or most_seen has gone missing! Don't delete or rename them.")
else:
    _fail = None
    for _lst in [_sightings, _make_list(), _make_list()]:
        if _fail is None:
            _want = _count(_lst)
            try:
                _got = count_birds(_lst[:])
            except Exception as _x:
                _got = "error: " + str(_x)
            if _got != _want:
                _fail = "🔬 检查员试了 count_birds(" + str(_lst) + ")，应该得到 " + str(_want) + "，函数给了 " + str(_got) + "。"
                _fail = _fail + "|🔬 The inspector tried count_birds(" + str(_lst) + "): it should give " + str(_want) + ", the function gave " + str(_got) + "."
                _messy_keys = False
                if type(_got) == dict:
                    for _k in _got:
                        if type(_k) == str and _k != _k.strip().lower():
                            _messy_keys = True
                if _messy_keys:
                    _fail = _fail.replace("|", "\"Kiwi\"、\" kiwi\" 和 \"kiwi\" 是同一种鸟——数之前先把名字洗干净（第 8 课的魔法）。|") + " \"Kiwi\", \" kiwi\" and \"kiwi\" are the same bird — clean the name before counting (Lesson 8 magic)."
                else:
                    _fail = _fail.replace("|", "每种鸟只数到 1？看看「已经见过」的时候，数字是加 1 还是被改回了 1。|") + " Every bird only counts to 1? When a bird has been seen before, does the number go up by 1 — or get reset to 1?"
            else:
                _wtop = _top(_want)
                try:
                    _gtop = most_seen(dict(_want))
                except Exception as _x:
                    _gtop = "error: " + str(_x)
                if _gtop != _wtop:
                    _fail = "🔬 count_birds 治好了！但 most_seen(" + str(_want) + ") 应该是 \"" + _wtop + "\"，函数给了 \"" + str(_gtop) + "\"。函数是不是只看了第一种鸟就 return 了？看看 return 的缩进。"
                    _fail = _fail + "|🔬 count_birds is cured! But most_seen(" + str(_want) + ") should be \"" + _wtop + "\" and the function gave \"" + str(_gtop) + "\". Did it return after looking at only the first bird? Check the indentation of return."
    if _fail is None:
        print("__KC_WIN__")
    else:
        print("__KC_HINT__ " + _fail)
