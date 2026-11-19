# 🔐 第 9 关：间谍密码本 / Level 9: the spy's codebook
# code_book 是「加密」用的字典：真字母 → 密码字母。比如 "a": "q" 表示 a 被写成了 q。
# code_book is the ENCODING dictionary: real letter → secret letter. "a": "q" means a was written as q.
# 密信还被弄乱了：有的字母是大写，前后多了空格。标点和中间的空格没有加密。
# The message got messy too: some letters are CAPITALS, with extra spaces at both ends. Punctuation and the spaces in between were not encoded.
# ⚠️ 密码本每次运行都会变！检查员还会用另外 3 本密码本考你的 decode(text, book)。
# ⚠️ The codebook changes every run! The inspector also tests decode(text, book) with 3 other codebooks.
print(code_book)
print("[" + secret + "]")

def decode(text, book):
    result = ""
    for c in text:
        result = result + book.get(c, c)    # 🤔 这是在「加密」还是「解密」？/ is this encoding or decoding?
    return result

print(decode(secret, code_book))
