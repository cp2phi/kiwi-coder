# 🐞 病号 2：不报错，但「整理输入」好像没起作用。治好它！
# Patient 2: no crash, but the tidying doesn't seem to work. Cure it!
# 期望输出 Wanted output:
# [rock]
# [paper]
# [scissors]

def tidy(text):
    text.strip()
    text.lower()
    return text

print("[" + tidy("  ROCK ") + "]")
print("[" + tidy("Paper") + "]")
print("[" + tidy(" scissors") + "]")
